#
#  Напишите программу, которая принимает список слов и возвращает список, содержащий
# только анаграммы.
# Анаграммы - это слова, составленные из одних и тех же букв, но в разном порядке. Создайте
# функцию anagrams, которая принимает список слов в качестве аргумента и возвращает список
# анаграмм.
# Используйте множества и сортировку букв в слове для проверки на анаграмму. Выведите
# результат на экран.

def anagrams(words):
    word_set = set()
    
    for word in words:
        sorted_word = ''.join(sorted(word))
        word_set.add((sorted_word, word))
    
    anagram_dict = {}
    
    for sorted_word, word in word_set:
        if sorted_word not in anagram_dict:
            anagram_dict[sorted_word] = set()
        anagram_dict[sorted_word].add(word)
    
    result = [list(group) for group in anagram_dict.values() if len(group) > 1]
    return result


words_list = input('Введите список слов').split()
anagram_groups = anagrams(words_list)
print("Анаграммы:")
for group in anagram_groups:
    print(group)


# Напишите функцию is_subset, которая принимает два множества set1 и set2
# и проверяет, является ли set1 подмножеством set2.
# Функция должна возвращать True, если все элементы из set1 содержатся в set2,
# и False в противном случае.
# Функция должна быть реализована без использования встроенных методов issubset или <=.

def is_subset(set1, set2):
    if set1.isdisjoint(set2):
        print('False')
    else:
        print('True')


set1 = set(input('1 set ').split())
set2 = set(input('2 set ').split())
is_subset(set1, set2)
