from abc import ABC, abstractmethod


class Plant(ABC):
    def __init__(self, display_name, height=0, age=0):
        self.display_name = display_name
        self._height = height
        self._age = age
    
    @property
    def height(self):
        return self._height
    
    @property
    def age(self):
        return self._age
    
    @abstractmethod
    def grow_per_season(self):
        pass
    
    def grow(self, amount):
        self._height += amount
        print(f"{self.display_name} вырос на {amount} см, текущая высота: {self._height} см")
    
    def increment_age(self):
        self._age += 1
        print(f"{self.display_name} стал на год старше, текущий возраст: {self._age} лет")
    
    def do_spring(self):
        self.grow(self.grow_per_season())
    
    def do_summer(self):
        self._height += self.grow_per_season()
        print(f"{self.display_name}  вырос летом, текущая высота: {self._height} см")
    
    def do_autumn(self):
        print(f"{self.display_name} не растет осенью, текущая высота: {self._height} см")
    
    def do_winter(self):
        print(f"{self.display_name} не растет зимой, текущая высота: {self._height} см")


class Flower(Plant):
    __flower_grow_per_season = 10
    
    def grow_per_season(self):
        return Flower.__flower_grow_per_season
    
    def do_summer(self):
        print(f"{self.display_name} цветет летом, текущая высота: {self._height} см")
    
    def do_autumn(self):
        self._height = 0
        print(f"{self.display_name} срезан осенью, текущая высота: {self._height} см")


class Tree(Plant):
    __tree_grow_per_season = 20
    
    def grow_per_season(self):
        return Tree.__tree_grow_per_season


# Создаем объекты растений
flower = Flower("Цветок")
tree = Tree("Дерево")
flower1 = Flower("Ромашка", height=10, age=3)

# Кладем растения в список
plants = [flower, tree, flower1]

# Количество лет наблюдения
years = 2

# Наблюдаем за ростом растений
for year in range(years):
    print(f"\nГод {year + 1}:")
    for plant in plants:
        print('spring:', end=' ')
        plant.do_spring()
        print('summer:', end=' ')
        plant.do_summer()
        print('autumn:', end=' ')
        plant.do_autumn()
        print('winter:', end=' ')
        plant.do_winter()
        plant.increment_age()
        print('end of year')