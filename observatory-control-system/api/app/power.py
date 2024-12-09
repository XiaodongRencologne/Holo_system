#!/usr/bin/env python3

from fastapi import APIRouter

router = APIRouter(tags=['Power'])

@router.get('/status')
async def status():
    "Some documentation"
    return {'status': 'ok'}

