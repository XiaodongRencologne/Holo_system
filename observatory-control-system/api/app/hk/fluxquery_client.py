from influxdb_client import InfluxDBClient
from influxdb_client.client.exceptions import InfluxDBError
from influxdb_client.client.warnings import MissingPivotFunction
from influxdb_client.client.query_api import QueryApi
from urllib3.exceptions import NewConnectionError
import os
import json
import pandas as pd
from pandas.core.frame import DataFrame
import logging
from .RestAPI_aux import get_secret, MyException, query_constructor
import warnings
from typing import Tuple, Dict

warnings.simplefilter("ignore", MissingPivotFunction)

# InfluxDB parameter
INFLUXDB_HOST = os.getenv('INFLUXDB_HOST', "localhost")
INFLUXDB_PORT = int(os.getenv('INFLUXDB_PORT', 8086))
INFLUXDB_TOKEN = get_secret("SECRET_KEY", os.getenv('INFLUXDB_TOKEN', ""))
INFLUXDB_URL = "http://{0}:{1}".format(INFLUXDB_HOST, INFLUXDB_PORT)
INFLUXDB_ORG = os.getenv('INFLUXDB_ORG', "ccat")
INFLUXDB_BUCKET = os.getenv('INFLUXDB_BUCKET', "Housekeeping")
INFLUXDB_READ_TIMEOUT = os.getenv('INFLUXDB_READ_TIMEOUT', 60_000)
# Logging parameter
LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'DEBUG')
myformat = "%(asctime)s.%(msecs)03d :: %(levelname)s: %(filename)s - " \
           "%(lineno)s - %(funcName)s()\t%(message)s"
logging.basicConfig(format=myformat,
                    level=getattr(logging, LOGGING_LEVEL),
                    datefmt="%Y-%m-%d %H:%M:%S")


def client_open() -> Tuple[InfluxDBClient, QueryApi]:
    client = InfluxDBClient(
        url=INFLUXDB_URL,
        token=INFLUXDB_TOKEN,
        org=INFLUXDB_ORG,
        timeout=INFLUXDB_READ_TIMEOUT
    )
    return client, client.query_api()  # Create an influxdb-client and Query API instance


def retrieve(bucket: str,
             parameter: Dict) -> DataFrame:
    """
    key field/value pairs depending on where predicates tag keys, field keys
    and time range
    :param bucket: str, influxdb v2.x bucket
    :param parameter: dict input parameter, see top
    :return: pandas dataframe
    """
    client, query_api = client_open()

    # if no time_to is provided -> now()
    time_to_predicate = "now()" if parameter.get('time_to') is None else "time(v: _time_to)"

    where_predicate = "\n|> filter(fn: (r) => r._measurement == {})".format(json.dumps(parameter.get('measurement')))
    # build a dynamic tag filter
    tags = parameter.get("tags") if parameter.get("tags") is not None else dict()
    # if tags provided, defaulted to empty dict
    for tagkey in tags:
        if tags[tagkey]:
            where_predicate += "\n|> filter(fn: (r) => "
            for tagvalue in tags[tagkey]:
                where_predicate += \
                    "r.{0} == {1} or ".format(tagkey, json.dumps(tagvalue))
            where_predicate = where_predicate.rstrip("or ") + ")"

    # append a dynamic field key filter
    fieldvalue = parameter.get('fieldKey')
    # if fieldKey provided, defaulted to empty list
    if fieldvalue:
        where_predicate += "\n|> filter(fn: (r) => "
        for item in fieldvalue:
            where_predicate += "r._field == {0} or ".format(json.dumps(item))
        where_predicate = where_predicate.rstrip("or ") + ")"

    # if no tags provided then no keep function -> all fields kept
    keep_predicate = ""
    if tags:
        keep_predicate = "\n|> keep(columns: {})".format(
            json.dumps(["time", "field", "value", "measurement"] + [tag for tag in tags]))

    # parameter set
    params = {
        "_bucket": bucket,
        "_time_from": parameter.get('time_from'),
        "_time_to": parameter.get('time_to'),
        "_drop": ["_start", "_stop", "index", "label"]
    }
    query = '''
import "regexp"
from(bucket: _bucket)
|> range(start: time(v: _time_from), stop: {0}){1}
|> rename(fn: (column) => (regexp.replaceAllString(r: /^_/, v:column, t: "")))
|> drop(columns: _drop){2}'''.format(time_to_predicate,  # either time_to or now()
                                     where_predicate,  # filter by tags and/or fieldKeys
                                     keep_predicate)  # all tags or solely those chosen
    # logging.debug("query: {0}\nparameter: {1}".format(query, params))
    logging.debug(query_constructor(query=query, parameter=params))
    try:
        df = query_api.query_data_frame(query=query,
                                        params=params)
    except NewConnectionError:
        logging.error("NewConnectionError encountered")
        raise MyException(status_code=500,
                          detail="Connection could not be established")
    except InfluxDBError as e:
        logging.error("InfluxDBError: Status={0}, Message={1}"
                      .format(e.response.status, e.message))
        raise MyException(status_code=e.response.status,
                          detail=e.message)
    finally:
        client.close()

    no_frame = 1
    if any(isinstance(frame, DataFrame) for frame in df):
        no_frame = len(df)
        df = pd.concat([frame for frame in df], ignore_index=True)
    if not df.empty:
        df = df.drop(columns=["result"])
    logging.debug("Total number of {0} record(s) in {1} DataFrame(s)".format(len(df), no_frame))

    return df


