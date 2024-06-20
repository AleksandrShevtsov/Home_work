# # Задание 1
# num1 = int(input('Введите 1-ое число'))
# num2 = int(input('Введите 2-ое число'))
# num3 = int(input('Введите 3-ое число'))
#
# if num1 < num2 < num3:
#     print(num1, num2, num3, sep=',')
# elif num1 < num3 < num2:
#     print(num1, num3, num2, sep=',')
# elif num2 < num1 < num3:
#     print(num2, num1, num3, sep=',')
# elif num2 < num3 < num1:
#     print(num2, num3, num1, sep=',')
# elif num3 < num1 < num2:
#     print(num3, num1, num2, sep=',')
# else:
#     print(num2, num1, num3, sep=',')

# 3адание 2

Year = int(input('Введите Год:'))

if not Year % 400:
    print('Год является высокосным')
elif not Year % 100:
   print('Год не является высокосным')
elif not Year % 4:
    print('Год является высокосным')
else:
    print('Год не является высокосным')