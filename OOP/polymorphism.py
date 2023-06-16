# Функция полиморфизм -> len(): __len__

# print(len('Makers'))
# print(len([1,2,3,4]))
# print(len({1:2,2:4, 5:6}))

# + (__add__) - метод полиморфизм

# print(5 + 5)
# print('hello' + 'hello')
# print([1,2,3] + [4,5,6])

# Полиморфизм - это способность функции(метода) использоваться для разных типов(классов)
# Широко распространенное определение: 'Один интерфейс и много реализаций'

# list.pop
# set.pop
# dict.pop


# class Cat:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
        
#     def info(self):
#         print(f'Its\' a cat. Cats name is {self.name}, age: {self.age}')
        
#     def make_sound(self):
#         print('Meow, meow!')
        
# class Dog:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
        
#     def info(self):
#         print(f'Its\' a dog. Dogs name is {self.name}, age: {self.age}')
        
#     def make_sound(self):
#         print('Bark, bark!')

# cat = Cat('Garfild', 5)
# dog = Dog('Plutto', 6)

# for obj in (cat, dog):
#     obj.info()
#     obj.make_sound()


# from math import pi


# class Shape:
#     def __init__(self, name) -> None:
#         self.name = name
        
#     def area(self):
#         pass

#     def fact(self):
#         return f'Я фигура в двумерной плоскости: {self.name}!'

# class Square(Shape):
#     def __init__(self, length) -> None:
#         super().__init__('Квадрат')
#         self.length = length
        
#     def area(self):
#         return self.length ** 2
    
#     def fact(self):
#         return super().fact() + '\n У квадрата все стороны равны и углы равны 90 градусам!'
    
# class Circle(Shape):
#     def __init__(self, radius) -> None:
#         super().__init__('Окружность')
#         self.radius = radius
        
#     def area(self):
#         return pi * (self.radius ** 2)
    

# a = Square(8)
# b = Circle(4)

# print(a.fact())
# print(a.area())

# print(b.fact())
# print(b.area())
# Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
# батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 % заряда при каждом обращении.
# Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность заряжания батареи.

# import time
# import os
# from math import floor
# from progress.bar import IncrementalBar


# class Phone:
#     __imei = None
#     __battery = 100
#     __description = None
    
#     def __check_level_of_battery(self):
#         if not self.__battery:
#             raise ValueError('Phone is low!')
    
#     def __subtraction_battery(self):
#         self.__check_level_of_battery()
#         self.__battery -= 0.5

#     def listen_music(self):
#         self.__check_level_of_battery()
#         if self.__battery < 5:
#             raise ValueError('Phone is low!')
        
#         self.__battery -= 5
#         return 'User is listening misic!'

#     def watch_video(self):
#         self.__check_level_of_battery()
#         if self.__battery < 10:
#             return 'You can\'n watch video, because the charge level is less than 10'
#         self.__battery -= 7
#         return 'User is watching video!'
    
#     def сharge_battery(self):
#         try:
#             i = 0
#             bar = IncrementalBar('Charging...', suffix='%(percent)d%%', index = self.__battery, max=100)
#             self.__battery = floor(self.__battery)
#             while self.__battery < 100:
#                 os.system('cls||clear')
#                 print('\nTo stop charging, press Ctrl+C\n')
#                 bar.next()
#                 time.sleep(4)
#                 self.__battery += 1
#                 i += 1
#         except KeyboardInterrupt:
#             return f'\n\nThe phone was charged for {i}%. Current battery status {self.__battery}%'
#         else:
#             return f'Phone is fully charged {self.__battery}%'
#         finally:
#             bar.finish()
             
#     def get_imei(self):
#         self.__subtraction_battery()
#         return self.__imei
    
#     def set_imei(self, imei):
#         self.__subtraction_battery()
#         self.__imei = imei
        
#     def get_battery(self):
#         self.__subtraction_battery()
#         return self.__battery
    
#     def set_battery(self, battery):
#         if battery > 100 and battery < 0:
#             raise 'Value Error'
#         self.__subtraction_battery()
#         self.__battery = battery

#     def get_desc(self):
#         self.__subtraction_battery()
#         return self.__description
    
#     def set_desc(self, desc):
#         self.__subtraction_battery()
#         self.__description = desc
    

# def main():
#     phone = Phone()
    
#     while True:
#         os.system('cls||clear')
#         print('Menu:')
#         print('  (1) - Get imei code\n  (2) - Set imei code\n  (3) - Get battery level\n  (4) - Set battery level\n  (5) - Get description\n  (6) - Set description\n  (7) - Listen music\n  (8) - Watch video\n  (9) - Charge battery\n  (0) - Exit')
#         choice = input('Enter your choice: ')
#         print()
        
#         if choice == '1':
#             print(f'Imei code: {phone.get_imei()}')
#             input('Press on anything to continue...')
#         elif choice == '2':
#             imei = input('Enter imei code:' )
#             phone.set_imei(imei)
#         elif choice == '3':
#             print(f'Battery level: {phone.get_battery()}')
#             input('Press on anything to continue...')
#         elif choice == '4':
#             battery = int(input('Enter battery level:' ))
#             phone.set_battery(battery)
#         elif choice == '5':
#             print(f'Description: {phone.get_desc()}')
#             input('Press on anything to continue...')
#         elif choice == '6':
#             desc = input('Enter description:' )
#             phone.set_desc(desc)
#         elif choice == '7':
#             print(phone.listen_music())
#             input('Press on anything to continue...')
#         elif choice == '8':
#             print(phone.watch_video())
#             input('Press on anything to continue...')
#         elif choice == '9':
#             print(phone.сharge_battery())
#             input('Press on anything to continue...')
#         elif choice == '0':
#             print('Good Bye!')
#             break
        
# if __name__ == '__main__':
#     main()