def list_measurement(bucket: str) -> DataFrame:
    """
    measurements in a bucket
    :param bucket: str, influxdb v2.x bucket
    :return: pandas dataframe
    """
    client, query_api = client_open()

    params = {"_bucket": bucket}
    query = '''
import "regexp"
import "influxdata/influxdb/schema"
schema.measurements(bucket: _bucket)
|> rename(fn: (column) => (regexp.replaceAllString(r: /^_/, v:column, t: "")))'''
    # logging.debug("query: {0}\nparameter: {1}".format(query, params))
    logging.debug(query_constructor(query=query, parameter=params))
    try:
        df = query_api.query_data_frame(query=query,
                                        params=params)
    except NewConnectionError:
        logging.error("NewConnectionError encountered")
        raise MyException(status_code=500,
                          detail="Connection could not be established")
    except InfluxDBError as e:
        logging.error("InfluxDBError: Status={0}, Message={1}"
                      .format(e.response.status, e.message))
        raise MyException(status_code=e.response.status,
                          detail=e.message)
    finally:
        client.close()
    if not df.empty:
        df = df.drop(columns=["result"])
    logging.debug("Total number of records: {}".format(len(df)))

    return df


def list_tag(bucket: str,
             parameter: Dict) -> DataFrame:
    """
    tag keys of a measurememt
    :param bucket: str, influxdb v2.x bucket
    :param parameter: dict input parameter, see top
    :return: pandas dataframe
    """
    client, query_api = client_open()

    params = {
        "_bucket": bucket,
        "_measurement": parameter.get('measurement')
    }
    query = '''
import "regexp"
import "influxdata/influxdb/schema"
fields = ["_start", "_stop", "_field", "_measurement"]
schema.measurementTagKeys(
bucket: _bucket,
measurement: _measurement)
|> filter(fn: (r) => not contains(value: r._value, set: fields))
|> rename(fn: (column) => (regexp.replaceAllString(r: /^_/, v:column, t: "")))'''
    # logging.debug("query: {0}\nparameter: {1}".format(query, params))
    logging.debug(query_constructor(query=query, parameter=params))
    try:
        df = query_api.query_data_frame(query=query,
                                        params=params)
    except NewConnectionError:
        logging.error("NewConnectionError encountered")
        raise MyException(status_code=500,
                          detail="Connection could not be established")
    except InfluxDBError as e:
        logging.error("InfluxDBError: Status={0}, Message={1}"
                      .format(e.response.status, e.message))
        raise MyException(status_code=e.response.status,
                          detail=e.message)
    finally:
        client.close()
    if not df.empty:
        df = df.drop(columns=["result"])
    logging.debug("Total number of records: {}".format(len(df)))

    return df


