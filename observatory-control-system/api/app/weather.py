#!/usr/bin/env python3

import csv
import io
import random
from typing import List

from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

router = APIRouter(tags=['Weather'])

class Weather(BaseModel):
    temp_C: float
    pressure_mbar: float
    windspeed_mps: float

def random_weather():
    t = random.gauss(0.0, 10.0)
    p = random.gauss(0.0, 10.0)
    ws = random.gauss(0.0, 10.0)
    return dict(temp_C=t, pressure_mbar=p, windspeed_mps=ws)

@router.get('/current', response_model=Weather)
async def current_site_weather():
    return random_weather()

class Weathers(BaseModel):
    data: List[Weather]

def write_list_of_dicts_as_csv(f, rows):
    cols = rows[0].keys()
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    for row in rows:
        w.writerow(row)

@router.get('/historical', response_model=Weathers,
    responses={200: {'content': {'text/csv': {}}}} )
async def historical_site_weather(request: Request):
    data = [ random_weather() for i in range(10) ]
    if request.headers['accept'] == 'text/csv':
        stream = io.StringIO()
        write_list_of_dicts_as_csv(stream, data)
        return StreamingResponse(
            iter([stream.getvalue()]), media_type='text/csv')
    return Weathers(data=data)

