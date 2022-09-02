.PHONY: help \
		check-bandit check-black check-flake8 check-mypy check-safety \
	    test test-cov \
	    build clean up

CMD:=poetry run
DOCKER_COMPOSE_CMD=sudo docker-compose -f docker-compose.yml
PYMODULE:=src
TESTS:=tests

# Help
help:
	@echo "Please use 'make <target>', where <target> is one of"
	@echo ""
	@echo "  check-bandit	run lint to detect security issues in python code"
	@echo "  check-black	run python code formatter"
	@echo "  check-flake8	run lint to check codying style (PEP8)"
	@echo "  check-mypy		run lint to check python code types"
	@echo "  check-safety	run lint to detect python dependencies vulnerabilities"
	@echo "  test			"
	@echo "  test-cov		"
	@echo "  build     		build docker compose images"
	@echo "  clean        	remove docker compose container images and networks"
	@echo "  up        		start docker compose images in detached mode"
	@echo ""
	@echo "Check the Makefile to know exactly what each target is doing."
	@echo "Most actions are configured in 'pyproject.toml'."

# Quality jobs
check-bandit:
	$(CMD) bandit $(PYMODULE) $(TESTS)

check-black:
	$(CMD) black $(PYMODULE) $(TESTS)

check-flake8:
	$(CMD) flake8 $(PYMODULE) $(TESTS)

check-mypy:
	$(CMD) mypy $(PYMODULE) $(TESTS)

check-safety:
	$(CMD) safety check


# Test jobs
test:
	$(CMD) pytest --cov=$(PYMODULE) $(TESTS)

test-cov:
	$(CMD) pytest --cov=$(PYMODULE) $(TESTS) --cov-report html


# Docker jobs
build:
	$(DOCKER_COMPOSE_CMD) build

clean:
	$(DOCKER_COMPOSE_CMD) rm -fs

up:
	$(DOCKER_COMPOSE_CMD) up -d api core redis
