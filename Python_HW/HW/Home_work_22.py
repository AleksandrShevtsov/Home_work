# Напишите программу, которая открывает файл, считывает из него два числа и выполняет
# операцию их деления.
# Если число отрицательное, выбросите исключение ValueError с сообщением: "Число
# должно быть положительным".
# Обработайте исключение и выведите соответствующее сообщение.

# Открываем файл в режиме чтения
# import random
#
# with open('names1.txt', 'r') as file:
#     # Читаем два числа из файла
#     try:
#         numbers = file.read().split()
#         num1 = int(numbers[random.randint(0, 10)])
#         num2 = int(numbers[random.randint(0, 10)])
#
#         # Если число отрицательное, выбрасываем исключение ValueError
#         if num1 < 0 or num2 < 0:
#             raise ValueError('Число должно быть положительным')
#
#         # Выполняем деление
#         result = num1 / num2
#
#         # Выводим результат
#         print(f"Результат деления: {result}")
#
#     # Обработка исключения ValueError
#     except ZeroDivisionError as e:
#         print(f"Ошибка: {e}")
#
# Напишите программу, которая открывает файл, считывает его содержимое и выполняет
# операции над числами в файле.
# Обработайте возможные исключения при открытии файла (FileNotFoundError) и при
# выполнении операций над числами (ValueError, ZeroDivisionError).
# Используйте конструкцию try-except-finally для обработки исключений и закрытия файла
# в блоке finally.
import random

try:
    file = open('names1.txt', 'r')
    content = file.read()
    numbers = content.split()
    num1 = int(numbers[random.randint(0, len(numbers) - 1)])
    num2 = int(numbers[random.randint(0, len(numbers) - 1)])
    result = num1 / num2
    print(f"Result: {num1} / {num2} = {result}")
    
except ValueError:
    print("Invalid input. Please enter two integers.")
    
except ZeroDivisionError:
    print("Cannot divide by zero.")
    
except FileNotFoundError:
    print("File not found.")
    
finally:
    if 'file' in locals():
        file.close()
        