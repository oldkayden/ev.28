# dict() - Это у нас словарь -> упорядочанная колекция элементов (python 3.7 -> ordered) 
# Каждый элемент внутри словаря хранятся в виде пары:--> {ключа значение}
# Ассоциативный массив, hash table, object(js), structure == dictionary(py)

# Ключами могут быть только не изменяймые типы данных и в словаре сохраняются только уникальные ключи.
# тогда как значениями могут выступать любые типы данных.

# thisdict = {
#     "brand" :"Ford",
#     "model" : "Mustang",
#     "year" : 1967
# }

# # print(thisdict)
# # print(type(thisdict))
# print(thisdict["brand"], thisdict["model"])
# print(thisdict["year"])

# thisdict["motor"] = "GTE Turbo"
# thisdict["brand"] = "tesla"
# print(thisdict)

# a = {}
# b = dict()

# ------------------------------------------------------------

# items - выводит все содержимое ключ и элемент, keys - выводит содержимое ключей, values - выводит содержимое элемент
# user_info = {
#     "first_name" : "John",
#     "last_name": "Snow", 
#     "age" : 24,
#     "email" : "johnsnow@gmail.com",
#     "role": "admin",
#  }

# ls = user_info.keys()
# ls = list(ls)
# print(ls[2:])

# ls = list(user_info.values())
# print(ls)

# items = user_info.items()
# print(items)
# print(user_info)
# for value in user_info.values():
#     print(value)

# for key in user_info.keys():
#     print(key)

# print(user_info)
# for key, value in user_info.items():
#     print(f"keys: {key}, values: {value}")

# dict_ = {"name":"Jack", "age":17}
# print(dict_)
# dict_["name"] = "John"
# dict_["age"] = 24
# dict_["address"] = "WinterFell"
# print(dict_)
# dict_.update({"age": 25, "address":"BlackCastle"})
# print(dict_)

# ------------------------------------------------------------

# Получение данных со словаря 
# dict_ = {1: "Pizza", 2: "Burger", 3: "Steak"}
# print(dict_[2], "!!!")
# print(dict_.get(2))
# setdefault - работает так же как get, но если нет такого ключа то он создает новую пару из этого ключа 
# dict_ = {1: "Pizza", 2: "Burger", 3: "Steak"}
# print(dict_.setdefault(4, "Riba"))
# print(dict_.get(4))
# print(dict_)
# ------------------------------------------------------------
# создания словаря - fromkeys
# ls = list(range(1, 100))
# new_dict = dict.fromkeys(ls, "value")
# print(new_dict)
# ------------------------------------------------------------

# удаление элемнтов 
# pop, popitem
# pop(<key>) - удоляет пару по ключу
# dict_ = {"name" : "John", "last_name" : "Snow"}
# print(dict_)
# removed = dict_.pop("last_name")
# print(dict_)
# print(removed)

# popitem - удоляет последнию пару

# dict_ = {"name" : "John", "last_name" : "Snow"}
# removed = dict_.popitem()
# print(dict_)
# print(removed)

# ------------------------------------------------------------
# roles = {
#     0: "Admin",
#     1: "Customer",
#     2: "Vendor",
# }
# users = {
#     55: {
#     "id" : 1, "role" : roles[2], "username" : "Tirion",
#     },
#     2: {
#     "id" : 2, "role" : roles[0], "username" : "John Snow",
#     },
#     3:{
#     "id" : 3, "role" : roles[1], "username" : "Raychel",
#     }
# }
# print(users)

# product = {
#     "id": 1,
#     "title" : "Samsung Galaxy A51",
#     "description" : "Lorem Ipsum",
#     "price" : 250
# }
# print(product)
# id_user = int(input("Введите id: ")) # 55
# if users [id_user]["role"] == roles[0]:
#     product["description"] = input("Введите описание: ")
# else:
#     print("You do not have permissions!")

# print(product)
# list_ = [1, 2, 3, 4, 5]
# new_list = list_.split(',', '')
# print(new_list)





# a=1
# while a<=10:
#     b=1
#     while b<=a:
#         c=a*b
#         print(c, end=" ")
#         b+=1
#     print(" ")
#     a+=1



# print('Таблица умножения')
 
