from django.core.management.base import BaseCommand
from homeworkapp.models import Client

# python manage.py update_client 2 Andrey


class Command(BaseCommand):
    help = "Update Client name by id."
    
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('name', type=str, help='Client name')
        
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        client = Client.objects.filter(pk=pk).first()
        client.name = name    # name найденого пользователя меняем на name переданное из командной строки
        client.save() # сохраняем в базу
        self.stdout.write(f'{client}')