"""
встроенные функции 
"""
"""
Анонимные функции - lambda (Обычная функция с одной особенностью, у нее нет имени)
Принимает сколько угодно параметров, но всегда возврощяет одно выражение
"""

# def hello():
#     return 'hello'
# print(hello())

# x = lambda: 'hello'
# print(x())

# x = lambda a, b, c: (a * b) % c
# print(x(5, 5, 5))

# x = lambda num1, num2, degree=None: (num1 * num2) ** degree if degree else num1 * num2 
# print(x(2, 2, 3))
# print(x(5, 5))

# def myFunc(n):
#     return lambda num: num * n

# my_doubler = myFunc(2)
# print(my_doubler(50))

# list_ = ['hello', 'mil', 'john', 'daniel', 'vlad']
# a = sorted(list_, key=len, reverse=True)
# print(a)

# dict_ = {
#     'john': 500,
#     'tirion': 160_000,
#     'tom': 150,
#     'sanchar': 20,
#     'ayana': 100_000,
# }
# print(dict_.items())
# new_dict = dict(sorted(dict_.items(), key=lambda x: x [1], reverse=True))
# print(new_dict)

"""
map(function, iterable) - применяет к каждому элементу внутри iterable функцию,
 которая мы ей передаем в function, 
закидывая в результат те данные, которые возврощает функции. 
В результате мы получаем mapobject(iterator), в котором хранятся все наши данные.
"""

# ls = ['one', 'two', 'three', 'four']

# new_list = list(map(lambda x: x.capitalize(), ls))
# print(new_list)


# ls = ['1', '2', '3']

# new_list = list(map(int, ls))
# print(new_list)


# names = ['john', 'aria', 'baku', 'bakberdi', 'lilo']

# new_list = list(map(lambda x: f'Hello mr\mrs {x}', names))
# print(new_list)


'''
Функция высшего порядка - функция, 
принемает в качестве аргумента другую функцию
'''
'''
filter(function, iterable) - принемает ко всем элементам iterable функции, 
которую мы передали и возврощаем filterobject(итератор) только с теми элементами, 
для которых функция вернула True
'''

# ls = ['one', 'lili', 'oleg', 'billi', 'tirion']
# res = list(filter(lambda x: len(x) > 4, ls))
# print(res)

'''
enumerate(iterable) - пронумеровывает каждый элемент внутри iterable ее собственным индексом 
'''

# ls = ['str1', 'str2', 'str3']
# new_list = list(enumerate(ls))
# print(new_list)

# def calculate_virus_cells(hours):
#     bact_per_min = 4
#     time_to_combine = 100 / bact_per_min
#     virus_cells_per_combine = 1
#     virus_cells = 1
#     for i in range(60 * hours):
#         new_bacteria = bact_per_min * virus_cells
#         if new_bacteria >= 100:
#             virus_cells += new_bacteria // 100
#             new_bacteria %= 100
#             virus_cells *= virus_cells_per_combine
#         virus_cells_per_combine += 1
#     return virus_cells
# зк

# def calculate_virus_cells(hours):
#     bact_per_min = 4
#     time_to_combine = 100 / bact_per_min
#     virus_cells_per_combine = 1
#     virus_cells = 1
#     for i in range(60 * hours):
#         new_bacteria = bact_per_min * virus_cells
#         if new_bacteria >= 100:
#             virus_cells += new_bacteria // 100
#             new_bacteria %= 100
#             virus_cells *= virus_cells_per_combine
#         virus_cells_per_combine += 1
#     return virus_cells

# print(calculate_virus_cells(60)) # выведет 144

#------------------------------------------------------------------

# ls = [1, 2, 3, 4, 5]
# new_list = list(map(lambda x: x * 82 if x % 2 == 0 else x, ls))
# print(new_list)



# from typing import List

# class Solution:
#     def separateDigits(self, nums: List[int]) -> List[int]:
#         result = []
#         for num in nums:
#             digits = []
#             while num > 0:
#                 digits.append(num % 10)
#                 num //= 10
#             result.append(digits[::-1])
#         return result




class Alphabet:
    def __init__(self):
        self.a = 'QWERTY'
        self.c = 'ASDF'
        print(self.__c)
obj = Alphabet()
print(obj.a)

















