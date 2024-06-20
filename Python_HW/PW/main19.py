# hash_value = hash("hello")
# print(hash_value) # Выводит целочисленное значение хэша
# hash_value = hash("hello")
# print(hash_value) # Выводит целочисленное значение хэша

# s = 'hello'
# print(s.replace('h', ''))
# print(s)

# print(hash(1))
# print(hash(1.0))
# print(hash("1"))
# print(hash((1, )))


# s = {5, 1, 7, 1}
# print(s)

# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# print(set1.intersection(set2)) # Выводит {2, 3}
# print(set1 & set2) # Выводит {2, 3}
# print(set1.union(set2))
# print(set1 | set2)
# print(set1.difference(set2)) # Выводит {1}
# print(set1 - set2) # Выводит {1}
# print(set2.difference(set1))
# print(set2 - set1)
# print(set1.symmetric_difference(set2)) # Выводит {1, 4}
# print(set1 ^ set2) # Выводит {1, 4}

# set1 = {1, 2, 3}
# # print(type(set1))
# # set2 = set()
# # print(type(set2))
# print(2 in set1)
# print({1, 2} in set1)
#
# set2 = {1, 2, (3, )}
#
# my_set = {1, 2, 3}
# print(len(my_set))


# my_set = {1, 2, 3}
# my_set.add(4)
# print(my_set)
# # my_set.remove(4)
# my_set.discard(4)
# print(my_set)
# my_set.discard(4)
# my_set.discard(4)
# my_set.clear()
# print(my_set)

# set1 = {1, 2, 3}
# set2 = {2, 3, 4, 7}
# print(set1 == set2) # Выводит False
# print(set1 < set2) # Выводит False, set1 не является подмножеством set2


# my_set = {1, 2, 3}
# for item in my_set:
#     print(item) # Выводит каждый элемент множества
#
# print({i for i in range(5)})
# print([i for i in range(5)])
# print((i for i in range(5)))


words = ['hello', 'daddy', 'hello', 'mum']
print(set(words))

# Дан массив.
# Дать ответ на вопрос есть ли в нём два элемента с суммой ноль.
# ● Решить с двумя вложенными циклами
# ● Решить с помощью множеств



# Напишите программу, которая принимает два списка и возвращает список, содержащий
# только уникальные элементы из обоих списков.
# Создайте функцию unique_elements, которая принимает два списка в качестве аргументов и
# возвращает список уникальных элементов. Используйте множества для фильтрации
# дубликатов. Выведите результат на экран.
# Примеры списков:
# [1, 2, 3, 4, 5]
# [4, 5, 6, 7, 8]
# Пример вывода:
# Уникальные элементы: [1, 2, 3, 4, 5, 6, 7, 8]


def unique(l1, l2):
    l1.extend(l2)
    return set(l1)

print(unique([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))


