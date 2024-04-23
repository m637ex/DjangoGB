from django.core.management.base import BaseCommand
from homeworkapp.models import Client
from faker import Faker
fake = Faker()

# вызов: python manage.py create_client

class Command(BaseCommand):
    help = "Create Client."
    def handle(self, *args, **kwargs): 
        client = Client(
            name = fake.name(), # — имя клиента
            email = fake.email(), # — электронная почта клиента
            phone = fake.phone_number(), # — номер телефона клиента
            address = fake.address(), # — адрес клиента
        ) # создаём модель Клиента
        client.save() # создаём экземпляр класса и сохраняем
        self.stdout.write(f'{client}') # Выведем данные в консоль
