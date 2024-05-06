# test_task_carbon_soft

Запуск клиента на линуксе:
1) Перейдите в папку со скриптом `cpu_utilization_script.sh`;
2) Перед началом, убедитесь, что у скрипта `cpu_utilization_script.sh` активен флаг "executable". Если же нет, то активруйте его;
3) Выполните команду `nohup ./cpu_utilization_script.sh &`;
4) Не закрывайте консоль.



Запуск сервера.
С помощью скрипта `run_server.sh`:
1) Установите Python 3.10.4. Также проверял на 3.10.12, на остальных версиях работоспособность не гарантируется;
2) Убедитесь что установлен `python3-venv`, если нет - установите;
3) Выставить скрипту `run_server.sh` флаг на запуск(`x`);
4) Выполните скрипт `run_server.sh` для запуска сервера со стандартными параметрами;
5) Также скрипт с принимает два параметра SERVER_IP - ip адресс сервера и SERVER_PORT - port сервера. `run_server.sh SERVER_IP SERVER_PORT`

Вручную
1) Установите Python 3.10.4. Также проверял на 3.10.12, на остальных версиях работоспособность не гарантируется;
2) Убедитесь что установлен `python3-venv`, если нет - установите;
3) На основе вышеуказанной версии Python, в папке server, создайте виртуальное окружение командой `python3 -m venv venv`;
4) Активируйте виртуальное окружение командой `source venv/bin/activate`;
5) Установите зависимости из файла requirements.txt. `pip3 install -r requirements.txt`;
6) Из папки `server/cpu_checker` запустите сервер командой `python3 ./manage.py runserver`;
7) Или запустите сервер на нужном ip и port `python3 ./manage.py runserver SERVER_IP:SERVER_PORT`, где SERVER_IP - ip адресс сервера, SERVER_PORT - порт сервера.
