#!/bin/bash

SERVER_IP=${1:"127.0.0.1"}
SERVER_PORT=${2:8001}


python3 ./manage.py runserver SERVER_IP:SERVER_PORT
echo "server is running"