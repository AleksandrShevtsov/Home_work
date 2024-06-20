# count = 0
# while count < 5:
#  print(count)
#  count += 1

# count = 0
# while count < 10:
#  if count == 5:
#      break
#  print(count)
#  count += 1
# print('------')
# count = 0
# while count < 10:
#     count += 1
#     if count == 3:
#         continue
#     print(count)

# count = 0
# while count < 5:
#     count += 1
#     continue
#     print(count)
# else:
#     print("Цикл завершен")
#
# a = True
# while a:
#     a = False


# while True:
#     user_input = input("Введите число: ")
#     if user_input == "exit":
#         break
#     elif not user_input.isdigit():
#         continue
#     print(int(user_input) * 2)

# if True:
#     pass
# print()

# import time
# start_time = time.time()
# print(start_time)
# time.sleep(3)
# # выполняемые действия
# end_time = time.time()
# print(end_time)
# execution_time = end_time - start_time
# print("Время выполнения программы:", execution_time, "секунд")

# import random #подключаем модуль псевдослучайных функций Python
# myplaylist = ["Pink Floyd", "Santana", "The Beatles", "ELO", "Mark Knopfler", "KennyG", "Bob Dylan"] #описание плей-листа
# print(myplaylist)
# random.shuffle(myplaylist) #перемешиваем список
# print(myplaylist) #вывод результата на экран
#
# print(random.randint(1, 10))

# import random
# members = ["Василий", "Евгений", "Олег", "София", "Инна", "Василиса", "Петр"]
# print(random.choice(members))


# Для трехзначных чисел оставить только те, сумма цифр в которых равна 15.
# Для четных выводить дополнительно последнюю цифру.
# Для оканчивающихся на ноль печатать строку zero.
# Попробовать решить сначала без break/continue, потом избегая вложенных условий.
# 329
# while True:
#     num = int(input())
#     if num == 0:
#         break
#     if 99 < num < 1000:
#         ones = num % 10
#         tens = num // 10 % 10
#         hund = num // 100
#         sum = ones + tens + hund
#         if sum == 15:
#             print(num)
#         if num % 2 == 0:
#             print(num, ones)
#         if ones == 0:
#             print('zero')

# 2. Напишите программу, которая запрашивает у пользователя положительное целое число и
# вычисляет его факториал.
# Факториал числа N вычисляется как произведение всех целых чисел от 1 до N.
# Используйте цикл с предусловием while для решения задачи.
# Выведите результат на экран с помощью команды print.

# num = int(input("Введите положительное число:"))
# fact = 1
# i = 0
# while i < num:
#     i += 1
#     if num <= 0:
#         num = int(input("Число введено неверно. Введите положительное число:"))
#         continue
#     fact *= i
# print(fact)


# Напишите программу, которая запрашивает у пользователя вещественное число и выводит его
# представление в памяти компьютера. Вещественные числа в памяти компьютера
# представлены с использованием формата с плавающей запятой. Используйте стандартные
# функции языка Python для получения представления числа в бинарном виде и вывода его на
# экран.

print(bin(5))
num = float(input("Введите число:"))
int_num = int(num)
part_num = num - int_num
int_num_str = ''
while True:
    int_num_str = str(int_num % 2) + int_num_str




