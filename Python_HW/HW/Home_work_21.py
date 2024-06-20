# 1. Напишите программу, которая подсчитывает количество вхождений каждого слова в
# тексте и выводит на экран наиболее часто встречающиеся слова. Для решения задачи
# используйте класс Counter из модуля collections. Создайте функцию count_words, которая
# принимает текст в качестве аргумента и возвращает словарь с количеством вхождений
# каждого слова. Выведите наиболее часто встречающиеся слова и их количество.

from collections import Counter


def count_words(in_list):
    return Counter(in_list)


MY_LIST = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est.'
counter = count_words(MY_LIST.lower().replace(',', '').replace('.', '').split())
for key, values in counter.most_common():
    print(f'{key}: {values}')


# Напишите программу, которая создает именованный кортеж Person для хранения
# информации о человеке, включающий поля name, age и city. Создайте список объектов
# Person и выведите информацию о каждом человеке на экран.
#
# Пример вывода:
# Name: Alice, Age: 25, City: New York
# Name: Bob, Age: 30, City: London
# Name: Carol, Age: 35, City: Paris

from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'city'])

persons = [
    Person('Alice', 25, 'New York'),
    Person('Bob', 30, 'London'),
    Person('Carol', 35, 'Paris')
]
for person in persons:
    print(f"Name: {person.name}, Age: {person.age}, City: {person.city}")


# Напишите программу, которая принимает словарь от пользователя и ключ, и возвращает
# значение для указанного ключа с использованием метода get или setdefault. Создайте
# функцию get_value_from_dict, которая принимает словарь и ключ в качестве аргументов, и
# возвращает значение для указанного ключа, используя метод get или setdefault в
# зависимости от выбранного варианта. Выведите полученное значение на экран.
# Пример словаря:
# my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}
# Пример вывода:
# Введите ключ для поиска: banana
# Использовать метод get (y/n)? y
# Значение для ключа 'banana': 6

def get_value_from_dict(my_dict, key):
    global use_metod
    if use_metod == 'y':
        value = my_dict.get(key)
    elif use_metod == 'n':
        value = my_dict.setdefault(key, 'Не найдено')
    else:
        print('Неверный ввод')
    
    return value


user_dict = {'apple': 5, 'banana': 6, 'cherry': 7}
key = input('Введите ключ для поиска: ')
use_metod = input('Использовать метод get (y/n)? ')
get_value_from_dict(user_dict, key)
print(f'Значение для ключа {key}: {get_value_from_dict(user_dict, key)}')
