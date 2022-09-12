#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import APIRouter

from api.config import ROUTE_PREFIX_V1
from api.routers import validations

router = APIRouter()

# include to router all api REST routes with version prefix
router.include_router(validations.router, prefix=ROUTE_PREFIX_V1)

# NOTE: add more API routes here
