#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pydantic import BaseModel


# create validation responses
class CreateValidationRequest(BaseModel):
    text: str
    # NOTE: add more attributes here
    pass


class CreateValidationResponse(BaseModel):
    id: str
    # NOTE: add more attributes here
    pass


# read validation responses
class RetrieveValidationResponse(BaseModel):
    id: str
    text: str
    valid: int
    # NOTE: add more attributes here
    pass
