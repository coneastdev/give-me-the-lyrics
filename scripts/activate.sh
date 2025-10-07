#!/usr/bin/env bash

python -m venv .venv
chmod +x .venv/bin/activate
source .venv/bin/activate
pip install beautifulsoup4 requests customtkinter