#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import getenv
from celery import Celery

from modules.logger import Logger


# instantiate logger
logger = Logger(__name__, "worker.log").get_logger()

# create celery object
celery = Celery(
    __name__,
    broker=getenv("CELERY_BROKER_URL", "redis://redis:6379/0"),
    backend=getenv("CELERY_RESULT_BACKEND", "redis://redis:6379/0"),
)


@celery.task(track_started=True, name="create_operation_task")
def create_operation_task(operation: str, text: str) -> dict:
    """Create a new operation task.

    Args:
        operation (str): Operation to perform.
        text (str): Text to analyze.

    Returns:
        dict: Returns all information about the operation in a dictionary.
    """
    logger.info(
        f"data: {operation} msg: creating new operation task!"
    )
    
    # NOTE: do some stuff and return results

    return {"operation": operation, "text": text, "valid": 1 }
