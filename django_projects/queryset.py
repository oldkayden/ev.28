# Product.objects.all() - выдаёт весь список объектов модели
# SELECT * FROM product;

# Product.objects.create() - создаёт новый объект
# INSERT INTO product ...

# Product.objects.update() - обновляет выбранные объекты
# UPDATE product ...;

# Product.objects.delete() - удаляет объекты
# DELETE FROM product;

# Product.objects.filter(условие)
# SELECT * FROM product WHERE условие;

# Операции сравнения
# "="
# Product.objects.filter(price=10000)
# SELECT * FROM product WHERE price = 10000;

# ">"
# Product.objects.filter(price__gt=10000)
# SELECT * FROM product WHERE price > 10000;

# "<"
# Product.objects.filter(price__lt=10000)
# SELECT * FROM product WHERE price < 10000;

# ">="
# Product.objects.filter(price__gte=10000)
# SELECT * FROM product WHERE price >= 10000;

# "<="
# Product.objects.filter(price__lte=10000)
# SELECT * FROM product WHERE price <= 10000;

# BETWEEN
# Product.objects.filter(price__range=[50000, 80000])
# SELECT * FROM product WHERE price BETWEEN 50000 AND 80000;

# IN
# Product.objects.filter(price__in=[50000, 80000])
# SELECT * FROM product WHERE price IN (50000, 80000);

# LIKE
# ILIKE

# 'work%'
# Product.objects.filter(title__startswith='Apple')
# SELECT * FROM product WHERE title LIKE 'Apple%';
# Product.objects.filter(title__istartswith='Apple')
# SELECT * FROM product WHERE title ILIKE 'Apple%';

# '%work'
# Product.objects.filter(title__endswith='GB')
# SELECT * FROM product WHERE title LIKE '%GB';

# Product.objects.filter(title__iendswith='GB')
# SELECT * FROM product WHERE title ILIKE '%GB';

# '%work%'
# Product.objects.filter(title__contains='Samsung')
# SELECT * FROM product WHERE title LIKE '%Samsung%';
# Product.objects.filter(title__icontains='Samsung')
# SELECT * FROM product WHERE title ILIKE '%Samsung%';

# 'work'
# Product.objects.filter(title__exact='Apple Iphone 12')
# # SELECT * FROM product WHERE title LIKE 'Apple Iphone 12';
# Product.objects.filter(title__iexact='Apple Iphone 12')
# # SELECT * FROM product WHERE title ILIKE 'Apple Iphone 12';

# ORDER BY

# Product.objects.order_by('price')
# SELECT * FROM product ORDER BY price ASC;

# Product.objects.order_by('-price')
# SELECT * FROM product ORDER BY price DESC;

# Product.objects.order_by('-price', 'title')
# SELECT * FROM product ORDER BY price DESC, title ASC;

# LIMIT
# Product.objects.all()[:2]
# SELECT * FROM product LIMIT 2;

# Product.objects.all()[3:6]
# SELECT * FROM product LIMIT 3 OFFSET 3;

# Product.objects.first()
# SELECT * FROM product LIMIT 1;


# get(условие) - возвращает один объект

# Product.objects.get(id=1)
# SELECT * FROM product WHERE id=1;

# DoesNotExist - возникает, если не найден ни один объект
# MultipleObjectsReturned - возникает, когда найдено больше одного
# объекта

# count() - возвращает количество результатов

# Product.objects.count()
# SELECT COUNT(*) FROM product;

# Product.objects.filter(...).count()
# SELECT COUNT(*) FROM product WHERE ...;

# exclude()
# Product.objects.filter(price__gt=10000)
# SELECT * FROM product WHERE price > 10000;

# Product.objects.exclude(price__gt=10000)
# SELECT * FROM product WHERE NOT price > 10000;

# QuerySet - список объектов модели

# HTTP методы ("GET", "POST", "PUT", "PATCH", 'DELETE")