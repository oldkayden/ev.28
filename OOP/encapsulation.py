#Инкапсуляция:
# 1. Языковая конструкция, которая помогает связать данные с методами для их оброботки и управления (связь между данными и методами которые управляют ими)(класс - капсула)
# 2. Механизм сокрытия, при помощи которого можно ограничить доступ одного компанента программы к другому.

# Инкапсуляция как связь

# class Phone:
#     number = '+996700471376'



#     def print_number(self):
#         print(f'Мой номер:{Phone.number}')
#         print(f'Мой номер:{self.number}')


# my_phone = Phone()
# my_phone.print_number()

# Инкапсулация как механизм сорытия
# 3 уровня сакрытия данных в питоне
#     1. Публичный(pablic) - number, print_number
#     2. Защищенный(_protected) - _number
#     3. Приватный (__private) - __number

# class Car:
#     _country = 'Germany'
#     __motor = 'ABC'

#     def __init__(self) -> None:
#         self.marka = 'Emmir-Benz' #public
#         self._model = 'w140' #protected
#         self.__color = 'gray' #private

# obj = Car()
# print(dir(obj))
# print(obj._Car__color)
# print(obj._country)
# print(obj._model)


# class Phone:
#     username = 'John'
#     _caller = 'Jamie'
#     __count_of_cals = 15

#     def call(self):
#         print(f'{self._caller} Звонит вам!')
#         question = input('Взять трубку(yes/no): ')
#         if question.lower().strip() == 'yes':
#             self.__turn_on()
#         else:
#             print('Сбросили трубку!')
        


#     def __increment_calls(self):
#         self.__count_of_cals += 1

#     def __turn_on(self):
#         self.__increment_calls()
#         print('Hello!')
#         print(f'Count of calls with Jamie {self._caller}: {self.__count_of_cals}')

# john = Phone()
# print(john.username)
# john.call()
# john.call()
# john.call()
# john.call()

#------------------------------------------------------------------------------------------------------------------------

# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def display_info(self):
#         print(f'My name is {self.name} and I\'m {self.age} year old!')

# obj = Person('John', 18)
# obj.display_info()
# obj.nationality = 'Kyrgyz'
# print(obj.nationality)
# obj.age = -18
# obj.name = 55
# obj.display_info()

#--------------------------------------------------------------------------------------------------------

# getter & setter
# они нужны чтобы избежать прямого обращения к сокрытым атрибутам при этои можно добавить логику валидация (проверки) данных котрые будут установлены в атрибут

# class Person:
#     def __init__(self, name, age) -> None:
#         self.__name = name
#         self.__age = age

#     def display_info(self):
#         print(f'My name is {self.__name} and I\'m {self.__age} year old!')

#     #getter
#     def name(self):
#         return self.__name

#     # setter
#     def set_name(self, name):
#         if not isinstance(name, str):
#             print('Name must be str object!')
#         else:
#             self.__name = name



#     def age(self):
#         return self.__age

#     # setter
#     def set_age(self, age):
#         if not isinstance(age, int) or not 0 <= age < 150:
#             print('Name must be str object!')
#         else:
#             self.__age = age
            
# obj = Person('john', 24)
# print(obj.name())
# obj.set_age(-18)
# obj.display_info()
# obj.set_name(55)

