# Реализация глубокой копии списка
def deepcopy_list(orig_list):
    if not isinstance(orig_list, list):
        return orig_list
    return [deepcopy_list(element) for element in orig_list]

# Пример использования:
original_list = [1, [2, 3], [4, [5, 6]], 7]
copied_list = deepcopy_list(original_list)

print("Оригинальный список:", original_list)
print("Копия списка:", copied_list)

# Изменяем элемент во вложенном списке, чтобы убедиться, что копия не зависит от оригинала
original_list[1][0] = 99

print("Измененный оригинальный список:", original_list)
print("Копия списка после изменения оригинала:", copied_list)


# l = [1, 2, [3, 4]]
# l2 = []
# for el in l:
#     l2.append(el)
# l2[2][0] = 9
# print(l)
# print(l2)


# def fibonacci_recursive(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
#
# # Пример использования
# n = 6
# print(f"Fibonacci({n}) = {fibonacci_recursive(n)}")
#
#
# def fibonacci_iterative(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#
#     a, b = 0, 1
#     for _ in range(2, n + 1):
#         a, b = b, a + b
#     return b
#
#
# # Пример использования
# n = 6
# print(f"Fibonacci({n}) = {fibonacci_iterative(n)}")
#
#
#
#
# def gcd_recursive(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd_recursive(b, a % b)
#
# # Пример использования
# a, b = 48, 18
# print(f"GCD({a}, {b}) = {gcd_recursive(a, b)}")
#
#
# def gcd_iterative(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
#




# def sum_up_to(n):
#     # Базовый случай: сумма чисел до 0 равна 0
#     if n == 0:
#         return 0
#     # Рекурсивный случай: сумма до n равна n плюс сумма до (n-1)
#     else:
#         return n + sum_up_to(n - 1)
#
# # Пример использования
# number = 5
# print(f"Сумма всех чисел до {number} равна {sum_up_to(number)}")
