# sentence = input('VVedite predlojenie: ')


# if sentence[-1] == ' ?':
#     print('Yes, vopsotel\'noye!')
# else:
#     print('No, normal one!')


# print('Yes, vopsotel\'noye!' if sentence[-1] == '?' else 'No, normal one!')
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ternary operatots(Тернарный оператор) -Это окнструкция которая по своему действию аналогичным конструкции if/elsse,  но при этом записывается в одну строчку

# number = int(input('Vvedite chislo: '))
# res = 'even number' if number % 2 == 0 else 'odd number' 
#         #четное                              #не четное
# print(res)

# <выражение если True> if <условие> else <выражение если False> 

# ls = [55, 66, 75, 89, 100, 15, 6]
# print(ls)
# choice = input('Vvedite max/min: ')
# res = max(ls) if choice.lower().strip() == 'max' else min(ls)
# print(res)

# if choice.lower().strip() == 'max':
#     print(max(ls))
# elif choice.lower().strip() == 'min':
#     print(min(ls))
# else:
#     print('Тупой инвалид!')


# res = max(ls) if choice.lower().strip() == 'max' else min(ls) if choice.lower().strip() == 'min' else 'invalid ty!'
# print(res)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

# flag = True
# symbols = '0123456789' + '-' + '.'     #0123456789-.

# while flag:
#     print()
#     num1 = input('Vvedite pervoe chislo: ') 
#     is_correct_number = True   
#     for x in num1:
#         if x not in symbols:
#             print('Vy veli ne pravilnoe chislo!')
#             is_correct_number = False
#             break
#     if not is_correct_number:
#         continue
        
#     operator = input('Введите оператор(+, -, *, /): ').strip() 

#     num2 = input('Vvedite vtoroe chislo: ')
#     for x in num2:
#         if x not in symbols:
#             print('Vy veli ne pravilnoe chislo!')
#             is_correct_number = False
#             break
#     if not is_correct_number:
#         continue

#     num1 = float(num1) if '.' in num1 else int (num1)
#     num2 = float(num2) if '.' in num2 else int (num2)

    # print(num1, type(num1))
    # print(num2, type(num2))

    # if operator == '+':
    #     print(f'Результат: {num1 + num2}')
    # elif operator == '-':
    #     print(f'Результат: {num1 - num2}')
    # elif operator == '*':
    #     print(f'Результат: {num1 * num2}')
    # elif operator == '/':
    #     if num2 == 0:
    #         print('На ноль делить нельзя!')
    #     else:
    #         print(f'Результат: {num1 / num2}')
    # else:
    #     print('Ты чеееееееееееееееее?')

    # choice = input('Хотите продолжить (yes/no)? ')
    # if choice.lower().strip() != 'yes':
    #     flag = False
    #     print('Пока пока!')






  # if ('-' in num1 and num1 [0] == '-') or '-' not in num1:
    #     num1 = int(num1)




# list_ = [1, 2, 3, 4, 5]
# new_list = str(['1', '2', '3', '4', '5'])
# print(new_list)