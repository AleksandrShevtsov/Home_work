# import requests
# from bs4 import BeautifulSoup
# html = requests.get("https://example.com").text
# # print(html)
# # Создание объекта Beautiful Soup из HTML-страницы
# soup = BeautifulSoup(html, "html.parser")
# # # Извлечение данных из тегов
# title = soup.title.text
# # print(title)
# links = soup.find_all("a")
# # print(links)
# # Навигация по структуре документа
# parent = soup.find("div").parent
# # print(parent)
# # next_sibling = soup.find("div").next_sibling
# next_sibling = soup.find("h1").next_element
# print('next_sibling')
# print(next_sibling)
# print('next_sibling')
#
# # # Манипуляции с содержимым
# new_tag = soup.new_tag("a", href="https://example.com")
# soup.body.append(new_tag)
# print(soup)



# from bs4 import BeautifulSoup
# # Создание объекта Beautiful Soup из сырого HTML
# html ="""
# <html>
# <body>
#  <h1>Заголовок</h1>
#  <p>Текст параграфа</p>
#  <a href="https://example.com">Ссылка</a>
# </body>
# """
# soup = BeautifulSoup(html, "html.parser")
# # Извлечение заголовка
# title = soup.find("h1").text
# # print(title)
# # Извлечение текста параграфа
# paragraph = soup.find("p").text
# # print(paragraph)
# # Извлечение ссылки
# link = soup.find("a")
# print(link)
# print(link["href"])

import requests
from bs4 import BeautifulSoup
html = requests.get("https://realpython.com").text
soup = BeautifulSoup(html, "html.parser")
links = soup.find_all("a")
print(links)
for i in links[:5]:
    # print(type(i))
    href = i.attrs.get("href")
    if href[:4]=="http":
        print(href)
    # print(href)
