#!/usr/bin/env python3

from fastapi import FastAPI
import os

# Fast API root path:
ROOT_PATH = os.getenv("ROOT_PATH", "/api/v1")

description = """
Note that you'll need to add a few options to the curl commands:
    curl --cacert tls/server.cert.pem \\
         --cert   tls/client.cert.pem \\
         --key    tls/client.key.pem  \\
         ...
"""

app = FastAPI(
    description=description,
    root_path=ROOT_PATH,
    title='FYST API',
)

from . import events
from . import glycol
from . import power
from . import telescope
from . import weather
from . import housekeeping

app.include_router(telescope.router, prefix='/telescope')
app.include_router(weather.router, prefix='/weather')
app.include_router(glycol.router, prefix='/glycol')
#api.include_router(instruments.router, prefix='/instruments')
app.include_router(power.router, prefix='/power')
app.include_router(events.router, prefix='/events')
app.include_router(housekeeping.router, prefix='/housekeeping')
