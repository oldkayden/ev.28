'''
Абстракеция 
'''
# Абстракция (Абстрактный класс) - принцип ООПб в котором создается абстрактный класс (класс - пустышка), в котором задается названия аттрибутов и методов, для того чтобы в дочерных классаз переопределить их нужным образомю (У нас есть название, но нет логики)

# from abc import ABC, abstractmethod, abstractproperty

# class AbstractAnimal(ABC):

#     @abstractmethod
#     def voice(self):
#         ...

#     @abstractproperty
#     def legs(self):
#         ...


# @abstractmethod - декоратор который требует переопреледеление метода в наследуемом классе

# @abstractproperty I декоратор который требует 


# obj = AbstractAnimal() #TypeError: Can't instantiate abstract class AbstractAnimal with abstract methods legs, voice

# class Dog(AbstractAnimal):
#     ...

# obj = Dog() #Error

# class Dog(AbstractAnimal):
#     legs = 4 


#     def voice(self):
#         print('гав-гав')

# class Cat(AbstractAnimal):
#     legs = 4 


#     def voice(self):
#         print('meow')

# dog = Dog()
# cat = Cat()
# arr = [dog, cat]
# for i in arr:
#     i.voice()
#     print(i.legs)    

# obj = Dog() #TypeError: Can't instantiate abstract class Dog with abstract methods legs
# obj.voice()
# print(obj.legs)

# class Shape(ABC):
#     def __init__(self, name):
#         self.name = name

#     @abstractmethod
#     def area(self):
#         ...

# class Square(Shape):
#     def __init__(self, name , lenght):
#         super().__init__('Square')
#         self.lenght = lenght

#     def area(self):
#         return self.lenght **2
    
# obj = Square(12)
# print(obj.name)
# print(obj.area())
#---------------------- - - - - - - - - - - --  -- - - - - - - - - - -
# from abc import ABC, abstractmethod

# class Bird(ABC):
#     @abstractmethod
#     def fly(self):
#         pass

#     @abstractmethod
#     def grow(self):
#         pass

#     @abstractmethod
#     def sound(self):
#         pass


# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass

#     @abstractmethod
#     def run(self):
#         pass

#     @abstractmethod
#     def grow(self):
#         pass


# class Plant(ABC):
#     @abstractmethod
#     def grow(self):
#         pass

#     def photosynthesize(self):
#         print('Я фотосинтезирую')


# class Sparrow(Bird):
#     def fly(self):
#         print('Я лечу как воробей')

#     def grow(self):
#         print('Я расту как воробей')

#     def sound(self):
#         print('Чирик-чирик')


# class Dog(Animal):
#     def sound(self):
#         print('Гав-гав')

#     def run(self):
#         print('Я бегу как собака')

#     def grow(self):
#         print('Я расту как собака')


# class Tree(Plant):
#     def grow(self):
#         print('Я расту как дерево')


# sparrow = Sparrow()
# dog = Dog()
# tree = Tree()

# sparrow.fly()
# sparrow.grow()
# sparrow.sound()

# dog.sound()
# dog.run()
# dog.grow()

# tree.grow()
# tree.photosynthesize()
      

#---------------------------------------------------------------

# class A:
#     def count(self, word):
#         vowels = 'aeiou'
#         return sum(1 for letter in word.lower() if letter in vowels)


# class B:
#     def count(self, word):
#         consonants = 'bcdfghjklmnpqrstvwxyz'
#         return sum(1 for letter in word.lower() if letter in consonants)


# a_obj = A()
# b_obj = B()

# words = ['hello', 'world', 'python']

# results = [a_obj.count(word) + b_obj.count(word) for word in words]

# print(results)

#[-------------------------------------------------------------------------------


# from abc import ABC, abstractmethod

# class Planet(ABC):
#     def __init__(self):
#         self.orbit = 0

#     @abstractmethod
#     def get_age(self, earth_age):
#         pass


# class Mercury(Planet):
#     def __init__(self):
#         super().__init__()
#         self.orbit = 88

#     def get_age(self, earth_age):
#         mercury_age = earth_age / 365 / self.orbit
#         return mercury_age


# class Venus(Planet):
#     def __init__(self):
#         super().__init__()
#         self.orbit = 225

#     def get_age(self, earth_age):
#         venus_age = earth_age * self.orbit
#         return venus_age


# class Jupiter(Planet):
#     def __init__(self):
#         super().__init__()
#         self.orbit = 12

#     def get_age(self, earth_age):
#         jupiter_age = earth_age * self.orbit * 24
#         return jupiter_age


# earth_age = 20

# mercury = Mercury()
# venus = Venus()
# jupiter = Jupiter()

# mercury_age = mercury.get_age(earth_age)
# venus_age = venus.get_age(earth_age)
# jupiter_age = jupiter.get_age(earth_age)

# print(f"Your age on Mercury: {mercury_age:.2f} years")
# print(f"Your age on Venus: {venus_age:.2f} days")
# print(f"Your age on Jupiter: {jupiter_age:.2f} hours")

#---------------------------------------------------------------------------------------------

# class CustomNumber:
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         return self.value - other.value

#     def __sub__(self, other):
#         return self.value + other.value

#     def __mul__(self, other):
#         return self.value / other.value

#     def __truediv__(self, other):
#         return self.value * other.value

#     def __eq__(self, other):
#         return self.value != other.value

#     def __ne__(self, other):
#         return self.value == other.value

#     def __gt__(self, other):
#         return self.value < other.value

#     def __lt__(self, other):
#         return self.value > other.value

#     def __ge__(self, other):
#         return self.value <= other.value

#     def __le__(self, other):
#         return self.value >= other.value


# num1 = CustomNumber(10)
# num2 = CustomNumber(5)

# print(num1 + num2)  # 15
# print(num2 - num1)  # -5
# print(num1 * num2)  # 0.2
# print(num2 / num1)  # 0.5

# print(num1 == num2)  # False
# print(num1 != num2)  # True
# print(num1 > num2)   # True
# print(num1 < num2)   # False
# print(num1 >= num2)  # True
# print(num1 <= num2)  # False

























