from django.shortcuts import render
from gameapp.models import Coin

# Create your views here.
from django.http import HttpResponse
import random
import logging

logger = logging.getLogger(__name__)

_links_menu = [ # список ссылок для меню
    {'url': '/game/',
        'name': 'Главная'},
    {'url': '/game/coin/',
        'name': 'Монетка'},
    {'url': '/game/coin_values/',
        'name': 'Монетка 5 результатов'},
    {'url': '/game/cube6/',
        'name': 'Кубик'},
    {'url': '/game/random100/',
        'name': 'Рандом 100'},
]

def index(request):
    context = {
        "title": "Главная страница",
        "header": "Главная страница",
        "footer": "Главная страница",
        "name": "Andrey",
        'links_menu': _links_menu,
        "image_url": '/images/games.png',
    }
    logger.info('Index page accessed')
    return render(request, "gameapp/index.html", context=context)

def coin(request):    
    context = {
        "title": "Монетка",
        'links_menu': _links_menu,
        "game_name": "Монетка",
        "content": "Подбросим монетку... \
                    Орел или решка?"
    }
    coin = Coin(site=random.choice(['Орёл', 'Решка'])) # создаём модель 
    context['result_game'] = coin.site
    coin.save() # сохраняем в базу
    logger.info(f'Coin page accessed. Выпало: {coin.site}')
    return render(request, "gameapp/result_games.html", context=context)
    # return HttpResponse(f"""<h1>Подбросим монетку...</h1>
    #                     <p>Орел или решка?</p>
    #                     <p>Однозначно {coin.site}!</p>""") 

def coin_values(request): # Последние 5 бросков
    context = {
        "title": "5 бросков монетки",
        'links_menu': _links_menu,
        "content": "Последние 5 бросков."
    }
    value = Coin.last_five_values()
    lst = []
    for i in value:
        print(i)
        lst.append(i.site)
    context['result_game'] = lst
    return render(request, "gameapp/result_games.html", context=context)
    # return HttpResponse(f"<h1>Последние 5 бросков видно в принте</h1>{lst}")

def cube6(request):
    context = {
        "title": "Кубик",
        'links_menu': _links_menu,
        "image_url": '/images/games.png',
        "game_name": "Кубик",
    }
    logger.info('cube6 page accessed')
    context['result_game'] = random.randint(1, 7)
    return render(request, "gameapp/result_games.html", context=context)
    # return HttpResponse(f"<h1>Бросаем кубик... На кубике выпало: {random.randint(1, 7)}</h1>")

def random100(request):
    context = {
        "title": "Рандом 100",
        'links_menu': _links_menu,
        "image_url": '/images/games.png',
        "game_name": "Рандом 100",
    }
    logger.info('random100 page accessed') 
    context['result_game'] = random.randint(1, 101)
    return render(request, "gameapp/result_games.html", context=context)
    # return HttpResponse(f"<h1>Рандом из 100. Ваше число на сегодня - {random.randint(1, 101)}.</h1>")