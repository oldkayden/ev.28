# обработка исключений
# операторы try..except

# Error -> связаны с кодом
    # SyntaxError
    # IndentationError
    # TabError

# Исключение exception -> связанные с неправильными данными которые передаются в код 
    # ZeroDivisionError
    # ArithmeticError
    # NameError
    # IndentationError
    # KeyError
    # BaseException -> Прородитель всех исключений

# try:
#     a = int(input('Enter the number: '))
# except:
#     print('Не правильноые данные!')
# else:
#     print(a * 5)

# try:
#     <body>
# except:
#     <body> сработает если есть ошибки
# <else>:
#     <body> если нет ошибки
# <finally>:
#     <body> сработает в любом случае


# ls = ['Lohn', 'Snow', 'Tirion']

# try:
#     a = int(input('Vvedite Index: '))
#     print(ls(i))
# except ValueError:
#     print('Вы ввели неправильные данные')
# except IndexError:
#     print('Вы ввели неправильний индекс')

# ---------------------------------------------------------------------------------------------------------------
# отображение ошибки
# Exception as e(erroor)

# dict_={1: 'one', 2: 'two', 'name': 'John'}

# try:
#     key = input('Vvedite key: ')
#     print(dict_[key])
# except Exception as e:
#     print(f'opps {e.__class__} error!')

# try:
#     num1 = int(input('Enter num1: '))
#     num2 = int(input('Enter num2: '))
#     result = num1 / num2 
# except ValueError:
#     print('Invalid input!')
# except ZeroDivisionError:
#     print('Na 0 delit\' nel\'zya!')
# else:
#     print(result)
# finally:
#     print('The End!')

















