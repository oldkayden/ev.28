from models import Product, Category


def get_all_categories():
    return Category.select(Category.id, Category.title)


def get_all_products():
    return Product.select()

# categories = get_all_categories()
# print(categories)
# print('Все категори в БД: ')
# for category in categories:
#     print(f'ID: {category} Title: {category.title}')


# products = get_all_products()
# print('Все продукты в БД: ')
# for x in products:
#     print(f'ID: {x.id}, Title: {x.title}, Price: {x.prpice}, Category: {x.category_id}')    


# category_laptops = Category.get(Category.title=='laptops')
# print(category_laptops, category_laptops.title)

# for product in category_laptops.products: 
#     print(f'ID: {product.id}, Title: {product.title}, Price: {product.prpice}, Category: {product.category_id.title}')











