#!/bin/bash
cd "$(dirname "$0")"

mypy .
python3.5 -m pylint -f parseable -d I0011,R0801,F0401,R0904,W0702,W0512,R0201,E1101,C0325,W0613,W0603,W0602 \
    --rcfile=pylintrc *.py */*.py

