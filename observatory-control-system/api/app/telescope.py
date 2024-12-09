#!/usr/bin/env python3

from datetime import datetime, timedelta
from enum import Enum
from typing import Literal
from urllib.parse import urljoin

from fastapi import APIRouter
from httpx import AsyncClient
from pydantic import BaseModel, Field, conlist
import pydantic

from . import acu_types

router = APIRouter(tags=['Telescope'])
client = AsyncClient()

def tcs_url(path):
    return urljoin("http://tcs:5600", path)


# status

def create_telescope_status_class():
    new_fields = { 'timestamp':(int, ...) }
    old_fields = { k:(v.annotation,...) for k,v in acu_types.StatusGeneral8100.model_fields.items() }
    for name in ['Time', 'Year']:
        del old_fields[name]
    return pydantic.create_model('TelescopeStatus', **new_fields, **old_fields)

# strip off the aliases
TelescopeStatus = create_telescope_status_class()

def acu_dataset_time_to_timestampns(year, doy):
    t = datetime(year,1,1) + timedelta(days=doy-1)
    return int(t.timestamp() * 1e9)

@router.get('/status', response_model=TelescopeStatus)
async def telescope_status():
    response = await client.get(tcs_url("/acu/status"))
    data = acu_types.StatusGeneral8100.parse_raw(response.content).dict()
    data['timestamp'] = acu_dataset_time_to_timestampns(data['Year'], data['Time'])
    return TelescopeStatus(**data)

@router.get('/acu/status', response_model=acu_types.StatusGeneral8100)
async def raw_ACU_status():
    "Raw status from the ACU"
    response = await client.get(tcs_url("/acu/status"))
    return response.json()


# commands

class CommandStatus(str, Enum):
    ok = "ok"
    error = "error"

class CommandResponse(BaseModel):
    status: CommandStatus
    message: str | None = None

def command(func, *args, **kwargs):
    return router.post(func, *args, response_model=CommandResponse, response_model_exclude_unset=True, **kwargs)

class MoveToParameters(BaseModel):
    azimuth: float
    elevation: float

@command('/move-to')
async def move_to_new_position(param: MoveToParameters):
    response = await client.post(tcs_url("/move-to"), json=param.dict())
    return response.json()

class AzimuthScanParameters(BaseModel):
    azimuth_range: conlist(float, min_length=2, max_length=2)
    elevation: float
    num_scans: int
    start_time: float
    turnaround_time: float
    speed: float

@command('/azimuth-scan')
async def scan_in_azimuth(param: AzimuthScanParameters):
    response = await client.post(tcs_url("/azimuth-scan"), json=param.dict())
    return response.json()

@command('/abort')
async def abort():
    response = await client.post(tcs_url("/abort"))
    return response.json()

class PathParameters(BaseModel):
    start_time: float
    coordsys: Literal["Horizon","ICRS"]
    points: list[conlist(float, min_length=5, max_length=5)]

@command('/path')
async def path(param: PathParameters):
    response = await client.post(tcs_url("/path"), json=param.dict())
    return response.json()

class PositionBroadcastParameters(BaseModel):
    destination_host: str
    destination_port: int

@command('/acu/position-broadcast')
async def acu_position_broadcast(param: PositionBroadcastParameters):
    response = await client.post(tcs_url("/acu/position-broadcast"), json=param.dict())
    return response.json()
