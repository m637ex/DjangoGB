from django.core.management.base import BaseCommand
from homeworkapp.models import Product
from faker import Faker
from random import randint
fake = Faker()

# вызов: python manage.py create_client

class Command(BaseCommand):
    help = "Create product."
    def handle(self, *args, **kwargs):
        product = Product(
            name = f'Товар {randint(1,1000)}', # — название товара
            description = fake.sentence(nb_words=10), # —— описание товара
            price = randint(1000,1000000), # — цена товара
            quantity = randint(0,1000), # — количество товара
        ) # создаём модель продукта
        product.save() # создаём экземпляр класса и сохраняем
        self.stdout.write(f'{product}') # Выведем данные в консоль
        

