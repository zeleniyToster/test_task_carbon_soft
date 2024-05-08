#!/bin/bash

DEFAULT_IP=127.0.0.1
DEFAULT_PORT=8001
SERVER_IP="${1:-$DEFAULT_IP}"
SERVER_PORT="${2:-$DEFAULT_PORT}"

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 ./manage.py migrate
python3 ./manage.py runserver $SERVER_IP:$SERVER_PORT