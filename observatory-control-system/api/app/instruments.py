#!/usr/bin/env python3

from fastapi import APIRouter

router = APIRouter(tags=['Instruments'])

@router.get('/status')
async def status():
    "Some documentation"
    return {'status': 'ok'}

