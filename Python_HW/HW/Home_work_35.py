# 1. Напишите функцию get_response(url), которая отправляет GET-запрос по заданному URL-адресу и возвращает объект ответа. Затем выведите следующую информацию об ответе:
# - Код состояния (status code)
# - Текст ответа (response text)
# - Заголовки ответа (response headers)

import requests


def get_response(url):
    return requests.get(url)


url = "https://api.openai.com/v1/completions"
response = get_response(url)
print("Status Code:", response.status_code)
print("Response Text:", response.text)
print("Response Headers:", response.headers)

# 2. Напишите функцию find_common_words(url_list),
# которая принимает список URL-адресов и возвращает список наиболее часто встречающихся слов на веб-страницах.
# Для каждого URL-адреса функция должна получить содержимое страницы с помощью запроса GET и
# использовать регулярные выражения для извлечения слов.
# Затем функция должна подсчитать количество вхождений каждого слова и
# вернуть наиболее часто встречающиеся слова в порядке убывания частоты.

import requests
import re


def find_common_words(url_list):
    # Определяем пустое словарь для хранения частот слов
    common_words = {}
    #
    for url in url_list:
        response = requests.get(url)
        text = response.text
        words = re.findall(r'\w+', text)
        for word in words:
            if word.lower() in common_words:
                common_words[word.lower()] += 1
            else:
                common_words[word.lower()] = 1
    sorted_common_words = sorted(common_words.items(), key=lambda x: x[1], reverse=True)
    return [word[0] for word in sorted_common_words]


url_list = [
    'https://www.example.com/page1',
    'https://www.example.com/page2',
    'https://www.example.com/page3'
]
common_words = find_common_words(url_list)
print(common_words)
