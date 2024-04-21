from django.core.management.base import BaseCommand
from modelapp2.models import User


class Command(BaseCommand):
    help = "Update user name by id."
    
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('name', type=str, help='User name')
        
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        user = User.objects.filter(pk=pk).first()
        user.name = name    # name найденого пользователя меняем на name переданное из командной строки
        user.save() # сохраняем в базу
        self.stdout.write(f'{user}')