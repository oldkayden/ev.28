# 1) Создайте класс MyString, который будет наследоваться от str.
# Определите 2 своих метода:
# append, который будет принимать строку и добавлять её в конец исходной
# pop, который удаляет из строки последний элемент и возвращает его.
# Пример:
# example = MyString('String')
# example.append('hello')
# print(example) -> 'Stringhello'
# print(example.pop()) -> 'o'
# print(example) -> 'Stringhell'

class MyString(str):
    def append(self, string):
        self = (self + string)

    def pop(self):
        popped = self[-1]
        self = self[:-1]
        return popped

example = MyString('String')
example.append('hello')
print(example) #-> 'Stringhello'
print(example.pop()) #-> 'o'
print(example) #-> 'Stringhell'

# Велосипед.
# Создайте класс Bike в котором будут инициализированы следующие атрибуты: self.cost
# (стоимость)
# self.make (производитель)
# self.model (модель)
# self.year (год выпуска)
# self.condition (состояние)
# self._sale_price = None (цена для продажи, по умолчанию None)
# self.sold = False (продан или нет, по умолчания False)
# Также укажите мин. прибыль, которая должна прийти с продажи велосипеда. Создайте метод
# для указания цены для продажи, который принимает цену и если она меньше стоимости, то
# ставит дефолтную цену для продажи (стоимость + мин. прибыль).
# Для ремонта велосипеда будет использоваться метод service, которая принимает стоимость
# ремонта и новое состояние велосипеда, соответственно продажная цена велосипеда
# возрастает на столько, сколько обошелся ремонт и возвращает нынешнюю цену для продажи.
# При продаже велосипеда будет использоваться метод sell, который меняет значение self.sold на

# True и возвращает прибыль с продажи.
# Допишите метод get_default_bike, который будет создавать дефолтный велосипед. Создайте
# объект bike = Bike.get_default_bike() и используете его методы и получите значения всех его
# атрибутов.


# class Bike:
#     min_profit = 100 

#     def __init__(self, cost, make, model, year, condition):
#         self.cost = cost
#         self.make = make
#         self.model = model
#         self.year = year
#         self.condition = condition
#         self._sale_price = None
#         self.sold = False

#     def set_sale_price(self, price):
#         if price < self.cost:
#             self._sale_price = self.cost + self.min_profit
#         else:
#             self._sale_price = price

#     def service(self, repair_cost, new_condition):
#         self._sale_price += repair_cost
#         self.condition = new_condition
#         return self._sale_price

#     def sell(self):
#         self.sold = True
#         return self._sale_price - self.cost

#     @classmethod
#     def get_default_bike(cls):
#         return cls(500, "Brand", "Model X", 2022, "Excellent")


# bike = Bike.get_default_bike()

# bike.set_sale_price(700)
# current_price = bike.service(50, "Good")
# profit = bike.sell()

# cost = bike.cost
# make = bike.make
# model = bike.model
# year = bike.year
# condition = bike.condition
# sale_price = bike._sale_price
# sold = bike.sold

# print("Cost:", cost)
# print("Make:", make)
# print("Model:", model)
# print("Year:", year)
# print("Condition:", condition)
# print("Sale Price:", sale_price)
# print("Sold:", sold)
# print("Current Price:", current_price)
# print("Profit:", profit)

