#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse

HTTP_STATUS_CODE_TO_DETAIL = {
    status.HTTP_401_UNAUTHORIZED: "Unauthorized",
    status.HTTP_403_FORBIDDEN: "Forbidden",
    status.HTTP_404_NOT_FOUND: "Not found",
    status.HTTP_405_METHOD_NOT_ALLOWED: "Method not allowed",
    status.HTTP_500_INTERNAL_SERVER_ERROR: "Internal server error",
    status.HTTP_503_SERVICE_UNAVAILABLE: "Service unavailable",
    # NOTE: add more exceptions here
}


def add_exception_handlers(app: FastAPI) -> None:
    """Add all exception handler to the app instance.

    Args:
        app (FastAPI): FastAPI app instance.
    """

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(_: Request, __: RequestValidationError) -> JSONResponse:
        """Customize Pydantic validation exceptions.

        Args:
            _ (Request): API request object.
            __ (RequestValidationError): Pydantic RequestValidationError exception raised.

        Returns:
            JSONResponse: API JSON response.
        """
        return JSONResponse(
            # TODO: add more information about the error?
            content={"detail": "Invalid content"},
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(_: Request, exc: StarletteHTTPException) -> JSONResponse:
        """Customize response when HTTPException raised.

        Args:
            _ (Request): API request object.
            exc (HTTPException): HTTPException raised.

        Returns:
            JSONResponse: API JSON response.
        """
        if exc.status_code in HTTP_STATUS_CODE_TO_DETAIL:
            return JSONResponse(
                content={"detail": HTTP_STATUS_CODE_TO_DETAIL[exc.status_code]},
                status_code=exc.status_code,
            )

        return JSONResponse({"detail": "Unknown error"}, status_code=exc.status_code)
