from models import Product, Category


# query = Product.update(price=1_000_000).where(Product.id==5)
# print(query, '!!!')
# query.execute()

# query = Product.update(price=(Product.prpice * 1.5))
# query.execute() #увеличиваем всем товарам цену

#Удалить данных

# product = Product.get(Product.id==5)
# print(product, product.title)
# product.delete_instance()
# print(product)

# query = Category.delete().where(Category.id==6)
# query.execute()








