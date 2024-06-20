# Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы,
# использует библиотеку Beautiful Soup для парсинга HTML и
# выводит список всех ссылок на странице.
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

url = input("Введите URL-адрес веб-страницы: ")

# Если пользовательский ввод не содержит схемы (http или https), программа добавляет схему http по умолчанию.
if not url.startswith(('http://', 'https://')):
    url = 'http://' + url

try:
    # Загружаем страницу
    response = requests.get(url)
    response.raise_for_status()  # Проверяем, был ли запрос успешным
    # Парсим HTML с помощью BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    # Находим все теги <a>
    links = soup.find_all('a')

    # Выводим все ссылки
    print("Ссылки на странице:")
    for link in links:
        href = link.get('href')
        if href:
            # Создаем полный URL-адрес
            full_url = urljoin(url, href)
            # Проверяем, что это действительно URL
            parsed_url = urlparse(full_url)
            if parsed_url.scheme in ['http', 'https']:
                print(full_url)
except requests.exceptions.RequestException:
    print(f"Ошибка при загрузке страницы: {url}")

# Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы и
# уровень заголовков, а затем использует библиотеку Beautiful Soup для парсинга HTML
# и извлекает заголовки нужного уровня (теги h1, h2, h3 и т.д.) с их текстом.
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

url = input("Введите URL-адрес веб-страницы: ")

# Если пользовательский ввод не содержит схемы (http или https), программа добавляет схему http по умолчанию.
if not url.startswith(('http://', 'https://')):
    url = 'http://' + url

try:
    # Загружаем страницу
    response = requests.get(url)
    response.raise_for_status()  # Проверяем, был ли запрос успешным
    header_level = int(input("Уровень заголовков: "))
    # Парсим HTML с помощью BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Находим все теги <h1>, <h2>, <h3> и т.д.
    headers = soup.find_all(f'h{header_level}', limit=header_level)
    if headers:
        # Выводим все заголовки
        print("Заголовки на странице:")
        for header in headers:
            print(header.text)
    else:
        print("Заголовков нет")

except requests.exceptions.RequestException:
    print(f"Ошибка при загрузке страницы: {url}")
