#принципы ООП:
#1. Наследование
#2. Инкапсуляция
#3. Полиморфизм

#4. Абсьракция
#5. композиции
#6. Агрегация

#-------------------------------------------------------------

# Наследование
# Позволяет принимать родительские методы и атребуты дочернему лассу

#Родительский класс
#Дочерский класс

 #-----------------------------------------------------------------

# class Animal:
#     def print_info(self):
#         print('I\'m an animal')

# class Lion(Animal):
#     pass

# class Dog(Animal):
#     pass


# lion = Lion()
# lion.print_info()
# # print(dir(Animal)

# #-----------------------------------------------------------------------------------------------------------------------------

# class Animal:
#     def say(self):
#         print(f'This animal name is: {self.name}: {self.golod}')

#     def eat(self):
#         print(f'{self.name} eats: {self.meal}')

# class Lion(Animal):
#     name = 'lion'
#     golod = 'roar'
#     meal = 'meat'
#     griva = True

#     def info(self):
#         print(f'{self.name} griva: {self.griva}')

# class Dog(Animal):
#     name = 'dog'
#     golod = 'bark'
#     meal = 'meat'

# class Koala(Animal):
#     name = 'koala'
#     golod = 'roar'
#     meal = 'erkalif'

# rex = Dog()
# simba = Lion()
# julian = Koala()

# rex.say()
# rex.eat()
# print()
# simba.say()
# simba.eat()
# simba.info()
# print()
# julian.say()
# julian.eat()
  
#---------------------------------------------------------------------------------------------------------------------

# class Person:
#     def info(self):
#         print('I\'m person from Bishkek')

# class Student(Person):
#     def info(self):
#         super().info()
#         print('I\'m study at Manas University')

# obj = Student()
# obj.info()

#--------------------------------------------------------------------------------------------------------------------------

# class Laptop:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price

#     def get_info(self):
#         return {'brand': self.brand, 'model': self.model, 'price': self.price}
    
# class Acer(Laptop):
#     def __init__(self, model, price, year, videocard):
#         super().__init__('Acer', model, price)
#         self.year = year
#         self.video = videocard

#     def get_info(self):
#         repr = super().get_info()
#         repr['year'] = self.year
#         repr['videocard'] = self.video
#         return repr
    
# class Apple(Laptop):
#     def __init__(self, model, price, display, year):
#         super().__init__('Macbook', model, price)
#         self.display = display
#         self.year = year

#     def get_info(self):
#         repr = super().get_info()
#         repr['year'] = self.year
#         repr['videocard'] = self.display
#         return repr

# mac = Apple('Pro', 1500, 14, 2020)
# print(mac.get_info())

# acer = Acer('Pac', 600, 2019, 'Nvidia')
# print(acer.get_info())

#-------------------------------------------------------------------

# class Employee:
#     bonus = 1.5

#     def __init__(self, first_name, last_name, salary ):
#         self.name = f'{first_name} {last_name}'
#         self.salary = salary
        
#     def get_info(self):
#         return f'FIO: {self.name}, Salary: {self.salary}'
    
#     def give_increase(self):
#         self.salary *= self.bonus # salary = salary * bonus

#     def __str__(self) -> str:
#         return self.get_info()
    
# class Developer(Employee):
#     def __init__(self, first_name, last_name, salary, language):
#         super().__init__(first_name, last_name, salary)
#         self.lang = language

#     def get_info(self):
#         info = super().get_info()
#         info += f'Prog Language: {self.lang}'
#         return info

# class Manager(Employee):
#     def __init__(self, first_name, last_name, salary, devs=[]):
#         super().__init__(first_name, last_name, salary)
#         self.devs = devs

#     def add_devs(self, developer):
#         self.devs.append(developer)

#     def show_devs(self):
#         return [x for x in self.devs]
    
# dev1 = Developer('John', 'Snow', 1500, 'Python')    
# dev2 = Developer('Steve', 'Jobs', 3000, 'C++')    
# dev3 = Developer('Lary', 'Page', 1000, 'JS')    
# dev4 = Developer('Tirion', 'Lanistar', 2000, 'Emmir')

# man1 = Manager('Jamie', 'Lanistar', 4000, [dev2, dev1])
# man2 = Manager('william', 'Kan', 1500)

# print(f'Manager {man1.get_info()}, has {man1.show_devs()} developers!')
# print(f'Manager {man2.get_info()}, has {man2.show_devs()} developers!')

# man1.add_devs(dev3)
# man2.add_devs(dev3)
# man2.add_devs(dev4)

# dev3.give_increase()
# dev4.give_increase()
# man2.give_increase()

# print('After:')
# print(f'Manager {man1.get_info()}, has {man1.show_devs()} developers!')
# print(f'Manager {man2.get_info()}, has {man2.show_devs()} developers!')
