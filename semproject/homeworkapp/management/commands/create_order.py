from django.core.management.base import BaseCommand
from homeworkapp.models import Order, Client, Product
from faker import Faker
from random import randint, sample
from decimal import Decimal
fake = Faker()

class Command(BaseCommand):
    help = "Create product."
    def handle(self, *args, **kwargs):
        # Получаем случайного клиента
        client = Client.objects.order_by('?').first()
        # Получаем случайный продукт
        products = sample(list(Product.objects.all()), 3)  # случайно выбираем 3 продукта
        # Вычисляем общую цену заказа
        total_price = sum(product.price for product in products)
        # Приводим общую цену к типу Decimal
        total_price = Decimal(str(total_price))
        # Создаем заказ, связывая его с клиентом и добавляем выбранные продукты
        order = Order.objects.create(
            customer=client,
            total_price=total_price,
        )
        order.products.add(*products)  # добавляем продукты к заказу
        self.stdout.write(f'Order created for client: {client.name} with products: {[product.name for product in products]}')
