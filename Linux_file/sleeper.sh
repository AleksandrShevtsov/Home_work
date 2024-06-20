#!/bin/bash

# Запись даты и количества процессов 10 раз с интервалом в 5 секунд
for i in {1..10}; do
  echo "$(date +'%H:%M:%S') $(ps -ef | wc -l)"
  sleep 5  # Уменьшите значение или закомментируйте эту строку для изменения интервала
done

# Запись информации о процессоре в файл cpu_info.txt
cat /proc/cpuinfo > cpu_info.txt

# Запись информации об операционной системе в файл os_info.txt (только NAME=)
grep "^NAME=" /etc/os-release > os_info.txt

# Запись имени операционной системы без префикса NAME= в файл os_name.txt
grep "^NAME=" /etc/os-release | sed 's/NAME=//' | tr -d '"' > os_name.txt

# Создание 50 файлов с именами от 50.txt до 100.txt
for i in {50..100}; do
  touch "$i.txt"
done
