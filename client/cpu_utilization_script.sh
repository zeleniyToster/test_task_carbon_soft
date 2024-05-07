#!/bin/bash

DEFAULT_IP=127.0.0.1
DEFAULT_PORT=8001
# IP и порт сервера, куда отправлять данные
SERVER_IP="${1:-$DEFAULT_IP}"
SERVER_PORT="${2:-$DEFAULT_PORT}"

while true; do
    # Получить текущую утилизацию CPU (%)
    CPU_UTILIZATION=$[100-$(vmstat 1 2|tail -1|awk '{print $15}')]

    # Отправить данные на сервер
    curl -X POST -d "cpu_utilization=$CPU_UTILIZATION" "http://$SERVER_IP:$SERVER_PORT/cpu/"

    # Подождать 10 секунд перед следующей отправкой
    sleep 10
done
