# Задаание 1

# Напишите программу, которая запрашивает у пользователя целое число и определяет,
# является ли оно палиндромом. Число является палиндромом, если оно читается
# одинаково слева направо и справа налево. Выведите соответствующее сообщение на
# экран с помощью команды print. Используйте математические операции. Работу со
# строками использовать нельзя

n = int(input('Введите целое число:'))
temp_num, part_num = n, 0
new_n = 0
while temp_num > 0:
    part_num = temp_num % 10
    temp_num //= 10
    new_n = (new_n + part_num) * 10
if n == (new_n / 10):
    print(f'Это {n} полиндром')
else:
    print(f'Это {n} не полиндром')

# Задание 2

# Напишите программу, которая запрашивает у пользователя целое число и проверяет,
# является ли оно числом Армстронга. Число Армстронга - это число, которое равно сумме
# своих цифр, возведенных в степень, равную количеству цифр в числе


n = int(input('Введите число:'))
part_n, temp_n, i = 0, n, 0
new_n = 0
while temp_n > 0:
    part_n = temp_n % 10
    temp_n //= 10
    i += 1
j = i
temp_n = n
while j > 0:
    part_n = temp_n % 10
    new_n += part_n ** i
    temp_n //= 10
    j -= 1
if n == new_n:
    print(f'Число {n} является числом Армстронга.')
else:
    print(f'Число {n} не является числом Армстронга.')

