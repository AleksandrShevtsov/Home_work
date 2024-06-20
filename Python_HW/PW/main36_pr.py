import requests
from bs4 import BeautifulSoup
import re


def find_element_and_path(soup, target_value):
    # Применяем регулярное выражение для поиска элемента с нужным значением
    target_value = re.compile(target_value)

    for element in soup.find_all(string=target_value):
        print(element)
        print(type(element))
        path = []
        current_tag = element.parent
        while current_tag:
            tag = current_tag.name
            attrs = current_tag.attrs if current_tag.attrs else {}
            path.append((tag, attrs))
            current_tag = current_tag.parent
        path.reverse()
        return path
    return None


# Загрузка страницы с курсом валют (пример: wise.com)
url = 'https://wise.com/ru/currency-converter/usd-to-eur-rate'
response = requests.get(url)
# print(response.text)
# Проверка успешности запроса
if response.status_code != 200:
    print("Не удалось загрузить страницу")
else:
    # Создание объекта BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Значение, которое мы ищем, как регулярное выражение
    target_value = r"0\,93[0-9]{2}"

    # Поиск пути к значению
    path = find_element_and_path(soup, target_value)
    if path:
        print(f"Путь к значению, соответствующему регулярному выражению '{target_value}':")
        for tag, attrs in path:
            print(f"Тег: {tag}, Атрибуты: {attrs}")
    else:
        print(f"Значение, соответствующее регулярному выражению '{target_value}', не найдено")









