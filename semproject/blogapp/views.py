from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import random
import logging

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page accessed')
    return HttpResponse("<h1>Hello, blogers!</h1>")

def blog(request):    
    # coin = Coin(site=random.choice(['Орёл', 'Решка'])) # создаём модель 
    # coin.save() # сохраняем в базу
    logger.info(f'Blog page accessed.')
    return HttpResponse(f"My blog running") 