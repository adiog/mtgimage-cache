#!/bin/bash

VENV=${1:-venv}

echo "Using virtualenv at `pwd`/$VENV"

if [[ -z "${PYTHON35}" ]]; then
  which python3.5 || echo "Python 3.5 not found" && exit 1
  PYTHON35=`which python3.5`
fi

echo "Using python3.5 from ${PYTHON35}"

if [[ ! -d $VENV ]]; then
  virtualenv -p $PYTHON35 $VENV
fi

. $VENV/bin/activate
pip install -r virtualenv-python3.5.txt

