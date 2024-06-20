# Напишите функцию, которая принимает на вход список чисел и возвращает сумму
# квадратов только четных чисел из списка, используя функциональные подходы
# (например, map, filter и reduce).
# Пример вывода:
# Введите числа: 4, 6, 3, 4, 2, 3, 9, 0, 7
# Результат: 72

def squares_of_numbers(numbers):
    return map(lambda x: x**2, filter(lambda x: x % 2 == 1, numbers))


numbers = list(map(int, input("Введите числа: ").split()))
print(f"Результат: {squares_of_numbers(numbers)}")

# Напишите функцию, которая принимает на вход список функций и значение, а затем
# применяет композицию этих функций к значению, возвращая конечный результат.
# Пример использования:
# add_one = lambda x: x + 1
# double = lambda x: x * 2
# subtract_three = lambda x: x - 3
# functions = [add_one, double, subtract_three]
# compose_functions(functions, 5) должно вывести 9

def compose_functions(functions, value):
    for function in functions:
        value = function(value)
    return value


functions = [lambda x: x + 1, lambda x: x * 2, lambda x: x - 3]
value = int(input('Введите значение: '))
print(compose_functions(functions, value))
