# Реализовать класс Counter, который представляет счетчик. Класс должен поддерживать
# следующие операции:
# ● Увеличение значения счетчика на заданное число (оператор +=)
# ● Уменьшение значения счетчика на заданное число (оператор -=)
# ● Преобразование счетчика в строку (метод __str__)
# ● Получение текущего значения счетчика (метод __int__)

class Counter:
    def __init__(self, value):
        self.value = value

    def __int__(self):
        return self.value

    def __str__(self):
        return str(self.value)

    def __iadd__(self, other):
        self.value += other
        return self

    def __isub__(self, other):
        self.value -= other
        return self
    

counter = Counter(10)
print(counter)
counter += 5
print(counter)
counter -= 3
print(counter)

# Реализовать класс Email, представляющий электронное письмо. Класс должен
# поддерживать следующие операции:
# ● Сравнение писем по дате (операторы <, >, <=, >=, ==, !=)
# ● Преобразование письма в строку (метод __str__)
# ● Получение длины текста письма (метод __len__)
# ● Получение хеш-значения письма (метод __hash__)
# ● Проверка наличия текста в письме (метод __bool__)

import functools
import datetime


@functools.total_ordering
class Email:
    def __init__(self, from_email, to_email, subject, text, date):
        self.from_email = from_email
        self.to_email = to_email
        self.subject = subject
        self.text = text
        self.date = date
    
    def __str__(self):
        return f"From: {self.from_email}\nTo: {self.to_email}\nSubject: {self.subject}\n{self.text}"
    
    def __len__(self):
        return len(self.text)
    
    def __hash__(self):
        return hash(self.text)
    
    def __bool__(self):
        return bool(self.text)
    
    def __lt__(self, other):
        return self.date < other.date
    
    def __eq__(self, other):
        return self.date == other.date


email1 = Email("john@example.com", "jane@example.com", "Meeting", "Hi Jane, let's have a meeting tomorrow.",
               "2022-05-10")
email2 = Email("jane@example.com", "john@example.com", "Re: Meeting", "Sure, let's meet at 2 PM.", "2022-05-10")
email3 = Email("alice@example.com", "bob@example.com", "Hello", "Hi Bob, how are you?", "2022-05-09")

print(email1)
print(len(email2))
print(hash(email3))
print(bool(email1))
print(email2 > email3)
