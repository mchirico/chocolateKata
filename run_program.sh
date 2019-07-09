#!/bin/bash
export PYTHONPATH="${PWD}/src"

cd tests
python ../src/process_orders.py
