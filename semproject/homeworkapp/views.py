from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

html_index = """
<!doctype html>
<html lang="ru">

<head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="/static/css/bootstrap.min.css">
    <title> Главная </title>
</head>

<body>
    <h1 class="text-monospace">Это мой первый сайт и он работает!!!!"</h1>
    <img src="/static/image/cat.jpg" alt="Моё фото" width="600">
    <p class="text-body text-justify">Сайт на django это супер!!!</p>
    <p class="alert-dark">Все права защищены &copy;</p>
</body>
</html>
"""

html_about = """
<!doctype html>
<html lang="ru">

<head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="/static/css/bootstrap.min.css">
    <title>Обо мне</title>
</head>

<body>
    <h1 class="text-monospace">Привет, меня зовут Андрей</h1>
    <img src="/static/image/foto.jpg" alt="Моё фото" width="600">
    <p class="text-body text-justify">Это мой первый сайт.</p>
    <p class="alert-dark">Все права защищены &copy;</p>
</body>
</html>
"""

def index(request):
    logger.info('Index page accessed')
    return HttpResponse(html_index)

def about(request):    
    logger.info('about page accessed')
    return HttpResponse(html_about)