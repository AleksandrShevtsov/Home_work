# Напишите программу, которая запрашивает у пользователя число N и выводит на экран
# таблицу умножения от 1 до N. Используйте вложенный цикл for для создания таблицы
# умножения. Выведите результат на экран с помощью команды print и f-строк или метода
# format().
n = int(input('Введите число N: '))
print('Таблица умножения:')
for i in range(1, n + 1):
	for j in range(1, n + 1):
		print(f'{str(j * i).center(2)} ', end=' ')
	print()

# # Напишите программу, которая принимает два списка одинаковой длины и создает новый
# # список, содержащий пары элементов из исходных списков. Используйте функцию zip() для
# # создания пар элементов. Выведите результат на экран с помощью команды print.

list1 = (input('Введите элементы первого списка, разделенные пробелом:')).split(' ')
list2 = (input('Введите элементы второго списка, разделенные пробелом:')).split(' ')
print(f'Список пар элементов: ', end='')
for list1, list2 in zip(list1, list2):
	print(list1, list2, end='')
