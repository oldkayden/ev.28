# list() -> (списки, массив) - это у нас изменяемый, последовательный тип данных, который предстовляет из себя колекцию каких либо объектов(значения).

# my_list = [1, 'string', False, None, [1,2,3,4,5,]]
# print(my_list, type(my_list))

# range() -> она возврощяет последовательность элементов(чисель)
# ls = range(1,101)
# my_list = list(ls)
# print(my_list)

# my_list = list('Hello world')
# print(my_list)

# tuple_ = ('banana', 'apple','cherry')
# print(tuple_, type(tuple_))
# ls = list(tuple_)
# print(ls, type(ls))

# Индексатсия в списках 

# ls = [1, 2, 3, 4, 5, 'string', [True, False, None]]
# print(ls, len(ls))
# print(ls[1], ls[2])
# print(ls[4:])




# ls = [1, 2, 3, 4, 5, 'string', [True, False, None], 4, 5, 6]
# print(ls[6][:2])

# ls = list(range(1, 11))
# print(ls)
# for num in ls:
#     print(num)

# ls = ['John', 'Sansa', 'Tririon', 'Eddart', 'Serseya', 'Jamie']
# print(ls, len(ls))
# for x in ls:
#     print(f'Hello mr/mrs {x}! Welcome to the clup baby!')
#     print('1')

# # print(2)

# ls = list(range(1, 21))
# print(ls)
# for num in ls:
#     if num % 2 == 0:
#         print(f'число четное{num}, квадрат: {num**2}')
#     else:
#         print(f'Число нечетное{num}, куб: {num**3}')

# -----------------------------------------------------------------------------------------------------------------------------------------

# методы списков
# print(dir([]))
# append(element) - Добавляет элементов в конце списка

# ls = [1, 2, 3]
# print(ls)
# ls.append(4)
# ls.append(5)
# ls.append([True, False])
# ls.append('Hello')
# print(ls)

# extend(object) - расширяет список
# ls = [1,2,3]
# ls.append('Hello')
# print(ls)
# ls.extend('Hello')
# print(ls)


# ls = [1,2,3]
# ls1 = [4,5,6]
# print(ls + ls1)

# sort() - сортирует список, если передать reversed=True, то список отсортируется в убывающейм порядке

# from random import randint

# ls = []
# for x in range(0, 100):
#     num = randint(0, 1000)
#     ls.append(num)

# print(ls)
# ls.sort()
# print('After:')
# # print(ls)

# ls = ['John', 'Deyneris', 'Tirion', 'Aizirek', 'azalia']
# ls.sort(key=len, reverse=True)
# print(ls)

# insert(index, element)  - добовляет элемент по указанному index

# ls = ['string', 2, 3, False]
# ls.insert(1, 1)
# print(ls)

# remove(element) - удаляет element  из списска, если токого нет, то выводится ошибка!

#  pop([index]) - удаляет и возврощяет элемент из списка по index, но если index не передать, то удаляет последний элемент.

# ls = [5, 1, 2, 4, 4, 5, 5, 5]
# ls.remove(5, 3)
# print(ls)
# # print(5 in ls)


# while 5 in ls:
#     ls.remove(5)

# print(ls)


# ls = [5, 1, 2, 3,  4, 5, 5]
# # print(ls.pop(0))
# # print(ls.remove(5))
# deleted = ls.pop()
# print(ls)
# print(deleted)

# update----------------------------------------------

# ls = [1, 'h', 3]
# print(ls)
# ls[1] = 2 
# print(ls)
# ls.reverse()
# print(ls)
# print(ls[::-1])


# pizza =['first_item', 'second_item', 'third_item', 'fourth_item', 'fifth_item', 'sixth_item']
# spisok = []

# for x in pizza:
#     if not x.startswith('f'):
#         spisok.append(x)

# print(spisok)











