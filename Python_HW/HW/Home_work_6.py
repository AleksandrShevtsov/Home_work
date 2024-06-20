# # Задание 1
#
# import random
#
# in_num = int(input('Введите число от 1 до 100:'))
# rand_num = random.randint(1, 100)
# while in_num != rand_num:
#     if in_num > rand_num:
#         print('Загаданное число меньше.')
#         in_num = int(input('Попробуйте снова:'))
#     else:
#         print('Загаданное число больше.')
#         in_num = int(input('Попробуйте снова:'))
# else:
#     print('Поздравляю! Вы угадали число ' + str(in_num) + '!')
#
# # Задание 2
#
#
# in_num = int(input('Введите число:'))
# count = 0
# f_n1 = 0
# f_n2 = 1
# while count < in_num:
#     print(f_n1, end=', ')
#     f_n2, f_n1 = f_n1, f_n1 + f_n2
#     count += 1


# Задание 3

in_num = int(input('Введите число:'))
count = 1
i = 0
while count <= in_num:
    if in_num % count == 0:
        i += 1
    count += 1
if i == 2:
    print('Число', in_num, 'является простым.')
else:
    print('Число', in_num, 'не является простым.')
