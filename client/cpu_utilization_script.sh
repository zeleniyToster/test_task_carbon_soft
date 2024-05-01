#!/bin/bash

# IP и порт сервера, куда отправлять данные
#SERVER_IP="127.0.0.1"
#SERVER_PORT="$1"

while true; do
    # Получить текущую утилизацию CPU (%)
    CPU_UTILIZATION=$[100-$(vmstat 1 2|tail -1|awk '{print $15}')]
    echo "CPU_UTILIZATION" $CPU_UTILIZATION

    # Отправить данные на сервер
    #curl -X POST -d "cpu_utilization=$CPU_UTILIZATION" "http://$SERVER_IP:$SERVER_PORT/"

    # Подождать 10 секунд перед следующей отправкой
    sleep 10
done
