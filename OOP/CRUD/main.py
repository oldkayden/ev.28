from views import CreateMixin, Readmixin, UpdateMixin, DeleteMixin
import json

class Product(CreateMixin, Readmixin, UpdateMixin, DeleteMixin):
    def save(self):
        with open('data.json', 'w') as file:
            json.dump(self.objects, file, indent=4)
        return 'Saved'


class Comment(CreateMixin, Readmixin, DeleteMixin):
    pass


smartphons = Product()
print(smartphons.post(title='Redmi Note 10', description='The best phon for own price!', qty=10, price=250))
print(smartphons.post(title='Bilal mini 11', description='The best phon for own price!', qty=5, price=500))
print(smartphons.post(title='Emmir Small 12', description='The best phon for own price!', qty=12, price=380))
print(smartphons.post(title='Artur Pro 13', description='The best phon for own price!', qty=99, price=5467890))
print()
print()
print(smartphons.list())
print()
print(smartphons.detail(1))
# print(smartphons.detail(15))
# print()
# print(smartphons.patch(1, title='Redmi note 9'))
# print()
# print(smartphons.list())
# print(smartphons.detail(1))


