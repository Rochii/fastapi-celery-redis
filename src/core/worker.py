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


@celery.task(track_started=True, name="create_validation_task")
def create_validation_task(text: str) -> dict:
    """Create a new validation task.

    Args:
        text (str): Text to analyze.

    Returns:
        dict: Returns all information about the validation in a dictionary.
    """
    logger.info(f"text: {text} msg: creating new validation task!")

    # NOTE: do some stuff and return results

    return {"text": text, "valid": 1}
