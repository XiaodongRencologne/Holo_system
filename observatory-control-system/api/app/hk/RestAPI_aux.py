"""
auxiliary routines
"""
import datetime
import json
import os
from typing import Dict


class MyException(Exception):
    def __init__(self, status_code, detail):
        super(MyException, self).__init__(status_code, detail)
        self.status_code = status_code
        self.detail = detail


def get_secret(key: str, default: str) -> str:
    value = os.getenv(key, default)
    if os.path.isfile(value):
        with open(value) as f:
            return f.read().strip()
    return value


def query_constructor(query: str, parameter: Dict) -> str:
    for word, initial in parameter.items():
        if isinstance(initial, datetime.datetime):
            initial = initial.isoformat('T')
        else:
            initial = json.dumps(initial)
        query = query.replace(word, initial)
    return query
