# Напишите программу, которая принимает в качестве аргумента командной строки путь к файлу .py и запускает его.
# При запуске файла программа должна выводить сообщение "Файл <имя файла> успешно запущен".
# Если файл не существует или не может быть запущен, программа должна вывести соответствующее сообщение об ошибке.

import runpy


def run_python_file(file_path):
    try:
        runpy.run_path(file_path)
        return print(f'Файл {os.path.basename(__file__)} успешно запущен')
    except FileNotFoundError:
        print('Файл не существует')
    except Exception:
        print(f"Файл {file_path} не может быть запущен ")
        return False


file_path = input('Введите путь к файлу .py: ')
run_python_file(file_path)

# Вариант 2

import sys

file_path = sys.argv[1]
try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Файл не найден. Проверьте путь.")
except Exception as e:
    print(f"Произошла ошибка: {e}")

# 2. Напишите программу, которая принимает в качестве аргумента командной строки путь к директории
# и выводит список всех файлов и поддиректорий внутри этой директории.
# Для этой задачи используйте модуль os и его функцию walk.
# Программа должна выводить полный путь к каждому файлу и директории.

import os.path
import sys

file_path = sys.argv[1]
for dirpath, dirnames, filenames in os.walk(file_path):
    for filename in filenames:
        print(os.path.join(dirpath, filename))

