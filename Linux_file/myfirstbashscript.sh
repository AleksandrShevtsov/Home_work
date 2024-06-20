!#/bin/bash

USER="Alex"

echo "Дата: $(date)"

echo "Hello $USER"

echo "Скрипт запущен из дириктории: $(pwd)"

bioset_count=$(ps aux | grep -v grep | wc -l)

echo "Колличество процессов: $(bioset_count)"

ls -l /etc/password | awk "{print=%1}"
