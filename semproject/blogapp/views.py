from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import random
import logging
from .models import Author

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page accessed')
    return HttpResponse("<h1>Hello, blogers!</h1>")

def view_authors(request):    
    # coin = Coin(site=random.choice(['Орёл', 'Решка'])) # создаём модель 
    # coin.save() # сохраняем в базу
    logger.info(f'view_authors page accessed.')
    return HttpResponse(f"view_authors running")  

def create_author(request):
    for i in range(100):
        author = Author(firstname=f'Firstname{i}', lastname=f'Lastname{i}', email=f'Email{i}@example.com', biography='Родился, жил, писал разное', birthday='2000-01-01') 
        author.save()
    logger.info(f'create_author page accessed and 100 authors.')
    return HttpResponse(f"create_author 100 authors")
