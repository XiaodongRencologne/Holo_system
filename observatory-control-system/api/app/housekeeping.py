#!/usr/bin/env python3

from fastapi import HTTPException, Request, APIRouter, status
from fastapi.responses import JSONResponse, PlainTextResponse
from typing import List, Dict, Optional
from pydantic import BaseModel, Field, validator
from datetime import datetime
from pytz import utc
import json
# find flux queries in sub-directory hk
from .hk import fluxquery_client
from .hk.RestAPI_aux import MyException

"""
version history:
2023/02/02 - Ralf A. Timmermann
- version 1.0
"""

router = APIRouter(tags=['Housekeeping'])

responses = {
    200: {
        "content": {"text/csv": {
            "schema": {
                "type": "array",
                "items": {
                    "type": "str"}
            },
            "example": "column1"}},
        "description": "Return a CSV or JSON item"}
}

responses2 = {
    200: {
        "content": {"text/csv": {
            "schema": {
                "type": "array",
                "items": {
                    "type": "str, str, ..."}
            },
            "example": "column1, column2, ..."}},
        "description": "Return a CSV or JSON item"}
}


class Response(BaseModel):
    columns: List
    data: List[List]


class Item(BaseModel):
    measurement: str


class Item1(BaseModel):
    measurement: str
    tagKey: str


class Item2(BaseModel):
    measurement: str
    fieldKey: Optional[List] = Field(description="default = all fields")
    tags: Optional[Dict[str, List]] = Field(description="default = all tags")
    # permuted subsequent two fields to apply the validator also to
    # include "time_to"
    time_to: Optional[datetime] = Field(description="default = now")
    time_from: datetime

    @validator("time_from")
    @classmethod
    def time_validator(cls, v, values, **kwargs):
        time_to = values.get("time_to")
        # if time_to is not provided, assume now
        if time_to is None:
            time_to = datetime.utcnow().replace(tzinfo=utc)
        if v >= time_to:
            raise ValueError(
                "Error: time_from cannot be greater/equal time_to")
        # avoid time ranges > 6 days
        if (time_to - v).days > 6:
            raise ValueError(
                "Error: consider to adopt time intervals < 7 days")

        return v


@router.post("/measurement",
             summary="FYST Housekeeping Data for the Instrumental Teams",
             description="Extracts measured data for provided measurement, tag(s), and field key(s) "
                         "recorded within a period of time. Regarding available measurements, "
                         "tag keys, tag values, and field keys consider calling the other methods.",
             responses={**responses2},
             response_model=Response
             )
async def retrieve(item: Item2,
                   request: Request):
    # print("content of request: \n", request.__dict__)
    try:
        df = fluxquery_client.retrieve(bucket="Housekeeping",
                                       parameter=dict(item))
        if request.headers.get('accept') == "application/json":
            result = df.to_json(date_format='iso',
                                date_unit='us',  # microseconds in influxdb
                                orient='split',
                                index=False)
            return JSONResponse(json.loads(result),
                                status_code=status.HTTP_200_OK)
        elif request.headers.get('accept') == "text/csv":
            result = df.to_csv(index=False)
            return PlainTextResponse(result,
                                     status_code=status.HTTP_200_OK)
        else:
            raise MyException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                              detail="Provide an accept header: 'application/json' | 'text/csv'")
    except Exception as e:
        raise HTTPException(status_code=e.status_code,
                            detail=e.detail)


@router.get("/measurement/list",
            summary="List Measurements of Current Bucket",
            description="List measurements of current bucket",
            responses={**responses},
            response_model=Response
            )
async def list_measurement(request: Request):
    # print("content of request: \n", request.__dict__)
    try:
        df = fluxquery_client.list_measurement(bucket="Housekeeping")
        if request.headers.get('accept') == "application/json":
            result = df.to_json(orient='split',
                                index=False)
            return JSONResponse(json.loads(result),
                                status_code=status.HTTP_200_OK)
        elif request.headers.get('accept') == "text/csv":
            result = df.to_csv(index=False)
            return PlainTextResponse(result,
                                     status_code=status.HTTP_200_OK)
        else:
            raise MyException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                              detail="Provide an accept header: 'application/json' | 'text/csv'")
    except Exception as e:
        raise HTTPException(status_code=e.status_code,
                            detail=e.detail)


@router.post("/measurement/tagKey",
             summary="List Tag Keys for Given Measurement",
             description="List tag keys of current bucket for given measurement",
             responses={**responses},
             response_model=Response
             )
async def list_tag(item: Item,
                   request: Request):
    try:
        df = fluxquery_client.list_tag(bucket="Housekeeping",
                                       parameter=dict(item))
        if request.headers.get('accept') == "application/json":
            result = df.to_json(orient='split',
                                index=False)
            return JSONResponse(json.loads(result),
                                status_code=status.HTTP_200_OK)
        elif request.headers.get('accept') == "text/csv":
            result = df.to_csv(index=False)
            return PlainTextResponse(result,
                                     status_code=status.HTTP_200_OK)
        else:
            raise MyException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                              detail="Provide an accept header: 'application/json' | 'text/csv'")
    except Exception as e:
        raise HTTPException(status_code=e.status_code,
                            detail=e.detail)


@router.post("/measurement/tagValue",
             summary="List Tag Values for Given Measurement and Tag Key",
             description="List tag values for given measurement and tag key",
             responses={**responses},
             response_model=Response
             )
async def list_tagvalues(item: Item1,
                         request: Request):
    try:
        df = fluxquery_client.list_tagvalues(bucket="Housekeeping",
                                             parameter=dict(item))
        if request.headers.get('accept') == "application/json":
            result = df.to_json(orient='split',
                                index=False)
            return JSONResponse(json.loads(result),
                                status_code=status.HTTP_200_OK)
        elif request.headers.get('accept') == "text/csv":
            result = df.to_csv(index=False)
            return PlainTextResponse(result,
                                     status_code=status.HTTP_200_OK)
        else:
            raise MyException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                              detail="Provide an accept header: 'application/json' | 'text/csv'")
    except Exception as e:
        raise HTTPException(status_code=e.status_code,
                            detail=e.detail)


@router.post("/measurement/fieldKey",
             summary="List Field Key for Given Measurement",
             description="List field key for given measurement",
             responses={**responses},
             response_model=Response
             )
async def list_fieldkey(item: Item,
                        request: Request):
    try:
        df = fluxquery_client.list_fieldkey(bucket="Housekeeping",
                                            parameter=dict(item))
        if request.headers.get('accept') == "application/json":
            result = df.to_json(orient='split',
                                index=False)
            return JSONResponse(json.loads(result),
                                status_code=status.HTTP_200_OK)
        elif request.headers.get('accept') == "text/csv":
            result = df.to_csv(index=False)
            return PlainTextResponse(result,
                                     status_code=status.HTTP_200_OK)
        else:
            raise MyException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                              detail="Provide an accept header: 'application/json' | 'text/csv'")
    except Exception as e:
        raise HTTPException(status_code=e.status_code,
                            detail=e.detail)
