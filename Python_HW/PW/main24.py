# def my_generator():
#     try:
#         yield 1
#         yield 2
#         yield 3
#     except GeneratorExit:
#     # Код для очистки ресурсов
#         pass
# gen = my_generator()
# print(next(gen)) # Выводит 1
# gen.throw(ValueError("Enough"))


# def my_generator():
#     try:
#         yield 1
#         yield 2
#         yield 3
#     except GeneratorExit:
#     # Код для очистки ресурсов
#         pass
# gen = my_generator()
# print(next(gen)) # Выводит 1
# gen.close()
# print(next(gen)) # Выводит 1


# def fibonacci_generator():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# fib_gen = fibonacci_generator()
# for i in range(10):
#     print(next(fib_gen))
# fib_gen.close()


# def my_generator():
#     received_value = yield 1
#     yield received_value + 1
#
# gen = my_generator()
# print(next(gen)) # Выводит 1
# print(gen.send(10)) # Выводит 11



def my_generator():
    value = yield
    if value > 0:
        yield value * 2
    else:
        yield value * 3
gen = my_generator()
print(next(gen))
# print(gen.send(5)) # Выводит 10
print(gen.send(-2)) # Выводит -6