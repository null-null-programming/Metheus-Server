.DEFAULT_GOAL := help
.PHONY: lint format test prepare help

lint:  ## Lint and Static-type-check
	mypy app tests
	flake8 app tests

format:  ## Format Code
	black app tests
	isort app tests

test:  ## Run tests
	pytest -v tests --cov=app --cov-report=html --cov-report=xml --junitxml=junit/test-results.xml

# いつかコードカバレッジまでチェックするようにしたい
# coverage:  ## Run tests with coverage
# 	coverage erase
# 	coverage run --include=podsearch/* -m pytest -ra
# 	coverage report -m

prepare:  ## Excecute before commits
	make lint
	make format
	make test

help:  ## Print this help
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)