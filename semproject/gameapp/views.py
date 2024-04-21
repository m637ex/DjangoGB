from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import random
import logging

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page accessed')
    return HttpResponse("<h1>Hello, world!</h1>")

def heads_or_tails(request):    
    logger.info('heads_or_tails page accessed')
    return HttpResponse(f"<h1>Орел или решка? Однозначно {random.choice(['Орёл', 'Решка'])}!</h1>")

def cube6(request):
    logger.info('cube6 page accessed')
    return HttpResponse(f"<h1>Кубик выпал: {random.randint(1, 7)}</h1>")

def random100(request):
    logger.info('random100 page accessed')
    return HttpResponse(f"<h1>Рандом из 100. Ваше число на сегодня - {random.randint(1, 101)}.</h1>")