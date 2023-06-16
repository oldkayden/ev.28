# magic methods (магические методы)
# dunder methods (double underscore) -> __init__
# служебные методы

# Магия(фишки) заключается в том что эти методы запускаются без прямого обращения к ниим, определенные методы могут отвечать за определенные операторы 

# class A(int):
#     pass

# obj = A()
# print(dir(obj))

# Магические методы сравнения 
# __eq__(self, other) -> 5 == 8
#                         5.__eq__(8)
# __ne__-> != (не равно)

# __lt__ -> <

# __gt__ -> >

# __le__ -> <=

# __ge__ -> >=

# print('15' < 'ABC')
# print(ord('1'), ord('A'))

# class Word(str):
#     def __new__(cls, obj):
        # print(cls, "!!!")
        # print(obj, "!!!")
#         obj = obj.replace(' ', '')
#         return super().__new__(cls, obj)

#     def __gt__(self, other) -> bool:
#         print('gt работал')
#         print(self)
#         print(other)
#         return len(self) > len(other)
    
#     def __lt__(self, __value) -> bool:
#         return len(self) < len(__value)

#     def __eq__(self, __value) -> bool:
#         return len(self) == len(__value)

# obj = Word('        Hello John')
# obj1 = Word('     Make   rs')

# obj > obj1
# print(obj > obj1)
# print(obj < obj1)
# print(obj == obj1)
#-----------------------------------------------------------------------------------------------

# + - / * // % **

# + -> __add__
# - -> __sub__
# * -> __mul__
# // -> __floordiv__
# / -> __truediv__
# % -> __mod__
# ** -> __pow__

# class Cifra:
#     def __new__(cls, *args, **kwargs):
#         number = abs(args[0])
#         instance = super().__new__(cls)
#         instance.number = number
#         return instance
    

#     def __add__(self, other):
#         print('add вызвона')
#         res = self.number + other.number
#         print(f'Result: {self.number} + {other.number} = {res}')
        

# value1 = Cifra(-117)
# value2 = Cifra(53)
# value1 + value2

#-------------------------------------------------------------------------------

# from random import choice

# class Dog:
#     def sound(self):
#         print('Bark!')

# class Cat:
#     def sound(self):
#         print('Meow meow!')

# class Lion:
#     def sound(self):
#         print('Roar!')

# class Pet:
#     def __new__(cls):
#         other = choice([Dog, Cat, Lion])
#         instance = super().__new__(other)
#         print(f'I\'m {type(instance).__name__}')
#         return instance
    
#     def __init__(self) -> None:
#         print('Pet never was called!')

# pet = Pet()
# pet.sound()

#-------------------------------------------------------------------------------------

# SINGLETON

# class Singleton:
#     _instance = None
#     def __new__(cls):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#         return cls._instance
    
#     def __str__(self) -> str:
#         return str(id(self))
    
# a = Singleton()
# b = Singleton()
# print(a)
# print(b)
# print(a is b)
# obj = Singleton()
# obj1 = Singleton()
# print(obj , obj1)

#-------------------------------------------------------------------------------------------------
# дандер методы строкового отображения объектов
# __str__
# __repr__

# class Base:
#     def __init__(self, stroka) -> None:
#         self.string = stroka

#     def __str__(self) -> str:
#         return f'Объект: {self.string}'
    

#     def __repr__(self) -> str:
#         return 'Base("Example")'


# obj = Base('Jasy')
# print(obj)
# print(repr(obj))
# obj2 = Base('Emmir')
# print(obj2)
# obj3 = eval(repr(obj2))
# print(obj3)

#--------------------------------------------------------------------------------------------

# class Kopilka:
#     def __init__(self) -> None:
#         self.total = 0
#         self.coins = []

#     def add_coin(self, coin):
#         self.total += coin
#         self.coins.append(coin)

#     def __len__(self):
#         return len(self.coins)
    
#     def __getitem__(self, index):
#         return self.coins[index - 1]

# obj =Kopilka()
# obj.add_coin(10)
# obj.add_coin(5)
# obj.add_coin(600)
# print(obj.total)
# print(obj.coins)
# print(len(obj))
# print(obj[1])
# print(obj[2])
# print(obj[3])

