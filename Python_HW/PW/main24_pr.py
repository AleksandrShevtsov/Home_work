def unique_elements():
    seen = list()  # Множество для хранения уже виденных элементов
    value = yield  # Ожидаем значение от send()
    while True:
        if value not in seen:
            seen.append(value)
            value = yield seen
        else:
            value = yield  # Ждем следующее значение без возврата

# Пример использования:
gen = unique_elements()
next(gen)  # Инициализация генератора

# Передаем значения и выводим уникальные элементы
print(gen.send(1))  # Вывод: 1
print(gen.send(3))  # Вывод: 3
print(gen.send(4))  # Вывод: 4
print(gen.send(2))  # Вывод: 2
print(gen.send(1))  # Повторяющийся элемент, None
print(gen.send(5))  # Вывод: 5

