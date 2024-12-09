import requests
import shutil
import json
import logging

LOGGING_LEVEL = "INFO"
logging.getLogger().setLevel(level=getattr(logging, LOGGING_LEVEL))


class MyException(Exception):
    def __init__(self, status_code, detail):
        super(MyException, self).__init__(status_code, detail)
        self.status_code = status_code
        self.detail = detail


def download_file(**kwargs):
    headers = {'Content-type': 'application/json',
               'Accept': kwargs.get('accept', "application/json")}
    default = "download.csv" if headers.get('Accept') == "text/csv" else "download.json"
    path = kwargs.get('path', "tls")
    try:
        with getattr(requests, str.lower(kwargs.get('method', 'get')))(
                kwargs.get('url'),
                verify='{}/server.cert.pem'.format(path),
                cert=(
                    '{}/client.cert.pem'.format(path),
                    '{}/client.key.pem'.format(path)
                ),
                data=json.dumps(kwargs.get('data')),
                headers=headers,
                stream=True
        ) as r:
            if r.status_code == 200:
                with open(kwargs.get('filename', default), 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
            else:
                raise MyException(
                    status_code=r.status_code,
                    detail=r.reason
                )
    except Exception as e:
        logging.error("Download failed with error message: {}".format(str(e)))
        return 1
    logging.info("Download succeeded")
    return 0


if __name__ == '__main__':
    url = "https://localhost:5600/api/v1/housekeeping/measurement"
    method = "POST"  # or "GET"
    cert_path = "tls"  # location of certificates
    filename = 'download.json'  # optional, default download.json|csv
    accept = "application/json"  # alternatively 'text/csv'
    data = {"measurement": "Power.PDU.outlets",
            "fieldKey": ["powerFactor", "outletState"],
            "tags": {"ip": ["10.10.1.40", "10.10.1.41"],
                     "name": ["Aruba_16port_ffts_switch", "Rack_HEX"]
                     },
            "time_from": "2023-02-08T08:49:22.000000Z",
            "time_to": "2023-02-09T08:59:22.000000Z"
            }
    rc = download_file(
        method=method,
        url=url,
        path=cert_path,
        data=data,
        filename=filename,
        accept=accept
    )

    exit(rc)
