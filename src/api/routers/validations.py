#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback

from celery.result import AsyncResult
from fastapi import APIRouter, HTTPException, Path, status

from api.schemas.validations import (
    CreateValidationRequest,
    CreateValidationResponse,
    RetrieveValidationResponse,
)
from core.worker import create_validation_task
from modules.logger import Logger

# instantiate logger
logger = Logger(__name__, "api.log").get_logger()

# APIRouter creates path validations for validation model
router = APIRouter(
    prefix="/validation",
    tags=["validation"],
    # NOTE: we can add dependencies here, i.e: oauth2 api authentication
    # dependencies=[Depends(...)]
)


# POST /v{major_version}/validations
@router.post("", response_model=CreateValidationResponse)
async def create_validation(data: CreateValidationRequest):
    """Create new validation.

    Args:
        data (CreateValidationRequest): Pydantic input validation model.

    Returns:
        ValidationResponse: Pydantic response validation model.
    """
    try:
        task = create_validation_task.delay(data.text)
        logger.info(f"msg: queued new task with id {task.id} successfully")
        return CreateValidationResponse.parse_obj({"id": task.id})

    except Exception:
        logger.critical(
            f"msg: error during creation caused by exception -> {traceback.format_exc()}"
        )
        return HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)


# GET /v{major_version}/validations/{id}
@router.get("/{id}")
async def retrieve_validation(
    id: str = Path(
        default=...,
        regex=r"^[a-z0-9]{8}\-[a-z0-9]{4}\-[a-z0-9]{4}\-[a-z0-9]{4}\-[a-z0-9]{12}$",
    )
):
    """Retrieve validation results for an specific id.

    Args:
        id (str): Validation identifier.

    Returns:
        RetrieveValidationResponse: Pydantic processed response validation model.
    """
    try:
        async_result = AsyncResult(id)
        if not isinstance(async_result, AsyncResult):
            logger.error(f"id: {id} msg: task id not found -> {async_result}")
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        logger.info(
            f"id: {id} task_result.status: {async_result.status} type: {async_result.status}"
        )

        # NOTE:
        #   here some checks about the status of celery worker can be added because task may not
        #   be finished and we want to return another response can be returned

        # get method must be called to ensure resources are released
        task_results = async_result.get()

        return RetrieveValidationResponse.parse_obj(
            {
                "id": id,
                "text": task_results["text"],
                "valid": task_results["valid"],
            }
        )

    except Exception:
        logger.critical(
            f"id: {id} msg: error during retrieval caused by exception -> {traceback.format_exc()}"
        )
        return HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
