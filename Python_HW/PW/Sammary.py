# 5. Создать класс Person с полями имя и дата рождения.
#
# 6. Создать 10 объектов этого класса с разными именами.
#
# 7. Создать класс Employee который содержит поле имя и возраст.
#
# 8. Написать функцию, которая из списка объекта класса Person создает список из объектов класса Employee, вычисляя возраст каждого Person по дате рождения.
#
# Подумать, где должна быть реализована функция, вычисляющая возраст по дате рождения.
# Варианты: в конструкторе класса Employee, в качестве глобальной функции, в качестве метода класса (какого?).
# Получившийся список должен содержать сотрудников, старше 18 лет. Использовать map и filter.
# У классов Person и Employee должны быть определены конструкторы.
# Реализация трансформации список персонов в сотрудников должна быть в одну строчку.
#
# 9. Вывести получившихся сотрудников на экран.
#
# 10. Используя функцию forAll() убедиться, что все сотрудники действительно старше 18 лет.
import datetime


class Person:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth
    def age(self):
        today = datetime.date.today()
        age = today.year - self.date_of_birth.year
        return age

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("Alexey", datetime.date(1996, 4, 17))
person2 = Person("Vasiliy", datetime.date(1999, 8, 12))
person3 = Person("Sergey", datetime.date(1995, 5, 10))
person4 = Person("Yuriy", datetime.date(2000, 11, 21))

print(person1.age())


def persons_to_employees(*person):
    return filter(lambda emp: emp.age() >= 18, map(lambda x: Employee(x.name, x.age()), person))
        

employees = persons_to_employees(person1, person2, person3, person4)
print(list(employees))




from datetime import datetime

class Person:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def __str__(self):
        return f'Rerson(name = {self.name}, birthday = {self.birthday})'

    def count_age(self):
        now = datetime.today()
        age = now.year - self.birthday.year
        return age

person1 = Person('Anna', datetime(1987, 1, 20))
person2 = Person('Alex', datetime(2010, 9, 10))
person3 = Person('Bob', datetime(1978, 3, 30))
person4 = Person('Irina', datetime(1990, 10, 3))
person5 = Person('Alex', datetime(1988, 12, 14))
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Employee(name: {self.name}, age: {self.age})'

person_list = [person1, person2, person3, person4, person5]

def pers_to_empl(person_list):
    return filter(lambda empl: empl.age >= 18, map(lambda pers: Employee(pers.name, pers.count_age()), person_list))


result = list(pers_to_empl(person_list))
print(*list(pers_to_empl(person_list)), sep=";   ")