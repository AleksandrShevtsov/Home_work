# Напишите программу, которая принимает два числа и возвращает их сумму и произведение
# в виде кортежа (sum, product). Используйте функцию для вычисления суммы и
# произведения. Выведите результат на экран с помощью команды print.
# Пример вывода:
# Введите первое число: 3
# Введите второе число: 4
# Сумма и произведение чисел: (7, 12)


def sum_and_prod(number1, number2):
	summa = number1 + number2
	prod = number1 * number2
	return summa, prod


num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число:'))
print(f'Сумма и произведение чисел: {sum_and_prod(num1, num2)}')

# Напишите программу, которая принимает список чисел и возвращает сумму, минимальное и
# максимальное значение из списка. Используйте функцию для обработки списка чисел и
# возврата трех значений. Выведите результат на экран с помощью команды print.
#
#
def sum_max_min(list_n):
	res = 0
	for i in range(len(list_n)):
		res += int(list_n[i])
	return res, min(list_n), max(list_n)


list_num = input('Введите элементы первого списка, разделенные пробелом:')
list_num = list_num.split(' ')
value1, value2, value3 = sum_max_min(list_num)
print(f'Сумма чисел: {value1}')
print(f'Минимальное значение: {value2}')
print(f'Минимальное значение: {value3}')