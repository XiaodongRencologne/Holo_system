# FYST Observatory Control System

## Running

Start with:

    ./run.bash

and then open [https://127.0.0.1:5600](https://127.0.0.1:5600) in a browser.

## Connecting via mTLS

The `tls/make-certs.bash` script creates server, client, and CA certificates for
[mTLS authentication](https://www.cloudflare.com/en-ca/learning/access-management/what-is-mutual-tls/).
This script is automatically run by the `run.bash` script.

Here's an example of connecting via `curl` using the certificates:

    curl --cacert tls/server.cert.pem \
         --cert tls/client.cert.pem \
         --key tls/client.key.pem \
         https://localhost:5600/auth/userinfo

And here's an example using python's [requests](https://docs.python-requests.org/) library:

```python
import requests
s = requests.Session()
s.verify = 'tls/server.cert.pem'
s.cert = ('tls/client.cert.pem','tls/client.key.pem')
response = s.get('https://127.0.0.1:5600/api/v1/weather/current').json()
```

## Querying FYST's Housekeeping Timeseries InfluxDB

This Rest API enables queries of FYST's housekeeping timeseries database through
appropriate calls, too. Such, user circumvent having to code individual flux queries.
Its purpose is to serve the instrumental teams to inquire
relevant data for their observations. For anyone interested in the hidden 
details, this Rest API casts the request body - provided by the client - into dynamical
[Flux](https://www.influxdata.com/products/flux/) statements allowing to query
FYST's Housekeeping influxDB.

All Housekeeping data is stored in bucket "Housekeeping", analog to an Oracle 
database schema. Measurements (in Oracle similar to tables) in that bucket 
can be queried for field key/value pairs. Moreover, 
various endpoints permit queries of tags, their values and field keys 
being available in a measurement.

Rest API requests might be issued via
* CLI *curl* (see examples below)
* The request body of a *curl* statement can also be cast into 
[Requests](https://pypi.org/project/requests/) being part of an observer's 
Rest API client. 

For the time being, only JSON or CSV is provided as output format. Conversions to any
other formats, such as fits, need to be performed in the Rest API client.

### Exemplary curl calls

where accept header is

    "accept:application/json" or 
    "accept:text/csv"

List of measurements in the "Housekeeping" bucket
```bash
curl -X GET https://localhost:5600/api/v1/housekeeping/measurement/list \
--cacert tls/server.cert.pem \
--cert tls/client.cert.pem \
--key tls/client.key.pem \
-H "accept: text/csv"
```

List of tag keys in a measurement
```bash
curl -X POST https://localhost:5600/api/v1/housekeeping/measurement/tagKey \
--cacert tls/server.cert.pem \
--cert tls/client.cert.pem \
--key tls/client.key.pem \
-H "accept: text/csv" \
-H "Content-Type:application/json" \
-d '{"measurement": "Power.PDU.outlets"}'
```

List of values for a tag key in a measurement
```bash
curl -X POST https://localhost:5600/api/v1/housekeeping/measurement/tagValue \
--cacert tls/server.cert.pem \
--cert tls/client.cert.pem \
--key tls/client.key.pem \
-H "accept: text/csv" \
-H "Content-Type:application/json" \
-d '{"measurement": "Power.PDU.outlets", "tagKey": "pdu_hostname"}'
```

List of field key in a measurement
```bash
curl -X POST https://localhost:5600/api/v1/housekeeping/measurement/fieldKey \
--cacert tls/server.cert.pem \
--cert tls/client.cert.pem \
--key tls/client.key.pem \
-H "accept: text/csv" \
-H "Content-Type:application/json" \
-d '{"measurement": "Power.PDU.outlets"}'
```

List of field/value pairs for a list of field keys, a list of tag keys and a given time range:
```bash
curl -X POST https://localhost:5600/api/v1/housekeeping/measurement \
--cacert tls/server.cert.pem \
--cert tls/client.cert.pem \
--key tls/client.key.pem \
-H "accept: text/csv" \
-H "Content-Type:application/json" \
-d '{"measurement": "Power.PDU.outlets",
"fieldKey": ["voltage_V", "powerFactor"],
"tags": {"ip": ["10.10.1.40", "10.10.1.41"],
         "name": ["Aruba_16port_ffts_switch", "Rack_HEX"]},
"time_from": "2023-02-08T08:10:22.000000Z", 
"time_to": "2023-02-08T08:50:22.000000Z"}'
```

where
```
bucket: "Housekeeping" (preassigned)
measurement: str
fieldKey: Optional[List[str]] ([] defaults to all)
tags: Optional[Dict[str, List[str]] ({} defaults to all)
time_from: datetime
time_to: Optional[datetime] (defaults to now)
```
Constraints:
```
time_to - time_from < 7 days
```

Yet lacking: units and comments per field, as those ain't available in the 
influxdb. Stay tuned: Reinhold & Ralf are men at work!

Also provided is a 
[python example](https://github.com/ccatobs/observatory-control-system/blob/main/OCS_RestAPI_client_template/instrument_request.py) - on the client site -
enabling the instrumental teams to download data to either a JSON or CSV file. 

Caveat: the host address will be subject to change!

Contact: Ralf A. Timmermann, AIfA, University Bonn, email: rtimmermann@astro.uni-bonn.de
