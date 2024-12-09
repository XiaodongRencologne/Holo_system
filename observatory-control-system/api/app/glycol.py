#!/usr/bin/env python3

from fastapi import APIRouter

router = APIRouter(tags=['Glycol'])

@router.get('/status')
async def status():
    "Glycol status"
    return {'status': 'ok'}

