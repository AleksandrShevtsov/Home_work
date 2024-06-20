# Напишите функцию extract_emails(text), которая извлекает все адреса электронной почты из заданного текста и возвращает их в виде списка.
# Пример использования:
# text = "Contact us at info@example.com or support@example.com for assistance."
# emails = extract_emails(text)
# print(emails)  # Вывод: ['info@example.com', 'support@example.com']

import re

def extract_emails(text):
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    return emails


text = "Contact us at info@example.com or support@example.com for assistance."
emails = extract_emails(text)
print(emails)


# Напишите функцию highlight_keywords(text, keywords), которая выделяет все вхождения заданных ключевых слов в тексте,
# окружая их символами *. Функция должна быть регистронезависимой при поиске ключевых слов.

import re


def highlight_keywords(text, keywords):
    pattern = re.compile('|'.join(map(re.escape, keywords)), re.IGNORECASE)
    
    def replace(match):
        return f"*{match.group(0)}*"
    
    modified_text = pattern.sub(replace, text)
    return modified_text


text = "This is a sample text. We need to highlight Python and programming."
keywords = ["python", "programming"]
highlighted_text = highlight_keywords(text, keywords)
print(highlighted_text)
