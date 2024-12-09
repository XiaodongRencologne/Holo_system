#!/usr/bin/env python3

from fastapi import APIRouter

router = APIRouter(tags=['Events'])

description = 'Event interface'

@router.get('/')
async def recent_events():
    "Some documentation"
    return {'status': 'ok'}

@router.get('/callbacks')
async def list_callbacks():
    return {'status': 'ok'}

@router.post('/callbacks')
async def new_callback():
    return {'status': 'ok'}

@router.delete('/callbacks/{callback_id}')
async def delete_callback(callback_id):
    return {'status': 'ok'}

