#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pydantic import BaseModel


# create validation responses
class CreateOperationsRequest(BaseModel):
    operation: str
    text: str
    # NOTE: add more attributes here
    pass


class CreateOperationsResponse(BaseModel):
    id: str
    # NOTE: add more attributes here
    pass


# read validation responses
class RetrieveOperationsResponse(BaseModel):
    id: str
    operation: str
    text: str
    valid: int
    # NOTE: add more attributes here
    pass
