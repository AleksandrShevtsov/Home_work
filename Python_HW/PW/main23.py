# lst = [1, 2, 3]
# lst_iter = lst.__iter__()
# print(lst_iter)
# print(type(lst_iter))
# # print(lst_iter.__next__())
# # print(lst_iter.__next__())
# # print(lst_iter.__next__())
# # for i in lst_iter:
# #     print(i)
# lst_iter2 = lst.__iter__()
# print(lst_iter.__next__())
# print(lst_iter2.__next__())

# it = iter(lst)
# print(it.__next__())
# print(next(it))
# for i in it:
#     print(i)

# import sys
# numbers = iter(range(1, 1000001))
# print(sys.getsizeof(numbers))
# numbers = range(1, 1000001)
# print(sys.getsizeof(numbers))
# numbers = [i for i in range(1, 1000001)]
# print(sys.getsizeof(numbers))

# numbers = iter(range(1, 1000001))
# print(2000 in numbers)
# print(2000 in numbers)

# lst = [1, 2, 3]
# lst_iter = lst.__iter__()
# print(lst_iter.__next__())
# lst[1] = 5
# print(lst_iter.__next__())


# my_list = [1, 2, 3]
# # print(my_list.__next__())
# # print(my_list.__iter__().__next__())
# it = my_list.__iter__()
# print(it == it.__iter__())
# iterator = iter(my_list)
# while True:
#     try:
#         print(next(iterator))
#     except StopIteration:
#         break
# print("End")

# l = [i for i in range(5)]
# print(type(l))
# l = (i for i in range(5))
# print(type(l))


# ------------------------------------------------------------------


# def my_generator():
#     yield 5546
#     print("Hello")
#     yield 6
#     yield 'fgdg'
#
# gen = my_generator()
# # print(type(gen))
# print(next(gen)) # Выводит 1
# print(next(gen)) # Выводит 2
# print(next(gen)) # Выводит 2
# print(next(gen)) # Выводит 3
# print(next(gen)) # Выводит 3
#
# my_generator0 = [(x for x in range(10))]
# my_generator = (x for x in range(10))
# for item in my_generator:
#     print(item)
#
#
# lst = [1, 2]
# lst2 = {1, 2}
# print(type(lst.__iter__()))
# print(type(lst2.__iter__()))
# iter()

# def show_letters(some_str):
#     yield from ''.join([letter for letter in some_str if letter.isalpha()])
# random_str = show_letters('A!sdf 09 _ w')
# # print(random_str())
# print(next(random_str))


import itertools
my_list = [1, 2, 3, 4, 5]
my_iterator = itertools.islice(my_list, 1, 4)
for item in my_iterator:
    print(item) # Выводит 2, 3, 4


def my_gen(stop, start=0, step=1):
    start = start
    while start < stop:
        yield start
        start += step

for i in my_gen(2):
    print(i)