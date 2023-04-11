# str1 = 'Hello worold! My name is John, Last name is Snow. Nice to meet you!'
# def get_reversed_string(text):
#     # print(text[::1])
#     spisok = text.split()[::-1]
#     # print(spisok[::-1])
#     return ' '.join(spisok)


# print(get_reversed_string(str1))
    
# def sum_of_args(a, b, c=5, d=5):#параметры
#     return a + b + c + d

# result = sum_of_args(1,2,3,4)#  это аргументы 
# print(result)
# res = sum_of_args
# # print(res, type(res))
# print(res(5,6,7,8))
# print(sum_of_args(5,5))

#----------------------------------------------------------------------------------------------------------------------------
# позиционные и именнованые оргументы

# def printParams(a, b, c):
#     print(a, 'is stored in param a')
#     print(b, 'is stored in param b')
#     print(c, 'is stored in param c')
# # print(printParams(1,2,3))
# printParams(5, 10, 15)
# print()
# printParams(c=5, a=15, b=10)
# print()
# printParams(a=20, b=30, c=15)
    

  
# def sum_of_args(a, b, c, d):#параметры
#     return a + b + c + d

# print(sum_of_args(5, 10, 15, 20)) #arguments (позиционные аргументы )
# print(sum_of_args(a=5, c=20, b=10, d=15)) #keyword arguments(именнованные аргументы)
# print(sum_of_args(5, 10, d=15, c=20))

# -----------------------------------------------------------------------------------------------------------------------------------------

# оператор *

# a = [1,2,3]
# b = [4,5,6]
# c = [*a, *b]
# print(c)

#---------------------------------------------------------------------------------------------------------------------------------------------

# *args,  **kwargs в функциях

# def printScores(student, *scores):
#     print(f'Name of student: {student}')
#     # print(*args)#это тупль тип данных
#     print(f'AVG: {sum(scores) / len(scores)}')
#     for x in scores:
#         print('Score:', x)

# printScores('John Snow', 100, 90, 80, 95, 88)


# def printPetNames(owner, **kwargs): #{'kye': 'value'}
#     print(f'Owner name: {owner}')
#     # print(kwargs)
#     for kwargs, name in kwargs.items():
#         if type(name) == list:
#             print(f'{kwargs}:', *name)
#         else:
#             print(f'{kwargs}: {name}')

# printPetNames('John Snow', dog='Pluto', cat='Garfild', fish=['Nemo', 'Dori', 'Batya'], turtle='Leonardo')


# def get_some_data(a, b, *args, **kwargs):
#     print('параметры a и b:', a, b)
#     print('аргументы:', args)
#     print('именнное аргументы', kwargs )

# get_some_data(1,2,3,4,5, leng='Python', car='BMW')

#-----------------------------------------------------------------------

# def generate_rundom_string(len_):
#     import string as s
#     import random
#     # print(s.ascii_letters, s.digits,)
#     symbols = s.ascii_letters + s.digits
#     res =list(
#         random.choice(symbols) for i in range(0, len_)
#     ) + list(random.choice(s.punctuation))
#     random.shuffle(res)
#     return ''.join(res)

    
# print(generate_rundom_string(15))
# print(generate_rundom_string(20))
# print(generate_rundom_string(8))
# print(generate_rundom_string(8))


#-------------------------------------------------------------------------------------------------------------------------------------
# chek your self 4

# list_ = [1, 50]
# for x in range(1, 50):
#    if x % 2 == 1:
#       print(range)
      
# print(x)

# ls = list(range(1, 25))
# print(ls)
# for num in ls:
#     if num % 2 == 1:
#         print(num)


# ls = list(range(1, 50))
# # print(ls)
# for num in ls:
#     if num % 2 == 1:
#         print(num)  

# list_ = [x for x in range(1, 51) if x % 2 == 1]
# print(list_)


# list_ = [x ** 2 for x in range(1, 25) ]
# print(list_)


# try:
#     # код, который может вызвать исключение
# except [тип_исключения [as идентификатор]]:
#     # код, который выполняется, если произошло исключение типа тип_исключения
# else:
#     # код, который выполняется, если исключение не произошло
# finally:
#     # код, который выполняется в любом случае, независимо от того, было исключение или нет

# try:
#     num1 = int(input("Введите первое число: "))
#     num2 = int(input("Введите второе число: "))
#     result = num1 + num2
#     print(f"Сумма чисел {num1} и {num2} равна {result}")
# except ValueError:
#     print("Ошибка: введено некорректное значение. Введите число!")


# s = ['John', 'Ono', ' kazak', 'peter', 'dovod', 'radar', 'apa', 'piko']
# def is_palindrome(s):
   
#     s = s.replace(" ", "").lower()
   
#     return s == s[::-1]
# polindrom_words = is_palindrome(s)
# print(polindrom_words)


# word = ['John', 'Ono', ' kazak', 'peter', 'dovod', 'radar', 'apa', 'piko']
# def is_palindrome(word):
#     # приводим строку к нижнему регистру и удаляем пробелы
#     word = word.lower().replace(" ", "")
#     # сравниваем строку с ее перевернутой версией
#     return word == word[::-1]
# print('True or Falce')












