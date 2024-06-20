# def my_generator():
#     try:
#         yield 1
#         yield 2
#         yield 3
#     except ValueError:
#         print("Inside gen")
#         yield 4
#         yield 5
#         yield 6
#
#
# gen = my_generator()
# print(next(gen))
# gen.throw(ValueError("Enough"))
# print(next(gen))
# # print(next(gen))
# gen.close()
# print(next(gen))





# def running_sum():
#     total = 0
#
#     while True:
#         value = yield total
#         print(f'Total is {total}')
#         total += value
#         raise ValueError
#
# # Создаем генератор
# gen = running_sum()
#
# # Инициализация генератора
# print(next(gen))  # Вывод: 0
#
# # Передаем значения и получаем промежуточные суммы
# print(gen.send(10))  # Вывод: 10
# print(gen.send(20))  # Вывод: 30
# print(gen.send(5))   # Вывод: 35

#
#
#
# def my_generator():
#     value = 0
#     while True:
#         value = yield value  # Ожидаем значение от send()
#         if value > 0:
#             value = value * 2
#         else:
#             value = value * 3
#
# # Создаем генератор
# gen = my_generator()
#
# # Инициализация генератора
# next(gen)
#
# # Пример использования
# print(gen.send(5))    # Ожидаемый вывод: 10
# print(gen.send(-2))   # Ожидаемый вывод: -6
# print(gen.send(10))   # Ожидаемый вывод: 20
# print(gen.send(-3))   # Ожидаемый вывод: -9
#



