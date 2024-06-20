# Создайте класс Rectangle для представления прямоугольника.
# Класс должен иметь атрибуты width (ширина) и height (высота) со значениями по
# умолчанию, а также методы calculate_area() для вычисления площади прямоугольника и
# calculate_perimeter() для вычисления периметра прямоугольника.
# Переопределить методы __str__, __repr__.
# Затем создайте экземпляр класса Rectangle и выведите информацию о нем,
# его площадь и периметр.

class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
# Надеюсь я правильно понял задание с переопределением методов
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"


rectangle = Rectangle(10, 20)
print(rectangle)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())


# Создайте класс BankAccount для представления банковского счета.
# Класс должен иметь атрибуты account_number (номер счета) и balance (баланс), а также
# методы deposit() для внесения денег на счет и withdraw() для снятия денег со счета.
# Затем создайте экземпляр класса BankAccount, внесите на счет некоторую сумму и снимите
# часть денег. Выведите оставшийся баланс.
# Не забудьте предусмотреть вариант, при котором при снятии баланс может стать меньше
# нуля. В этом случае уходить в минус не будем, вместо чего будем возвращать сообщение
# # "Недостаточно средств на счете"

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            return "Недостаточно средств на счете"
        return self.balance


account = BankAccount(123456789, 1000)
print(account.deposit(500))
print(account.withdraw(200))
