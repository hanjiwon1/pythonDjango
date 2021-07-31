#!/bin/sh

VENV_DIR="django_env"

/usr/bin/python3 -m venv $VENV_DIR
source $VENV_DIR/bin/activate

python -m pip --version

pip install --upgrade pip

python -m pip install --force-reinstall -r requirement.txt