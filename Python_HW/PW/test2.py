def squares_of_numbers(numbers):
    return list(map(lambda x: x**2, filter(lambda x: x % 2 == 1, numbers)))


numbers = list(map(int, input("Введите числа: ").split()))
print(f"Результат: {squares_of_numbers(numbers)}")
