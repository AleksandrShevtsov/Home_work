# Напишите функцию merge_dicts, которая принимает произвольное количество словарей в
# качестве аргументов и возвращает новый словарь, объединяющий все входные словари.
# Если ключи повторяются, значения должны быть объединены в список. Функция должна
# использовать аргумент **kwargs для принятия произвольного числа аргументов словаря.
def merge_dicts(**kwargs):
	result = {}
	for d in kwargs.values():
		for key, value in d.items():
			if key in result:
				if not isinstance(result[key], list):
					result[key] = [result[key]]
				result[key].append(value)
			else:
				result[key] = [value]
	return result


a = {'a': 1, 'b': 2}
b = {'b': 3, 'c': 4}
c = {'c': 5, 'd': 6}

print(merge_dicts(a=a, b=b, c=c))


# Напишите программу, которая принимает строку от пользователя и подсчитывает
# количество уникальных символов в этой строке. Создайте функцию count_unique_chars,
# которая принимает строку и возвращает количество уникальных символов. Выведите
# результат на экр


def count_unique_chars(line):
	return len(set(line))


line = input('Enter words:')
print('umber of unique characters:', count_unique_chars(line))


# Напишите программу, которая создает словарь, содержащий информацию о студентах и их
# оценках. Ключами словаря являются имена студентов, а значениями - списки оценок.
# Создайте функцию calculate_average_grade, которая принимает словарь с оценками
# студентов и вычисляет средний балл для каждого студента. Функция должна возвращать
# новый словарь, в котором ключами являются имена студентов, а значениями - их средний
# балл. Выведите результат на экран.

def calculate_average_grade(stud_journal): # calculate
	for key, values in stud_journal.items():
		stud_journal[key] = sum(values) / len(values)
	return stud_journal


def calculate_average_grade_v2(stud_journal):
	return {key: sum(value) / len(value) for key, value in stud_journal.items()}


grades = {
	'Alice': [85, 90, 92],
	'Bob': [78, 80, 84],
	'Carol': [92, 88, 95]
}
print('V1: ', calculate_average_grade(grades))

print('V2: ', calculate_average_grade_v2(grades))
