from django.core.management.base import BaseCommand
from modelapp2.models import User


class Command(BaseCommand):
    help = "Get user by id."


    # def add_arguments(self, parser): # этот метод посде вызова команды позволит принимать аргументы
    #     parser.add_argument('id', type=int, help='User ID') # Принимаем id
        
    # def handle(self, *args, **kwargs):
    #     id = kwargs['id']
    #     user = User.objects.get(id=id)
    #     self.stdout.write(f'{user}')

# меняем id на pk - pk - primary key, первичный ключ в таблице, т.е. ID. и используем filter()
    def add_arguments(self, parser): # этот метод посде вызова команды позволит принимать аргументы
        parser.add_argument('pk', type=int, help='User ID') # Принимаем id
        
    def handle(self, *args, **kwargs):
        pk = kwargs['pk'] # меняем id на pk - pk - primary key, первичный ключ в таблице, т.е. ID.
        user = User.objects.filter(pk=pk).first() # ищем до первого .first() совпадения filter(pk=pk) 
        self.stdout.write(f'{user}')
        
# Если пользователя нет то вернёт None