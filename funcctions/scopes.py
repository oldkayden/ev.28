# область видемости и пространство имен (scopes)
#  это технология определяет контекст имени (переменные), в рамках котоого мы модем ее использовать 

# built-ins(встроенная область видимости) -> print, len, max,
# global(Глобальная)-> область одного файла
# enclosed(не локальная либо же (амкнутая), nonlocal)
# local(локальная) -> область внутри одно функции 


# x = 200

# def myFunc():
#     print(x)
#     a = 300
#     print(a)


# myFunc()
# print(x)
# print(a)

# a = 10 #глобальная 
# print #built-in

# def hello(): #имя глобальная 
#     a = 'Hello world' # local
#     print(a, 'Local inside in func!')

# hello()
# print(a, 'global')

# LEGB -local enclosed global built-in

#-----------------------------------------------------------------------------

# Enclosed
# # замкнутое пространство имен - локальное пространство,  у котороого есть врутренее локальное пространство


# x = 'global'
# print(x, '1') #global

# def enclosed(): #global
#     x = 'enclosed'
#     def local(): #local
#         x = 'local'
#         print(x, '3')
#     print(x, '2')
#     local()
#     print(x, '4')

# enclosed()
# print(x, '5')


# a = 5

# def func():
#     print(a) #5
#     a = a +1

# func()


# global -> позволяет изменять занчение глобально переменной находясь внутри локальной области

# nonlocal -> позволяет изменять значение на локальной (замкнутой) переменной находясь внутри локальной области

# var = 100


# def increment(): #LEGB
#     global var
#     var += 1 #var = var + 1

# # print(var) # 100
# increment()
# print(var) # 101

# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# print(counter())




# c = counter() 
# # print(c) #<function counter.<locals>.increment at 0x7f87ea726050>
# print(c()) #1
# print(c()) #2
# print(c()) #3
# print(c()) #4
# print(c()) #5
# print(c()) #6

# print(dir(__builtins__))
# print(len(dir(__builtins__)))


# globals - func которая возврощяет все имена внутри глобальной области видимости

#locals - функция еоторая возврощяет все имнеа внутри глобальной области видимости и локальной



# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# def showStats(hereos, mobs):
#     print()
#     print(f'John Snow ты убил \n\tгероев: {hereos}  \n\tмобов: {mobs}')
#     print()

# counter_heroes = counter()
# counter_mobs = counter()
# heroes = 0
# mobs = 0
# print('Приветствую вас, King John Snow!')

# while True:
#     print('Тебе доступны следующее действие: ')
#     print('1-убить героя, 2-убить моба, 3-посмотреть статистика, 4-выйти из игры,')    
#     choice = input('Введите что хотите сделать!: ').strip()
#     if choice == '1':
#         heroes=counter_heroes()
#         print('John  вы обезглавили Ланистера!')
#     elif choice == '2':
#         mobs=counter_mobs()
#         print('Вы убили Белого ходока!')
#     elif choice == '3':
#         showStats(heroes, mobs)
#     elif choice == '4':
#         print('Пока пока! Ждем еще раз!')
#         break
# print()
























