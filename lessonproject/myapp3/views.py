from django.shortcuts import render 
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from .models import Author, Post


# Create your views here.

# Представления на основе функций:
def hello(request):
    return HttpResponse("Hello World from function!")

# Представления на основе классов
class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello World from class!")
    
def year_post(request, year): # http://127.0.0.1:8000/les3/posts/2022/
    text = "'Sample text for year'"
    ... # формируем статьи за год
    return HttpResponse(f"Posts from {year}<br>{text}")

class MonthPost(View): # http://127.0.0.1:8000/les3/posts/2022/6/
    def get(self, request, year, month):
        text = "'Sample text for month'"
        ... # формируем статьи за год и месяц
        return HttpResponse(f"Posts from {month}/{year}<br>{text}")


def post_detail(request, year, month, slug): # http://127.0.0.1:8000/les3/posts/2022/6/python/
    ... # Формируем статьи за год и месяц по идентификатору. Пока обойдёмся без запросов к базе данных
    post = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "Кто быстрее создаёт списки в Python, list() или []",
        "content": "В процессе написания очередной программы задумался над тем, какой способ создания списков в Python работает быстрее..."
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})


def my_view(request):
    context = {"name": "John"}
    return render(request, "myapp3/my_template.html", context)

class TemplIf(TemplateView):
    template_name = "myapp3/templ_if.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Привет, мир!"
        context['number'] = 5
        return context
    
def view_for(request): # Вывод в цикле:
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
        'каждый': 'красный',
        'охотник': 'оранжевый',
        'желает': 'жёлтый',
        'знать': 'зелёный',
        'где': 'голубой',
        'сидит': 'синий',
        'фазан': 'фиолетовый',
    }
    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'myapp3/templ_for.html', context)

def index(request):
    return render(request, "myapp3/index.html")

def about(request):
    return render(request, "myapp3/about.html")

def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id) # получаем объект из базы по author_id
    posts = Post.objects.filter(author=author).order_by('-id')[:5]  # отфильтруй все посты автора author, отсортируй список в обратном порядке по id - order_by('-id'), [:5] - возьми последние 5 постов(больштии id)
    return render(request, 'myapp3/author_posts.html', {'author': author, 'posts': posts})

def post_full(request, post_id): # вывести текст поста по id
    post = get_object_or_404(Post, pk=post_id) # получаем объект из базы c id = post_id
    return render(request, 'myapp3/post_full.html', {'post': post})