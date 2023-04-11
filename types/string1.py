#  индексатсия в строке
 
# name = 'John'
        # j = 0 = -4
        # o = 1 = -3
        # h = 2 = -2
        # n = 3 = -1

# print(name)
# print(name[1])
# str1 = 'kani'
# print(str1[-1], str1[0])

# str1 = 'birthday'
# print(str1[5], str1[6], str1[7])
# print(str1[0], str1[1], str1[2], str1[3], str1[4])

# print(str1[1])

# print(str1[5] + str1[6] + str1[7])
# print(str1[0] + str1[1] + str1[2] + str1[3] + str1[4])

# срезы по индексам
# [start: end: <step>]

# str1 = 'birthday'
# print(str1[5:])
# print(str1[:5])

# from more_itertools import count_cycle


# text = "Hello world! My namr is John! I'm King of North!"
# print(text[:13])
# print(text[::5])

# print(text[::-1])

# Канкатенация строк (соединения)

# a = 'Hello'
# b = 'world'
# c = ' '
# print (a + c + b)

# экранированине строк - способ записи символов в строку, которые невозможно ввести с клавиатуры 

# \n -> перенос строки
# \t -> горизонтальная табуляция
# \v -> вертикальная табуляция
# \f -> перерводд страницы
# \r -> возврат укозателя

# print('\vHello \tworld!\nMy name is \fJohn Snow!')

# форматирование строк
# 1. с помощью %
# 2. с использованием .format()
# 3. Инерполяция строк (преобразование, f-stroki)

## %
# name = input('Vvedite imya:')
# last_name = input('Vvedite last_name:')
# # print('Добро пожаловать к нам ' +  name + ' ' + last_name + '!')
# print('Hello mr/mrs %s %s!' %(name, last_name))

# # .format
# name = input('Vvedite imya:')
# last_name = input('Vvedite last_name:')
# print('Приветсвую вас, {} {}, в наш клуб!'.format(name, last_name))

# f-sroki
# a = input('Enter mr/mrs:')
# name = input('Vvedite imya:')
# last_name = input('Vvedite last_name:')
# print(f'Hello{a} {name} {last_name}! Welcome to the parthy!')

# text = "Запомни Питтер, с большой силой приходит и большая отвественность."

# reversed_text = text[::-1]
# i = 0
# count_t = 0
# len_text = len(reversed_text)
# while i < len_text:
#     symbol = reversed_text[i]
#     if symbol == 'т'or symbol == 'Т':
#         count_t += 1
#     # print(symbol)
#     i += 1

# print(f'В тексте "т" встретилась {count_t} раз!')


















