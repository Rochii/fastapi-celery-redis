#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers import api
from api.routers.handlers.exceptions import add_exception_handlers

# create FastAPI object
app = FastAPI()

# include resource api routers
app.include_router(api.router)

# add exception handlers
add_exception_handlers(app)

# allow CORS middleware
app.add_middleware(
    CORSMiddleware,
    # NOTE: we can configure allowed hosts
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
