#!/usr/bin/env bash

set -ex

# static type check
#mypy app

# linter
flake8 app tests

# formatter
black app tests --check
isort app tests --check-only

# test with pytest
PYTHONPATH=./app
# pytest --cov=app --cov=tests --cov-report=term-missing --cov-report=xml tests
pytest -v tests --cov=app --cov-report=html --cov-report=xml --junitxml=junit/test-results.xml
