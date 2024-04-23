from django.core.management.base import BaseCommand
from homeworkapp.models import Client, Product, Order
from faker import Faker
from random import randint, sample
from decimal import Decimal

fake = Faker()

# >python manage.py fake_data 10 100 10
# получим 10 клиентов, 100 товаров, по 10 товаров на клиента.

class Command(BaseCommand):
    help = "Generate fake client and product and order." 
    
    def add_arguments(self, parser):
        parser.add_argument('count_client', type=int, help='client count')
        parser.add_argument('count_product', type=int, help='product count')
        parser.add_argument('count_order', type=int, help='order count')
        
    def handle(self, *args, **kwargs):
        count_client = kwargs.get('count_client')
        count_product = kwargs.get('count_product')
        count_order = kwargs.get('count_order')
        for _ in range(count_product):    
            product = Product(
                name = f'Товар {randint(1,1000)}', # — название товара
                description = fake.sentence(nb_words=10), # —— описание товара
                price = Decimal(randint(1000,100000)), # — цена товара
                quantity = randint(1,1000), # — количество товара
            ) # создаём модель продукта
            product.save() # создаём экземпляр класса и сохраняем
        for _ in range(count_client):
            client = Client(
                name = fake.name(), # — имя клиента
                email = fake.email(), # — электронная почта клиента
                phone = fake.phone_number(), # — номер телефона клиента
                address = fake.address(), # — адрес клиента
            ) # создаём модель Клиента
            client.save() # создаём экземпляр класса и сохраняем
            
            # Получаем случайный продукт
            products = sample(list(Product.objects.all()), count_order)  # случайно выбираем count_order продуктов 
            total_price = total_price = sum(product.price for product in products)  # Суммируем цены всех продуктов
    
            order = Order.objects.create( # Создаем заказ, связывая его с клиентом и добавляем выбранные продукты
                customer=client,
                total_price=total_price,
            )
            order.products.add(*products)  # добавляем продукты к заказу

