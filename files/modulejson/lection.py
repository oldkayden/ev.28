# JSON - Java
# единый текстовый формат данных, был создан для хранение и передачи данных между сервисами
# <filename>.json # файл в формате JSON
# {
#     "id":1,
#     "auter":{
#     "name": "Ed Sheeran",
#     "age": 35
#     },
#     "title": "don't",
#     "feat": false,
# } ------- это JSON


# !!!!
# js object == {key : value}
# Py dict == {key : value}
# JSON == {key : value}

# Процессы Сериализации и Десериализации данных (конвертация)

# Сериализация (запись данных в JSON) - это переводит из Pethon в Json формат

# dump - записывает данные в файл формата JSON
# dumps - записывает данные в текст формата JSON

# Десериалтзация (чтение данных из JSON) - это процесс перевода из JSON в PY dict

# load- Это функция которая считывает данные из текста 
# loads - функция которая считывает данные из текста JSON

#---------------------------------------------------------------------------------


# # Процесс сериализации
# import json 

# dict_ = {
#     "name" : "John Snow",
#     "age" : 24,
#     "status" : True,
#     "wife" : False,
#     "cildren" : None,
# }
# print(dict_, type(dict_))
# with open('new.json', 'w') as file:
#     json.dump(dict_, file, indent=4)

# json_text = json.dumps(dict_)
# print()
# print(json_text, type(json_text))

#---------------------------------------------------------
#процесс десериализации

# import json

# with open('new.json', 'r') as file:
#     json_data = file.read()

# print(json_data, type(json_data))
# dict_ = json.loads(json_data)
# print()
# print(dict_, type(dict_))


# import json

# with open('new.json', 'r') as file:
#     dict_ = json.load(file)
#     print(dict_, type(dict_))

#---------------------------------------------------------------------------

from urllib.request import urlopen
import json
import pprint as pp

url = 'https://randomuser.me/api/'
json_data = urlopen(url)
# print(json_data, dir(json_data))

dict_ = json.load(json_data)
pp.pprint(dict_, indent=(0))








