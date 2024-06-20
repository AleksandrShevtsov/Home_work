# Создать генератор, который будет делать то же самое что и range с одним аргументом.
def my_range(end):
    current = 0
    while current < end:
        yield current
        current += 1

# Пример использования:
for num in my_range(10):
    print(num)



# # Доработать предыдущий генератор так, чтобы он мог принимать один, два или три аргумента, как и обычный range.
# def my_range(*args):
#     # Обработка числа аргументов
#     num_args = len(args)
#
#     # Установка значений start, stop, и step в зависимости от числа аргументов
#     if num_args == 1:
#         start = 0
#         stop = args[0]
#         step = 1
#     elif num_args == 2:
#         start = args[0]
#         stop = args[1]
#         step = 1
#     elif num_args == 3:
#         start = args[0]
#         stop = args[1]
#         step = args[2]
#     else:
#         raise TypeError(f"my_range expected at most 3 arguments, got {num_args}")
#
#     # Генерация чисел
#     current = start
#     if step > 0:
#         while current < stop:
#             yield current
#             current += step
#     elif step < 0:
#         while current > stop:
#             yield current
#             current += step
#     else:
#         raise ValueError("my_range() arg 3 must not be zero")
#
#
# # Пример использования:
# print("Range with one argument:")
# for num in my_range(5):
#     print(num)
#
# print("\nRange with two arguments:")
# for num in my_range(2, 5):
#     print(num)
#
# print("\nRange with three arguments:")
# for num in my_range(1, 10, 2):
#     print(num)
#
# print("\nRange with negative step:")
# for num in my_range(10, 1, -2):
#     print(num)





