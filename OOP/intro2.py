# class Human:
#     age = 0

#     def __init__(self, first_name, last_name, weigth, nation):
#         self.name = f'{first_name} {last_name}'
#         self.weigth = weigth
#         self.nationlity = nation

#     def birthday(self):
#         from random import randint
#         print(f'\nHappy birthday, {self.name}!!!')
#         self.age += 1
#         self.weigth += randint(3, 7)

#     def show_info(self):
#         print(self.name, self.age, self.weigth, self.nationlity)
        

# human1 = Human('John', 'Snow', 3.300, 'American')
# human2 = Human('Abu-Bakr', 'Al-Nassr', 3.8, 'Arabic')

# human1.show_info()
# human2.show_info()
# print()

# print('after 1 year:')
# human1.birthday()
# human2.birthday()

# print()
# human1.show_info()
# human2.show_info()

#-------------------------------------------------------------------------------------------------------------------------

# class Student:
#     univer = 'Harvard University'

#     def __init__(self, name) -> None:
#         self.name = name
#         self.books = []
#         self.language = {}
#         self.knowledge = 0
#         self.is_ready_to_work = False

#     def add_points(self, points):
#         self.knowledge += points
#         if self.knowledge >= 500 and not self.is_ready_to_work:
#             self.is_ready_to_work = True
#             print(f'{self.name} get 500 points')

#     def read_book(self, book_name):
#         self.books.append(book_name)
#         self.add_points(50)

#     def do_project(self):
#         self.add_points(100)
        
#     def learn_new_language(self, language, percent):
#         if percent not in range(70, 101):
#             print('Invalid points')
#         else:
#             self.language[language] = percent
#             self.add_points

# st1 = Student('John Snow')
# st2 = Student('Billal Billalovich')

# print(st2.name)
# print(st1.name)

# print(f'Before study {st1.name}: {st1.books}, {st1.language}, {st1.knowledge}')
# print(f'Ready to work: {st1.is_ready_to_work}')

# st1.read_book('Game of Thrones')
# st1.read_book('Martin Eden')
# st1.read_book('Alghoritms and Data Structures')
# st1.read_book('Eugene onegin')

# st1.do_project()
# st1.do_project()

# st1.learn_new_language('Python', 40)
# st1.learn_new_language('Python', 90)
# st1.learn_new_language('C++', 75)

# st1.do_project()

# print(f'Before study {st1.name}: {st1.books}, {st1.language}, {st1.knowledge}')
# print(f'Ready to work: {st1.is_ready_to_work}')

#--------------------------------------------------------------------

# class Car:
#     def __init__(self, brand, model) -> None:
#         self.brand = brand
#         self.model = model

#     def show_info(self):
#         return f'{self.brand} -> {self.model}'
    
#     def __str__(self) -> str:
#         return f'{self.brand} -> {self.model}'
    
# obj1 = Car('BMW', '7 series')
# print(obj1)
# obj2 = Car('Lada', 'Sedan')
# print(obj2)
# obj3 = Car('Kia', 'K8')
# print(obj3)
# print(obj.show_info())

#--------------------------------------------------------------
# import random

# class Sniper:
#     hp = 100

#     def __init__(self, name) -> None:
#         self.name = name

#     def shoot(self, other):
#         other.hp -= 20
#         print(f'Атаковал {self}')
#         print(f'У {other} осталось {other.hp}')

#     def __str__(self) -> str:
#         return self.name

# snaper1 = Sniper('John Snow')
# snaper2 = Sniper('Fridrih  Sholtch')

# while snaper1.hp and snaper2.hp:
#     choice = random.randint(1,2)
#     snaper1.shoot(snaper2) if choice == 1 else snaper2.shoot(snaper1)
#     print()

# if snaper1.hp:
#     print(f'{snaper1} won the game!')
# else:
#     print(f'{snaper2} won the game!')

#---------------------------------------------------------------------------------------------

# class Soda:
#     def __init__(self, ingredient=None):
#         if isinstance(ingredient, str):
#             self.ingredient = ingredient
#         else:
#             self.ingredient = None

#     def __str__(self) -> str:
#         if self.ingredient:
#             return(f'Gazirovka iz {self.ingredient}')
#         else:
#             return('Normal gazirovka')

# a = Soda('Malina')
# print(a)

# b = Soda('5')
# print(b)

# c = Soda()
# print(c)

# d = Soda('Grusha')
# print(d)

#------------------------------------------------------------------------------------------------

from typing import List

class TriangleChecker:
    def __init__(self, sides) -> None:
        self.sides = sides

    def __str__(self) -> str:
        if not all(isinstance(x, (int, float)) for x in self.sides):
            return 'нельзя построиит триугольник! инвалид ты аут!'
        elif any(x <= 0 for x in self.sides):
            return 'нельзя построиит триугольник! инвалид ты аут!'
        self.sides.sort()
        if self.sides[0] + self.sides[1] <= self.sides[-1]:
            return 'нельзя построить ьреугольник! сумма меньше или равна!'
        return 'Мы можем построить треугольник!'

t1 = TriangleChecker([10, 10, 10])
print(t1)
t2 = TriangleChecker([-1, 10, 10])
print(t2)
t3 = TriangleChecker([1, 6, 2])
print(t3)
t4 = TriangleChecker([5, 10, 12])
print(t4)





