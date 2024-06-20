# 1. Напишите функцию find_longest_word, которая будет принимать список слов и возвращать
# самое длинное слово из списка.
# Аннотируйте типы аргументов и возвращаемого значения функции.

def find_longest_word(words: list[str]) -> str:
    longest_word = max(words, key=len)
    return longest_word

words = ["apple", "banana", "cherry", "dragonfruit"]
result = find_longest_word(words)
print(result)


# a. Напишите программу, которая будет считывать данные о продуктах из файла и
# использовать аннотации типов для аргументов и возвращаемых значений функций.
# Создайте текстовый файл "products.txt", в котором каждая строка будет содержать
# информацию о продукте в формате "название, цена, количество".

# b. В программе определите функцию calculate_total_price, которая будет принимать
# список продуктов и возвращать общую стоимость.

# c. Продумайте, какая аннотация должна быть у аргумента.

# d. Считайте данные из файла, разделите строки на составляющие и создайте список
# продуктов.

# e. Вызовите функцию calculate_total_price с этим списком и выведите результат.

def calculate_total_price(products: list[tuple[str, float, int]]) -> float:
    total_price = 0.0
    
    for product in products:
        name, price, quantity = product
        total_price += price * quantity
    return total_price


# чтение данных
products = []
with open("products.txt", "r") as file:
    for line in file:
        # разделение строк на составляющие
        name, price, quantity = line.strip().split(",")
        # добавление данных
        products.append((name, float(price), int(quantity)))

total_price = calculate_total_price(products)
print(f"Total price: {total_price:.2f}")

