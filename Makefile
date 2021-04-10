.DEFAULT_GOAL := help
.PHONY: type lint format test prepare help

type:  ## Static type check with mypy
	mypy app

lint:  ## Lint with flake8
	flake8 app tests

format:  ## Format code with black, isort
	black app tests
	isort app tests

test:  ## Run tests with pytest
	pytest -v tests --cov=app --cov-report=html --cov-report=xml --junitxml=junit/test-results.xml

# いつかコードカバレッジまでチェックするようにしたい
# coverage:  ## Run tests with coverage
# 	coverage erase
# 	coverage run --include=podsearch/* -m pytest -ra
# 	coverage report -m

prepare:  ## Excecute before commits
	make type
	make lint
	make format
	make test

help:  ## Print this help
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)