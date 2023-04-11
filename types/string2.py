# print(dir("5"))
# print(dir(int))

# a = "Hello"
# b = "John"

# # print(a !=b)
# # print("abc" == "abc")

# print(a > b)
# print(a < b)

# print('a')  #97 ->1100001
# print('a' > 'b') #97 > 98 
# print('h' > 'c')  # 104 > 99

# print('hello' > 'harry') #true

# print('abc' > 'abc') #false

# len - возврощяет количество символов в строке

# a = 'Hello'
# b = 'john snow'
# print(len(a) < len(b))
# print(len(a), len(b))

# Методы строк
# replace(old, new, [count]) -  меняет в строке символы  old  на new, если вы укажите count, то заменяет  count раз

# text = 'ha ha ha ha'
# result = text.replace('a', 'e', 2)
# print(text)
# print(f'result after replace: {result}')

# str1 = 'Hello world! My name is John Snow!'
# res = str1.replace('John Snow', 'Tirion Lanister')
# print(res)

# strip() -  он уберает пробельные символы в начале и в конце строки 
# rstrip, lstrip

# a = '   Hello   '
# print(len(a))
# print(a)
# res = a.strip()
# print(res)
# print(len(res))
 
# print(dir(str))


# isdigit - ->      Проверяют
# isnumeric- ->     состоит ли наша строка
# isdecimal - ->    полностью из чисел

# num = input('Vvedite chislo:')
# print(f'Vvedino chislo?: {num.isdigit()}')

# num = input('Vvedite chislo:')
# if num.isdigit():
#     num = int(num)
#     print(f'{num} + 5 = {num + 5}')
# else:
#     print('Vy vveli ne chisla!')

# text ='\u0031'
# print(text)
# print(text.isnumeric())
# print(text.isdigit())
# print(text.isdecimal())

# isalnum() ->  проверяет состоит ли наша строка из числ и символов латиинского и киррилицы

# str1 = '56a'
# print(str1.isalnum())

# str2 = '56_a'
# print(str2.isalnum())

# isalpha ->  состоит ли наша строка полностью из символов алфавита

# text = 'Hello world'
# res = text.replace(' ', '')
# print(res)
# print(res.isalpha())


# # islower()
# # isupper()
# # istitle()
# str1 = 'IS'
# print(str1.isupper())



# index(value, [start], [end]) - выводит индекс знвчения  value  которые мы передаем, в нашей строке.



# text = 'Hello john snow'
# print(text.index('john'))

# text = 'Hello world! My name is john Snow!'

# print(text.index('o'))

# res = text.index('o')
# print(res)
# res = text.index('o', res + 1)
# print(res)
# res = text.index('o', res + 1)
# print(res)
# res = text.index('o', res + 1)
# print(res)

# count(value) - считают количество свохждений value в нашем строку

# text = 'hello o o o hello'
# print(text.count('o'))
# print(text.count('hello'))

# split(separator) - дробит нашу строку на несколько частей по разделу, все части строк сохроняются типе  list 

# text = 'let me speak by my hearth in English! Cause my name is John Snow'

# res = text.split(' ')
# print(res)
# print(len(res))


# a = 'hello#hello#hello#hello'
# res = a.split('#')
# print(res)

# 'connector'.join(list) -> соединяет по connector строки которые находились в list

# text = 'let me speak by my hearth in English! Cause my name is John Snow'
# res = text.split(' ')
# print(res)
# str1 = '~'.join(res)
# print(str1)

# find(value, [start], [end]) - делает тоже самое что и index,  но если не нашел то вернется -1

# text = 'Hello '
# print(text.find('l'))
# print(text.find('lk'), type(text.find('lytui')))

# swapcase() -  переводится все символы в противополжный регистр
# upper() - переводит все в верхний
# lower() - переводит все в нижний регистр

# text = 'Hello WorLD, JOHN snow'
# print(text.upper())
# print(text.lower())
# print(text.swapcase())

# capitalize() - переводит самый первый символ в верхний регистр
# title()- переводит первые символы всех слов в верхний регистр

# name = input('Vvedite imya:').capitalize()
# print(name)
# print(f'Hello! Mr/Mrs {name}!')

# fio = 'john edart snow'
# print(fio.title())

#  методы в пайтен

# print(dir(str))



    














