#  Напишите декоратор validate_args, который будет проверять типы аргументов функции
#  и выводить сообщение об ошибке,
#  если переданы аргументы неправильного типа.
#  Декоратор должен принимать ожидаемые типы аргументов в качестве параметров.


def validate_args(*types):
    def decorator(func):
        def wrapper(*args):
            for arg, expected_type in zip(args, types):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Неправильный тип аргумента: {arg} (ожидался {expected_type})")
            return func(*args)
        return wrapper
    return decorator


@validate_args(int, str)
def greet(age, name):
    print(f"Привет, {name}! Тебе {age} лет.")


# Тесты:
try:
    greet(25, "Анна")  # Ожидаемый вывод: Привет, Анна! Тебе 25 лет.
    greet("25", "Анна")
except TypeError as e:
    print(e)

# Напишите декоратор log_args, который будет записывать аргументы и результаты вызовов
# функции в лог-файл. Каждый вызов функции должен быть записан на новой строке в
# формате "Аргументы: <аргументы>, Результат: <результат>". Используйте модуль logging
# для записи в лог-файл.


import logging
from functools import wraps

logging.basicConfig(filename="log.txt", encoding="utf-8", level=logging.INFO, format="%(message)s")

def log_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Аргументы: {args} Результат: {func(*args, **kwargs)}")
        print(f"Аргументы: {args} Результат: {func(*args, **kwargs)}")
        return func(*args, **kwargs)
    return wrapper

@log_args
def add(a, b):
    return a + b


add(25, 0)
add(26, 20)
add(2, 3)
add(5, 7)