# for x in obj:
#     print(x)
#------------------------------------------------------------------------------------
# чекюрслеф 

# class Dog:
#     def voice(self):
#         print("Гав")

# class Cat:
#     def voice(self):
#         print("Мяу")

# barsik = Cat()
# rex = Dog()

# def to_pet(animals):
#     animals.voice()

# to_pet(barsik)
# to_pet(rex)
#-------------------------------

# class CreateMixin: 
#     todos = {} 
#     def create(self, key, todo): 
#         if key in self.todos.keys(): 
#             return 'Задача под таким ключом уже существует' 
#         self.todos[key] = todo 
#         return self.todos 
    
# class DeleteMixin: 
#     todos = {} 
#     def delete(self, key):
#         delete_ = self.todos.pop(key, 'нет такого ключа') 
#         if 'нет такого ключа' == delete_: 
#             return delete_ 
#         else:
#             return delete_ 
        

# class UpdateMixin: 
#     todos = {} 
#     def update(self, key, new_value): 
#         self.todos[key] = new_value 
#         return self.todos 
    
# class ReadMixin: 
#     todos = {} 
#     def read(self): 
#         res = [x for x in self.todos.items()] 
#         return sorted(res) 
    
# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin): 
#     def set_deadline(self, deadline): 
#         import datetime 
#         time_ = datetime.datetime.now().strftime('%d/%m/%Y') 
#         deadline = deadline.split('/') 
#         time_ = time_.split('/') 
#         deadline = list(map(int, deadline)) 
#         time_ = list(map(int, time_)) 
#         time_ = sum((time_[0], time_[1]*30, time_[2]*365)) 
#         deadline = datetime.date(deadline[2], deadline[1], deadline[0]) 
#         time_ = datetime.date.today() 
#         return (deadline - time_).days 
    
# task = ToDo() 
# print(task.set_deadline('31/12/2022'))
# print(task.create(1, 'todo')) 
# print(task.delete(3)) 
# print(task.update(1, 'todo')) 
# print(task.read()) 
# print(task.create(1, 'Do housework')) 
# print(task.create(1, 'Do housework')) 
# print(task.create(2, 'Go for a walk')) 
# print(task.update(1, 'Do homework')) 
# print(task.delete(2)) 
# print(task.read()) 
# print(task.set_deadline('31/12/2021'))
# как классно что я вчера делал таски по множественому наследование и миксины
#----------------------------------
from abc import ABC, abstractmethod

class Bird(ABC):
#     @abstractmethod
    def fly(self):
        pass
    
#     @abstractmethod
    def grow(self):
        pass
    
#     @abstractmethod
    def sound(self):
        pass

class Animal(ABC):
#     @abstractmethod
    def sound(self):
        pass
    
#     @abstractmethod
    def run(self):
        pass
    
#     @abstractmethod
    def grow(self):
        pass

class Plant(ABC):
#     @abstractmethod
    def grow(self):
        pass
    
#     @abstractmethod
    def photosynthesize(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Я лечу как воробей")
    
    def grow(self):
        print("Я расту как воробей")
    
    def sound(self):
        print("Чирик-чирик")

class Lion(Animal):
    def sound(self):
        print("Ррррр")
    
    def run(self):
        print("Я бегу как лев")
    
    def grow(self):
        print("Я расту как лев")

class Rose(Plant):
    def grow(self):
        print("Я расту как роза")
    
    def photosynthesize(self):
        print("Я фотосинтезирую как растение")

# Пример использования классов и их методов:
sparrow = Sparrow()
sparrow.fly()  # Вывод: Я лечу как воробей
sparrow.grow()  # Вывод: Я расту как воробей
sparrow.sound()  # Вывод: Чирик-чирик

lion = Lion()
lion.sound()  # Вывод: Ррррр
lion.run()  # Вывод: Я бегу как лев
lion.grow()  # Вывод: Я расту как лев

rose = Rose()
rose.grow()  # Вывод: Я расту как роза
rose.photosynthesize()  # Вывод: Я фотосинтезирую как растение

