#!/bin/bash

USER="Alex"

echo "Дата: $(date)"

echo "Hello $USER"

echo "Скрипт запущен из дириктории: $(pwd)"


echo "Колличество процессов:" 
ps aux | grep -v grep | wc -l

ls -l /etc/passwd | awk "{print $1}"
