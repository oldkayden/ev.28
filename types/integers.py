# # # # # # # # # Типы данных числа -> int, float

# # # # # # # # # = ->  оператор присваивания
# # # # # # # # # variable(переменная)
# # # # # # # # # num = 5 
# # # # # # # # # print(num) # 5
# # # # # # # # # num = 79 # переопределенние 
# # # # # # # # # print(num) #79

# # # # # # # # # abc -> нижний регистр 
# # # # # # # # # ABC -> верхний регистр 

# # # # # # # # # PEP8
# # # # # # # # # tomorrow_day = '10.03.2023' # Snake case
# # # # # # # # # tomorrowDay = '10.03.2023' # Camel case

# # # # # # # # # num1 = 5
# # # # # # # # # num2 = 15
# # # # # # # # # num3 = 10
# # # # # # # # # result = num1 + num2 - num3
# # # # # # # # # print('Summa:', result)

# # # # # # # # # num1 = input('Enter the num1:')
# # # # # # # # # num2 = input('Enter the num2:')
# # # # # # # # # num1 = int(num1)
# # # # # # # # # num2 = int(num2)
# # # # # # # # # print(num2,'*', num1, '=', num2 * num1)

# # # # # # # # # num1 = int(input('Enter the num1:'))
# # # # # # # # # num2 = int(input('Enter the num2:'))
# # # # # # # # # print(num1,'/5', num2, '=', num1 / num2)

# # # # # # # # #  / and // and %
# # # # # # # # #  / -  обычное деление 
# # # # # # # # #  // - деление без остатка
# # # # # # # # #  % -  модульное деление(получение осттатка от деления)

# # # # # # # # # num1 =7
# # # # # # # # # num2 = 3
# # # # # # # # # print('/', num1 / num2)
# # # # # # # # # print('//', num1 // num2)
# # # # # # # # # print('%', num1 % num2)

# # # # # # # # # #  ** -> возведение в степень 
# # # # # # # # # print(5 ** 2)
# # # # # # # # # print(16 ** 55)

# # # # # # # # # print(144 ** 0.5) кводратный корень

# # # # # # # # # pow -  возведение в степени
# # # # # # # # # powO(num1, num2)

# # # # # # # # # num1 = 5
# # # # # # # # # num2 = 10
# # # # # # # # # print(pow(5, 10))

# # # # # # # # print(pow(5, 10, 65))
# # # # # # # # print(5 ** 10 % 65)

# # # # # # # a = 5
# # # # # # # b = 2
# # # # # # # res = pow(a, b, 12) 
# # # # # # # print(res)


# # # # # # # round -  это у нас округления числа с плавающей точкой

# # # # # # a = 5.368232

# # # # # # print(round(a, 2))

# # # # # # abc () -  абсолютное значение числа -> abs ()

# # # # # a = abs (-16)
# # # # # # b = abs (15)
# # # # # print(a, b)

# # # # # divmod(a, b)->  она выводит два числа, первое число это результат целочисленного деления (//)а на bб а втрое это модульное деления (%)


# # # # res =  divmod(5, 2)
# # # # print(res)
# # # # print((5 // 2, 5 % 2))

# # # # print(9 ** 0.5)

# # # import math

# # # a = 5

# # # print(round(math.sqrt(a), 2))
# # # res = math.sqrt(a)
# # # print(round(res, 2))

# # # множественнное  присваивание
# # # оператор присваивания(=)
# # a = 5
# # b = 15 
# # c = None
# # print('a:', a, 'b:', b)

# # # c = a
# # # a = b
# # # b = c

# # a, b = b, a

# # print('a:', a, 'b:', b)

# num1, num2, num3 = input('num1:'), input('num2:'), input('num3:')
# print(num1)
# print(num2)
# print(num3)

# from math import pi



# r = int(input('Введите радиус:'))
# res_P = 2 * r * pi
# res_S = pi * (r ** 2)
# print('S okrujnosti:', round(res_S))
# print('P okrujnosti:', round(res_P))

#print(randint(1, 10))

# from random import randint
# name = input('vvedite svoy imiy:')
# last_name = input('vvedite svoy familia:')
# num = randint(1000000, 9_999_999)
# print(name, last_name, num)
# res = name + last_name + str(num)
# print(res)


# from random import randint

# num = randint(1, 10)

# print(num)

# i = 0

# while i < 3:
#     guess = int(input('Ugodai chislo;'))
#     if guess == num:
#         print('you win! krasava!')
#         break
#     #  i = i + 1
#     i += 1 #increment










