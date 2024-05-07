from random import choice, randint, uniform

from django.core.management.base import BaseCommand # работа с консолью
from myapp5.models import Category, Product # импортируем модели из ругого приложения


class Command(BaseCommand):
    help = "Generate fake products."

    def add_arguments(self, parser): # получаем данные от пользователя из консоли
        parser.add_argument('count', type=int, help='Generate fake products. Count:')

    def handle(self, *args, **kwargs):
        categories = Category.objects.all()
        products = []
        count = kwargs.get('count')
        for i in range(1, count + 1):
            products.append(Product(
                name=f'продукт номер {i}',
                category=choice(categories),
                description='длинное описание продукта, которое итак никто не читает',
                price=uniform(0.01, 999_999.99),
                quantity=randint(1, 10_000),
                rating=uniform(0.01, 9.99),
            ))
        Product.objects.bulk_create(products) # bulk_create - добавляем список в базу одним запросом