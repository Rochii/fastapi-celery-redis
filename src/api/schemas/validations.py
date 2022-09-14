#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pydantic import BaseModel


# create validation responses
class CreateValidationRequest(BaseModel):
    text: str
    # NOTE: add more attributes here


class CreateValidationResponse(BaseModel):
    id: str
    # NOTE: add more attributes here


# read validation responses
class RetrieveValidationResponse(BaseModel):
    id: str
    text: str
    valid: int
    # NOTE: add more attributes here