# for i in range(1, 10):
#     for k in range(2, 10):
#         print(f'{i} * {k} = {i * k}\t', end='')
#     print('')
# else:
#     print('It\'s off')


# import pygame, sys
# import random

# # Инициализация Pygame
# pygame.init()

# # Определение размеров экрана
# screen_width = 640
# screen_height = 480

# # Создание окна
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption('Snake Game')

# # Определение цветов
# white = (255, 255, 255)
# black = (0, 0, 0)
# red = (255, 0, 0)
# green = (0, 255, 0)

# # Определение констант
# cell_size = 10
# fps = pygame.time.Clock()
# font = pygame.font.SysFont(None, 25)

# # Определение функции отображения сообщения на экране
# def message(msg, color):
#     screen_text = font.render(msg, True, color)
#     screen.blit(screen_text, [screen_width/6, screen_height/3])

# # Определение функции для создания змеи
# def create_snake(cell_size, snake_list):
#     for x in snake_list:
#         pygame.draw.rect(screen, green, [x[0], x[1], cell_size, cell_size])

# # Определение главной функции игры
# def game_loop():
#     # Определение переменных игры
#     game_over = False
#     game_close = False

#     # Начальная позиция змеи
#     x1 = screen_width/2
#     y1 = screen_height/2

#     # Изменение позиции змеи
#     x1_change = 0       
#     y1_change = 0

#     # Создание списка для змеи
#     snake_list = []
#     length_of_snake = 1

#     # Определение случайной позиции для еды
#     foodx = round(random.randrange(0, screen_width - cell_size) / 10.0) * 10.0
#     foody = round(random.randrange(0, screen_height - cell_size) / 10.0) * 10.0

#     # Главный игровой цикл
#     while not game_over:
#         # Обработка событий
#         while game_close == True:
#             screen.fill(white)
#             message("Вы проиграли! Нажмите Q-Выход или C-Новая игра", red)
#             pygame.display.update()

#             # Обработка нажатия клавиш
#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_q:
#                         game_over = True
#                         game_close = False
#                     if event.key == pygame.K_c:
#                         game_loop()

#         # Обработка событий
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_over = True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x1_change = -cell_size
#                     y1_change = 0
#                 elif event.key == pygame.K_RIGHT:
#                     x1_change = cell_size
#                     y1_change = 0
#                 elif event.key == pygame.K_UP:
#                     y1_change = -cell_size
#                     x1
# import pygame
# import time
# import random

# pygame.init()

# # Определение цветов
# white = (255, 255, 255)
# black = (0, 0, 0)
# red = (213, 50, 80)
# green = (0, 255, 0)
# blue = (50, 153, 213)

# # Определение размеров экрана
# dis_width = 800
# dis_height = 600

# # Создание окна
# dis = pygame.display.set_mode((dis_width, dis_height))
# pygame.display.set_caption('Snake Game')

# # Определение размера и скорости змеи
# snake_block = 10
# snake_speed = 15

# # Определение шрифта для отображения текста
# font_style = pygame.font.SysFont("bahnschrift", 25)

# # Определение функции отображения текста на экране
# def message(msg, color):
#     mesg = font_style.render(msg, True, color)
#     dis.blit(mesg, [dis_width / 6, dis_height / 3])

# # Определение функции игры
# def gameLoop():
#     game_over = False
#     game_close = False

#     # Определение начальных координат для змеи
#     x1 = dis_width / 2
#     y1 = dis_height / 2

#     # Изменение координат змеи
#     x1_change = 0
#     y1_change = 0

#     # Создание списка для хранения координат змеи
#     snake_List = []
#     Length_of_snake = 1

#     # Определение начальных координат для еды
#     foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#     foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

#     # Главный игровой цикл
#     while not game_over:

#         # Обработка нажатия клавиш
#         while game_close == True:
#             dis.fill(black)
#             message("Вы проиграли! Нажмите Q-Выход или C-Новая игра", red)
#             pygame.display.update()

#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_q:
#                         game_over = True
#                         game_close = False
#                     if event.key == pygame.K_c:
#                         gameLoop()

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_over = True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x1_change = -snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_RIGHT:
#                     x1_change = snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_UP:
#                     y1_change = -snake_block
#                     x1_change = 0
#                 elif event.key == pygame.K_DOWN:
#                     y1_change = snake_block
#                     x1_change = 0
                    