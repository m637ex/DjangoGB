from django.core.management.base import BaseCommand
from modelapp2.models import User


class Command(BaseCommand):
    help = "Create user."
    def handle(self, *args, **kwargs):
        user = User(name='John', email='john@example.com', password='secret', age=25) # создаём модель пользователя
        # user = User(name='Neo', email='neo@example.com', password='secret', age=58)

        user.save() # создаём экземпляр класса и сохраняем
        self.stdout.write(f'{user}') # Выведем данные в консоль
