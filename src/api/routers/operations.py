#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback

from celery.result import AsyncResult
from fastapi import APIRouter, HTTPException, Path, status

from api.schemas.operations import (
    CreateOperationsRequest,
    CreateOperationsResponse,
    RetrieveOperationsResponse,
)
from core.worker import create_operation_task
from modules.logger import Logger

# instantiate logger
logger = Logger(__name__, "api.log").get_logger()

# APIRouter creates path operations for validation model
router = APIRouter(
    prefix="/operations",
    tags=["operations"],
    # NOTE: we can add dependencies here, i.e: oauth2 api authentication
    # dependencies=[Depends(...)]
)


# POST /v{major_version}/operations
@router.post("", response_model=CreateOperationsResponse)
async def create_validation(data: CreateOperationsRequest):
    """Create new operation.

    Args:
        data (CreateOperationRequest): Pydantic input validation model.

    Returns:
        CreateOperationResponse: Pydantic response validation model.
    """
    try:
        task = create_operation_task.delay(data.operation, data.text)
        logger.info(f"msg: queued new task with id {task.id} successfully")
        return CreateOperationsResponse.parse_obj({"id": task.id})

    except Exception:
        logger.critical(
            f"msg: error during creation caused by exception -> {traceback.format_exc()}"
        )
        return HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)


# GET /v{major_version}/operations/{id}
@router.get("/{id}")
async def retrieve_operation(
    id: str = Path(
        default=...,
        regex=r"^[a-z0-9]{8}\-[a-z0-9]{4}\-[a-z0-9]{4}\-[a-z0-9]{4}\-[a-z0-9]{12}$",
    )
):
    """Retrieve operation results for an specific id.

    Args:
        id (str): Validation identifier.

    Returns:
        RetrieveOperationsResponse: Pydantic processed response operation model.
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

        return RetrieveOperationsResponse.parse_obj(
            {
                "id": id,
                "operation": task_results["operation"],
                "text": task_results["text"],
                "valid": task_results["valid"],
            }
        )

    except Exception:
        logger.critical(
            f"id: {id} msg: error during retrieval caused by exception -> {traceback.format_exc()}"
        )
        return HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
