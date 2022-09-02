# pull official python3.10 image
FROM python:3.10-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.1.15

# install system dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir poetry==$POETRY_VERSION

# set working directory
WORKDIR /usr/src/app

# install application requirements and code
COPY poetry.lock pyproject.toml ./
COPY src/ src/

# project initialization
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

