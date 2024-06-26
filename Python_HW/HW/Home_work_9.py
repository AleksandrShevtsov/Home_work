# Напишите программу, которая запрашивает у пользователя строку и определяет,
# является ли она панграммой.
# Панграмма - это фраза, содержащая все буквы алфавита.
# Программа должна игнорировать регистр букв и пробелы при проверке панграммы.
# Выведите соответствующее сообщение на экран с помощью команды print.
# Решить задачу для латиницы.

S = input('Введите текст: ')
alfavit = 'qwertyuioplkjhgfdsazxcvbnm'
S = S.lower()
S = S.replace(' ', '')
print(S)
i = 0
while i < len(S):
    if S[i] in alfavit:
        alfavit = alfavit.replace(S[i], '')
    i += 1
if alfavit == '':
    print('Строка является панграммой')
else:
    print('Строка не является панграммой')


# Напишите программу, которая запрашивает у пользователя строку и выводит на экран
# количество гласных и согласных букв в ней.
# Используйте функцию len() для подсчета количества букв.
# Выведите результат на экран с помощью команды print.
# Решить задачу для латиницы.

S = input('Введите текст: ')
vowel = 'aeoiyu'
S = S.lower()
S = S.replace(' ', '')
count, count1, i = 0, 0, 0
while i < len(S):
    if S[i] in vowel:
        count += 1
    else:
        count1 += 1
    i += 1

print(f'Гласных: {count}, Согласных: {count1}')