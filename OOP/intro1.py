# ООП - обьектно - ориентированное программирование 

# Класс - это описание того, как должен выглядеть обьект, то есть в классемы описываем какими свойствоми (данным) и поведением(функции) должен обладать объект

# Объект - это сущность которую мы создаем от класса у объекта есть сопственные состояние свойств(данные)

#  Целью создание было связать данные с функциями которые управляли этими данными

# Свойствами(атрибутами) - называют обычные переменные внутри класса, в которых хранятся данные объекта

# Методы это обычные функции внутри класса, методы описывают поведение объектa
# -----------------------------------------------------------------------------------------------------------------------------------

# class Human:
#     age = 0

#     def __init__(self, first_name, last_name, job, citizenship):
#         self.name = first_name + ' ' + last_name
#         self.job = job
#         self.citizenship = citizenship

#     def show_info(self):
#         return f'Name: {self.name}, Age: {self.age}, Job: {self.job}, Citizen: {self.citizenship}'        

# john = Human('Jhon', 'Snow', 'King of North', 'Northerner')
# bilal = Human('Bilal', 'Lanister', 'Programmist', 'KR')


# print(john, type(john))
# print(dir(john))
# print(john.show_info())
# john.age = 24
# print(john.show_info())
# john.job = 'King of Westeros'
# print(john.show_info())
# print()
# print(bilal.show_info())

#-----------------------------------------------------------------------------------------------------
# class Dog:
#     #атрибуты класса 
#     age = 0 
#     ushi = True

#     def __init__(self, name: str, color: str) -> None:
#         "Инициализатор, имеено здесь создаются аттрибуты объекта"
#         #self - ссылка на объект который только создался
#         self.name = name
#         self.color = color

#     def bark(self):
#         print(f'{self.name} пиздит!')

#     def show_info(self):
#         print(f'Name: {self.name}, Age: {self.age}, Color: {self.color}, Ushi: {self.ushi}')

# rex = Dog('Rex', 'black')
# pluto = Dog('Pluto', 'brown')
# aktosh = Dog('Aktosh', 'gray')

# rex.show_info()
# pluto.show_info()
# aktosh.show_info()

# print()

# rex.age = 2
# pluto.age = 5
# aktosh.age = 3
# aktosh.ushi = False


# rex.show_info()
# pluto.show_info()
# aktosh.show_info()

# print()

# rex.bark()
# pluto.bark()

#--------------------------------------------------------------------------------------------

# class Human:
#     def __init__(self):
#         print('init worked!')
#         self.raychel = 'raychel'
#         self.golod = 100

#     def eat(self, meal, doela=True):
#         print(f'{self.raychel} покушала {meal}')
#         if doela:
#             self.golod -= 50
#         else:
#             self.golod -= 25

# obj = Human()
# print(obj.raychel, obj.golod)
# obj.eat('burger', doela=False)
# print(obj.raychel, obj.golod)
# obj.eat('Kruasan')
# print(obj.raychel, obj.golod)













