import peewee
from models import Category, Product
import random


def add_category(name):
    try:
        obj = Category(title=name.lower().strip())
        obj.save()
        print(f'Сохрани категорию {obj}')
    except (peewee.IntegrityError, peewee.InternalError):
        print(f'{name.lower().strip()} - Это категория уже существует!')

# add_category('laptops')
# add_category('   comuters    ')
# add_category('Sony Playstations')
# add_category('Tablets')
# add_category('earphones')

def add_product(name, prpice, category_name):
    category_name = category_name.lower().strip()
    try:
        category = Category.get(title = category_name)
        # print(category, category.title, category.created_at)
    except peewee.DoesNotExist:
        print(f'Категории {category_name} не существует!')
    else:
        obj = Product(title = name, prpice = prpice, category_id = category)
        obj.save()
        print(f'Сохранили товар {obj} - {obj.title}')
        
# add_product('asus megabook', 1000, 'Laptops')
# add_product('Acer Swift', 1080, 'Laptops')
# add_product('Iphone 14 Pro', 1100, 'Smartphone')
# add_product('Samsung S22 ULTRA', 1300, 'Smartphone')
# add_product('Acer megabook', 1090, 'Minibook')
# add_product('lenovo megabook', 1200, 'Laptops')
# add_product('Airpods', 12000, 'earphones')

#----------------------------------------------------------
# добавление новых данных

# add_category('cars')

with open('files/cars.txt', 'r') as file:
    ls = file.readlines()
    print(ls)
    for x in ls:
        name = x.strip()
        prpice = random.randint(5000, 20000)
        add_product(name, prpice, 'cars')


with open('files/telefon.txt', 'r') as file:
    ls = file.readlines()
    print(ls)
    for x in ls:
        name = x.strip()
        print(name)
        prpice = random.randint(5000, 20000)
        add_product(name, prpice, 'smartphones')



































