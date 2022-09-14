.PHONY: help \
		format format-isort format-black \
		lint lint-flake8 lint-pylint lint-bandit lint-safety \
		test test-unitary test-functional test-integration \
		build clean up

POETRY_CMD:=poetry run
DOCKER_COMPOSE_CMD=sudo docker-compose -f docker-compose.yml
DOCKER_CMD=sudo docker exec api
PYMODULE:=src
TESTS:=tests

# Help
help:
	@echo "Please use 'make <target>', where <target> is one of"
	@echo ""
	@echo "  format             run all code formatters (isort, black)"
	@echo "  format-isort       run python import for library sorting"
	@echo "  format-black       run python code formatter according PEP8"
	@echo "  lint               run all linters (flake8, pylint, bandit, safety)"
	@echo "  lint-flake8        run linter to check coying style according PEP8"
	@echo "  lint-pylint        run lint to check code quality"
	@echo "  lint-bandit        run linter to detect security issues in python code"
	@echo "  lint-safety        run linter to detect python dependency vulnerabilities"
	@echo "  test               run all tests (unitary, functional, integration)"
	@echo "  test-unitary       run unitary testing inside the container"
	@echo "  test-functional    run functional testing inside the container"
	@echo "  test-integration   run integration testing inside the container"
	@echo "  build              build docker container images"
	@echo "  clean              remove docker containers and networks" 
	@echo "  up                 start docker containers in detached mode"
	@echo ""
	@echo "Check the Makefile to know exactly what each target is doing."
	@echo "Most actions are configured in 'pyproject.toml'."


# Formatter jobs
format:
	$(MAKE) format-isort format-black

format-isort:
	$(POETRY_CMD) isort $(PYMODULE) $(TESTS)

format-black:
	$(POETRY_CMD) black $(PYMODULE) $(TESTS)


# Linter jobs
lint:
	$(MAKE) lint-flake8 lint-pylint lint-bandit lint-safety

lint-flake8:
	$(POETRY_CMD) flake8 $(PYMODULE) $(TESTS)

lint-pylint:
	$(POETRY_CMD) pylint $(PYMODULE) $(TESTS)

lint-bandit:
	$(POETRY_CMD) bandit $(PYMODULE) $(TESTS)

lint-safety:
	$(POETRY_CMD) safety check


# Test jobs
test:
	$(MAKE) test-unitary test-functional test-integration

test-unitary:
	$(DOCKER_CMD) $(POETRY_CMD) pytest --cov=$(PYMODULE) $(TESTS)/unitary

test-functional:
	$(DOCKER_CMD) $(POETRY_CMD) pytest $(TESTS)/functional

test-integration:
	$(DOCKER_CMD) $(POETRY_CMD) pytest $(TESTS)/integration

# Docker jobs
build:
	$(DOCKER_COMPOSE_CMD) build

clean:
	$(DOCKER_COMPOSE_CMD) rm -fs

up:
	$(DOCKER_COMPOSE_CMD) up -d api core redis
