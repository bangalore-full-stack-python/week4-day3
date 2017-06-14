#!/usr/bin/env bash

rm -f info.db
python3 schema.py
python3 controller.py

rm -rf __pycache__
