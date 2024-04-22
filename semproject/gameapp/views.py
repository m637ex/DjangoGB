from django.shortcuts import render
from gameapp.models import Coin

# Create your views here.
from django.http import HttpResponse
import random
import logging

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page accessed')
    return HttpResponse("<h1>Hello, gamers!</h1>")

def coin(request):    
    coin = Coin(site=random.choice(['Орёл', 'Решка'])) # создаём модель 
    coin.save() # сохраняем в базу
    logger.info(f'Coin page accessed. Выпало: {coin.site}')
    return HttpResponse(f"""<h1>Подбросим монетку...</h1><p>Орел или решка?</p><p>Однозначно {coin.site}!</p>""") 

def coin_values(request): # Последние 5 бросков
    value = Coin.last_five_values()
    lst = []
    for i in value:
        print(i)
        lst.append(i.site)
    return HttpResponse(f"<h1>Последние 5 бросков видно в принте</h1>{lst}")

def cube6(request):
    logger.info('cube6 page accessed')
    return HttpResponse(f"<h1>Бросаем кубик... На кубике выпало: {random.randint(1, 7)}</h1>")

def random100(request):
    logger.info('random100 page accessed')
    return HttpResponse(f"<h1>Рандом из 100. Ваше число на сегодня - {random.randint(1, 101)}.</h1>")