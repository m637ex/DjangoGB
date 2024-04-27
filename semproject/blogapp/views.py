from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import logging
from .models import Author

logger = logging.getLogger(__name__)

_links_menu = [ # список ссылок для меню
    {'url': '/blog/',
        'name': 'Главная'},
    {'url': '/blog/about/',
        'name': 'Обо мне'},
]

def index(request):
    context = {
        "title": "Главная страница",
        "header": "Главная страница",
        "footer": "Главная страница",
        "name": "Andrey",
        'links_menu': _links_menu,
        "image_url": '/images/cat.jpg',
    }
    return render(request, "blogapp/index.html", context=context)

def about(request):
    context = {
        "title": "Обо мне",
        "header": "Обо мне",
        "footer": "Обо мне",
        'links': _links_menu,
        "about_text": "My about text",
        "image_url": '/images/foto.jpg',
    }
    return render(request, "blogapp/about.html", context=context)

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
