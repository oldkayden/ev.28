# Декораторы - Это функция, которая позволяет без измение кода функции разширить ее функционал

# def decorator(func):
#     print(func)
#     func()

# def hello():
#     print('Hello stranger!')

# def john():
#     print('My name is John Snow! I\'m king of North!')

# decorator(hello)
# print('!!!!!')
# decorator(john)

# pythonic way -> @ синтакчисический сахар - красота кода


# def decorator(func):
#     def wrapper():
#         print(f'Вы вызвали функцию: {func.__name__}')
#         func()
#     return wrapper

# @decorator #@decorator -> decorator(hello)
# def hello():
#     print('Hello stranger!')



# @decorator
# def john():
#     print('My name is John Snow! I\'m king of North!')

# hello()
# john()

# def benchmark(func):
#     def wrapper(*args, **kwargs):
#         import time
#         start = time.time()
#         func(*args, **kwargs)
#         finish = time.time()
#         print(f'Время выполнения функции {func.__name__}, заняло: {finish - start}')
#     return wrapper

# @benchmark
# def loop():
#     i = 0
#     range_number = 1_000_000
#     while i < range_number:
#         i += 1


# @benchmark
# def add():
#     i = 0
#     range_number = 1_000_000
#     ls = []
#     while i < range_number:
#         ls.append(i)
#         i += 1
#     print(ls)

# loop()
# add()

# def bold(func):
#     def wrapper(*argc, **kwargs):
#         res = '<bold>' + func(*argc, **kwargs) + '<\bold>'
#         return res
#     return wrapper

# def div(func):
#     def wrapper(*argc, **kwargs):
#         res = '<div>' + func(*argc, **kwargs) + '<\div>'
#         return res
#     return wrapper

# @bold
# @div
# @bold
# def str_(name):
#     return name


# print(str_(' John Snow '))

#-------------------------------------------------------------------------------------------------------------------

# def trace(func):
#     def wrapper(*args, **kwargs):
#         print(f'Trace: вызвала {func.__name__}(), \nона принела args: {args}, kwargs: {kwargs}')
#         original_result = func(*args, **kwargs)
#         print(f'Trace: вызвала {func.__name__}( \nона вернула : {original_result})')
#         return original_result
#     return wrapper

# @trace
# def say(name, address):
#     return f'{name} --> {address}'

# @trace
# def hello(name, last_name, country):
#     return f'Hello {name} {last_name} from {country}!'

# say('Sherlock Holms', 'Bakery street 221B')
# print()
# hello('Homer', 'Simpson', 'Canada')


list1 = [11, 23, 45, 7, 9]
list2 = [21, 4, 16, 8, 10]
new_list = list1 + list2
print(new_list)









































