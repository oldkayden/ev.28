# работе с файломи

# карета - указатель - курсор

# open(<путь до файла>)


# file = open ('/home/bakberdi/Desktop/ev.28/lecture') #абсолютный путь

# file = open('files.py') # относительный путь (относительно  то директории в каторой вы работаете)

# Режими работа с фалами

# 1. чтения -> r/r+ (read)
# 2. записи -> w/w+ (wrate)
# 3. Добавления -> a/a+ (append)
# b, x, t

# file = open('text.txt', 'r')
# print(file.read())
# file.close()


# file = open('text.txt')
# data = file.read()
# data = data.split('\n')
# print(data)
# file.close()

# Контекстный менеджер

# with open('text.txt') as file: #file = open('text.txt')
#     data = file.readline()
#     print(data)
#     data = (file.readline())
#     print(file, 'inside')

# print(file.read, 'outside')


# file.tell() -> возврощает индекс где нахоится(курсор)
# file.seek(index) -> перемещает курсор на (index) который вы передали

# with open('text.txt', 'r') as file:
    # print(file.readline().replace('\n', ''))
    # print(file.tell())
    # # file.seek(0)
    # print(file.readline().replace('\n', ''))
    # data = file.read()
    # index = data.index('\n')
    # file.seek(index+1)
    # print(file.readline().replace('\n', ''))
    # print(file.readlines()[1]) #самый легкий путь
    # print(file.tell())
    # file.read()
    # print(file.tell())
    # print(file.readline())


# with open('text.txt', 'r') as file:
    # print(file.readline(50))
    # print(file.readlines(-1))
    # print(file.read(5))

# with open('text.txt', 'a') as file:
#     file.write('Privet Stroka!\n')
#     file.write('Baha Snow is bastard of lageng!\n')
#     file.write('lsdjghfakdfghk.adfjbgfk;jasf\n')
#     file.seek(0)
#     data = ['Bilal is genuis!', 'Tima is good boy!\n']
#     file.writelines(data)


# with open('text.txt', 'r+') as file:
#     file.write('John Snow!')
#     file.seek(0)
#     print(file.read())

# try:
#     from PIL import Image
# except ImportError:
#     import Image

# import pytesseract
# import re

# def get_imei_code(image):
#     string = pytesseract.image_to_string(image)
#     # print(string, type(string))
#     list_of_imei = re.findall(r'IMEI\d.\s\d+', string)
#     print(list_of_imei)

#     with open('imei_codes.txt', 'w') as file:
#         file.writelines(f'{x}\n' for x in list_of_imei)

# image = 'imei.jpg'
# get_imei_code(image)


