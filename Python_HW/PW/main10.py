s = "Hello world!"
print("world" in s)
index = s.find("world")
print(index)
print(s.index("world"))

print(s.find("ghfh"))
# print(s.index("ghfh"))

# text = "He llo"
# is_alpha = text.isdecimal()
# print(is_alpha)
#
# text = "Hello, world!"
# starts_with_hello = text.startswith("Hello")
# print(starts_with_hello)

# text = "Hello, World!"
# lower_text = text.lower()
# print(lower_text)
# print(text)

# print("The Moon And The Earth".lower())

# text = "Hello, World!"
# new_text = text.replace("Hello", "Hi")
# print(new_text)
# print(text)

# text = "Hello,   world!,         world?"
# words = text.split(", ") # Разделение строки на подстроки
# print(words)
# print(type(words))
# joined_text = "".join(words) # Объединение списка подстрок в строку
# print(joined_text)
# print(type(joined_text))
#
# print(text.split())
# print("".join(text.split()))
# print("".join(text.split("  ")))


# s = input()
# a, b, c, d = s.split()
#
# print(a, b, c, d)

# text = "Hello"
# aligned = text.rjust(10)


# print(text.rjust(10))
# print("d".rjust(10))
# print("text".rjust(10))
# print("srtwetasdadsadett".rjust(10))


# text = "------   Hello, world!   ------"
# stripped_text = text.strip('-').strip()
# # stripped_text = "   Hello, world!   ".strip()
# print(stripped_text)
#
# stripped_text = text.strip('-')
# print(stripped_text)
# stripped_text2 = stripped_text.strip()
# print(stripped_text2)


# Приходит текст из 5 строк.
# Задача:
# ● сделать так, чтобы все предложения начинались с большой буквы.
# ● не было подряд несколько пробелов, запятых, многоточий и т.п.
# ● строка не должна начинаться с пробелов, допустима только табуляция (отступ).


text = ('''     сделать так, чтобы все предложения начинались с большой буквы.
     не было подряд несколько пробелов,,, запятых, многоточий.
     строка не должна начинаться с пробелов, допустима только табуляция (отступ)!!!''')
print(text)
sentences = text.split('\n')
print(sentences)
a, b, c = sentences
a = a.strip().capitalize().replace(",,,", ",").replace("!!!", "!")
b = b.strip().capitalize().replace(",,,", ",").replace("!!!", "!")
c = c.strip().capitalize().replace(",,,", ",").replace("!!!", "!")
print("\n".join((a, b, c)))
# print("text".capitalize())
"fdsfsd".replace("f", "")