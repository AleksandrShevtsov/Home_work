# Задание 1

# in_num = int(input('Введите число :'))
# i = 0
# res = ''
# while in_num != 0:
#     res = str(in_num % 2) + res
#     in_num //= 2
# print(res)


# Задание 2

in_num = float(input('Введите вещественное число :'))
temp_num = in_num
if in_num < 0:
    temp_num = in_num - int(in_num)
    if temp_num <= -0.5:
        print('Округленное значение:', int(in_num) - 1)
    else:
        print('Округленное значение:', int(in_num))
else:
    temp_num = in_num - int(in_num)
    if temp_num >= 0.5:
        print('Округленное значение:', int(in_num + 1))
    else:
        print('Округленное значение:', int(in_num))
