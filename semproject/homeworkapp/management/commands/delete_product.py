from django.core.management.base import BaseCommand
from homeworkapp.models import Product

# python manage.py delete_product 1


class Command(BaseCommand):
    help = "Delete product by id."
    
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='product ID')
        
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        if product is not None:
            product.delete()
        self.stdout.write(f'{product}')