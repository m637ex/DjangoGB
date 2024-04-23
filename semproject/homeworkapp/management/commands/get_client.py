from django.core.management.base import BaseCommand
from homeworkapp.models import Client

# python manage.py get_client 3


class Command(BaseCommand):
    help = "Get client by id."

    def add_arguments(self, parser): # этот метод посде вызова команды позволит принимать аргументы
        parser.add_argument('pk', type=int, help='client ID') # Принимаем id
        
    def handle(self, *args, **kwargs):
        pk = kwargs['pk'] # меняем id на pk - pk - primary key, первичный ключ в таблице, т.е. ID.
        client = Client.objects.filter(pk=pk).first() # ищем до первого .first() совпадения filter(pk=pk) 
        self.stdout.write(f'{client}')
        
# Если пользователя нет то вернёт None