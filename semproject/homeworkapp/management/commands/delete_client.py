from django.core.management.base import BaseCommand
from homeworkapp.models import Client

# python manage.py delete_client 1


class Command(BaseCommand):
    help = "Delete client by id."
    
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        if client is not None:
            client.delete()
        self.stdout.write(f'{client}')