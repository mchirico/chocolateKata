#!/bin/bash
export PYTHONPATH="${PWD}/src"
pycodestyle --show-source --show-pep8 src/*.py
pycodestyle --show-source --show-pep8 tests/*.py
pycodestyle --show-source --show-pep8 src/utils/*.py

cd tests
pytest --cov=../ -v *.py