def list_tagvalues(bucket: str,
                   parameter: Dict) -> DataFrame:
    """
    tag values for a tag key and a measurement
    :param bucket: str, influxdb v2.x bucket
    :param parameter: dict input parameter, see top
    :return: pandas dataframe
    """
    client, query_api = client_open()

    params = {
        "_bucket": bucket,
        "_measurement": parameter.get('measurement'),
        "_tagKey": parameter.get('tagKey')
    }
    query = '''
import "regexp"
import "influxdata/influxdb/schema"
schema.measurementTagValues(
bucket: _bucket,
measurement: _measurement,
tag: _tagKey)
|> rename(fn: (column) => (regexp.replaceAllString(r: /^_/, v:column, t: "")))'''
    # logging.debug("query: {0}\nparameter: {1}".format(query, params))
    logging.debug(query_constructor(query=query, parameter=params))
    try:
        df = query_api.query_data_frame(query=query,
                                        params=params)
    except NewConnectionError:
        logging.error("NewConnectionError encountered")
        raise MyException(status_code=500,
                          detail="Connection could not be established")
    except InfluxDBError as e:
        logging.error("InfluxDBError: Status={0}, Message={1}"
                      .format(e.response.status, e.message))
        raise MyException(status_code=e.response.status,
                          detail=e.message)
    finally:
        client.close()
    if not df.empty:
        df = df.drop(columns=["result"])
    logging.debug("Total number of records: {}".format(len(df)))

    return df


def list_fieldkey(bucket: str,
                  parameter: Dict) -> DataFrame:
    """
    field keys of a measurement
    :param bucket: str, influxdb v2.x bucket
    :param parameter: dict input parameter, see top
    :return: pandas dataframe
    """
    client, query_api = client_open()

    params = {
        "_bucket": bucket,
        "_measurement": parameter.get('measurement')
    }
    query = '''
import "regexp"
import "influxdata/influxdb/schema"
schema.measurementFieldKeys(
bucket: _bucket,
measurement: _measurement)
|> rename(fn: (column) => (regexp.replaceAllString(r: /^_/, v:column, t: "")))'''
    # logging.debug("query: {0}\nparameter: {1}".format(query, params))
    logging.debug(query_constructor(query=query, parameter=params))
    try:
        df = query_api.query_data_frame(query=query,
                                        params=params)
    except NewConnectionError:
        logging.error("NewConnectionError encountered")
        raise MyException(status_code=500,
                          detail="Connection could not be established")
    except InfluxDBError as e:
        logging.error("InfluxDBError: Status={0}, Message={1}"
                      .format(e.response.status, e.message))
        raise MyException(status_code=e.response.status,
                          detail=e.message)
    finally:
        client.close()
    if not df.empty:
        df = df.drop(columns=["result"])
    logging.debug("Total number of records: {}".format(len(df)))

    return df


# this section is just meant to test functionalities in stand-alone
if __name__ == '__main__':
    print(list_measurement(bucket="Housekeeping"))
    print(list_tag(bucket="Housekeeping",
                   parameter={"measurement": "Power.PDU.outlets"}
                   ))
    print(list_tagvalues(bucket="Housekeeping",
                         parameter={"measurement": "Power.PDU.outlets",
                                    "tagKey": "pdu_serial_number"}
                         ))
    print(list_fieldkey(bucket="Housekeeping",
                        parameter={"measurement": "Power.PDU.outlets"}
                        ))
    print(retrieve(bucket="Housekeeping",
                   parameter={"measurement": "Power.PDU.outlets",
                              "tags": {"ip": ["10.10.1.40", "10.10.1.41"],
                                       "name": ["Aruba_16port_ffts_switch", "Rack_HEX"]
                                       },
                              "fieldKey": ["powerFactor", "voltage_V"],
                              "time_from": "2022-05-18T08:49:22.000000Z",
                              "time_to": "2022-05-18T08:50:22.000000Z"
                              }
                   ))
