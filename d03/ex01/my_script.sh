#!/bin/sh

PATH_URL="https://github.com/jaraco/path.git"

python3 -m venv ./local_lib
source ./local_lib/bin/activate

python3 -m pip --version

python3 -m pip install --upgrade pip --target=local_lib --force-reinstall git+$PATH_URL --log install_path.log

python3 my_program.py