#!/bin/bash

set -xe

# Using local python virtual environment instead of globally installing
python -m venv .venv
source .venv/bin/activate
python -m pip install pygame numpy chess-board
