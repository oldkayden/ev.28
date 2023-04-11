# import random

# def guess_number():
#     # генерируем случайное число от 1 до 100
#     secret_number = random.randint(1, 100)
#     print("Загаданное число:", secret_number)

#     # запрашиваем у пользователя ввод числа и проверяем его
#     while True:
#         try:
#             guess = int(input("Угадайте число от 1 до 100: "))
#         except ValueError:
#             print("Неверный ввод. Попробуйте еще раз.")
#             continue

#         if guess < 1 or guess > 100:
#             print("Число должно быть от 1 до 100. Попробуйте еще раз.")
#             continue

#         if guess == secret_number:
#             print("Поздравляю! Вы угадали число!")
#             break
#         elif guess < secret_number:
#             print("Загаданное число больше.")
#         else:
#             print("Загаданное число меньше.")

# if __name__ == '__main__':
#     guess_number()
