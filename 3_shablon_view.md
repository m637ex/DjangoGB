
## Представления ##

# Представления на основе функций:

from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World from function!")

# Представления на основе классов
from django.views import View
from django.http import HttpResponse

class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello World from class!")

# Диспетчер URL:

lessonproject\lessonproject\urls.py # - диспетчер url проектов
lessonproject\myapp3\urls.py # - диспетчер url приложения

# Передача параметров
Происходит в urlpatterns = ... url файла приложения

from .views import year_post, MonthPost, post_detail
urlpatterns = [
    ...
    path('posts/<int:year>/', year_post, name='year_post'), # http://127.0.0.1:8000/les3/posts/2022/
    path('posts/<int:year>/<int:month>/', MonthPost.as_view(), name='month_post'),
    path('posts/<int:year>/<int:month>/<slug:slug>/', post_detail, name='post_detail'), # http://127.0.0.1:8000/les3/posts/2022/6/python/
]

# Преобразование пути в типы Python
В Django преобразование путей осуществляется с помощью приставок, которые
определяют тип данных, который будет передаваться в качестве параметра в
представление. Для этого мы заключаем параметр в треугольные скобки и
указываем приставку, а далее после двоеточия слитно пишем имя параметра.
● str — приставка для передачи строки любых символов, кроме слэша.
Например, если мы хотим передать в представление информацию о
конкретном посте блога, то мы можем использовать такой путь:
path('posts/<str:slug>/', post_detail). Здесь slug - это строка символов, которая
является уникальным идентификатором поста.
● int — приставка для передачи целого числа. Например, если мы хотим
передать в представление информацию о конкретном пользователе по его
идентификатору, то мы можем использовать такой путь:
path('users/<int:id>/', user_detail). Здесь id - это целое число, которое является
уникальным идентификатором пользователя.
● slug — приставка для передачи строки, содержащей только буквы, цифры,
дефисы и знаки подчеркивания. Например, если мы хотим передать в
представление информацию о конкретной категории товаров, то мы можем
использовать такой путь:
path('categories/<slug:slug>/', category_detail). Здесь slug - это строка
символов, которая является уникальным идентификатором категории.
● uuid — приставка для передачи уникального идентификатора. Например, если
мы хотим передать в представление информацию о конкретном заказе, то мы
можем использовать такой путь:
path('orders/<uuid:pk>/', order_detail). Здесь pk - это уникальный
идентификатор заказа.
● path — приставка для передачи строки любых символов, включая слэши.
Например, если мы хотим передать в представление информацию о
конкретном файле на сервере, то мы можем использовать такой путь:
path('files/<path:url>/', file_detail). Здесь url - это строка символов, которая
содержит путь к файлу на сервере.

# в views.py:
def year_post(request, year): # http://127.0.0.1:8000/les3/posts/2022/
    return HttpResponse(f"Posts from {year}")

class MonthPost(View): # http://127.0.0.1:8000/les3/posts/2022/6/
    def get(self, request, year, month):
        return HttpResponse(f"Posts from {month}/{year}")

def post_detail(request, year, month, slug): # http://127.0.0.1:8000/les3/posts/2022/6/python/
    post = {
        "year": year,   # 2022
        "month": month, # 6
        "slug": slug,   # python
        "title": "Кто быстрее создаёт списки в Python, list() или []",
        "content": "В процессе написания очередной программы задумался над тем, какой способ создания списков в Python работает быстрее..."
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False}) # => JSON

# ШАБЛОНЫ
Каталог шаблонов:
myproject/
    myapp1/
        templates/
            myapp1/ # ВАЖНО!!! каталог приложения внутри templates!!!!
                index.html
    myproject/
    manage.py

пример шаблона:
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Первый шаблон Django</title>
</head>
<body>
    <h1>Hello, {{ name }}!</h1> 
</body>
</html>

где {{ name }} - переменная передаваемая из контекста


my_template.html:

from django.shortcuts import render  - сокращает и упрозает разрабтку кода

def my_view(request):
    context = {"name": "John"}
    return render(request, "myapp3/my_template.html", context)

# Проверка условия в шаблонах
        {% if number == 1 %}
            пост
        {% elif number >= 2 and number <= 4 %}
            поста
        {% else %}
            постов
        {% endif %}

# Пробрасываем контекст в if шаблон используя TemplateView в views.ru
from django.views.generic import TemplateView
...
class TemplIf(TemplateView):
    template_name = "myapp3/templ_if.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Привет, мир!"
        context['number'] = 5
        return context

## Вывод в цикле:
1. Вывод элементов списка:
<h2>Элементы списка</h2>
<ul>
{% for item in my_list %}
    <li>{{ item }}</li>
{% endfor %}
</ul>

2. Вывод ключей и значений словаря в таблицу:
<h2>Ключи и значения словаря</h2>
<table>
{% for key, value in my_dict.items %}
    <tr><td>{{ key }}</td><td>{{ value }}</td></tr>
{% endfor %}
</table>

views.py:
def view_for(request):
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

urls.py:
path('for/', view_for, name='templ_for'),

# Наследование шаблонов Django
Пример базового шаблона с наследованием:
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Сайт{% endblock %}</title>
</head>
<body>
    {% block content %}
        <p>Скоро тут появится текст...</p>
    {% endblock %}
</body>
</html>

Пример шаблона, наследующего базовый:
{% extends 'myapp3/base.html' %}
{% block title %}Обо мне{% endblock %}
{% block content %}
    <h1>Обо мне</h1>
    <p>Меня зовут Алексей и я пишу программы с 14 лет.</p>
{% endblock %}

ВАЖНО!!! Если базовый шаблон находится во внутреннем каталоге приложения, первая строка будет следующей: {% extends 'app/base.html' %}

# Базовый шаблон проекта
Настройка происходит в  settings.py проекта в переменной TEMPLATES =
...
'DIRS': [
    BASE_DIR / 'templates', # список где django ищет файлы шаблонов
],
...

в шаблоне index.html:
{% extends 'base.html' %}           <!-- - базовый шаблон проекта -->
{% extends 'myapp3/base.html' %}    <!-- - базовый шаблон приложения -->

irls.py проекта:
from myapp3.views import index
urlpatterns = [
    path('', index), # ссылка на главную страницу проекта по умолчанию ]

# Объединяем модели, представления, шаблоны и маршруты

# Представления
Создадим “вьюшку” для получения 5 последних статей автора из BD:
from django.shortcuts import render, get_object_or_404
from .models import Author, Post

def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('-id')[:5]
    return render(request, 'myapp3/author_posts.html', {'author': author, 'posts': posts})

get_object_or_404 - позволяет обращаться к базе данных и получать их, если данных нет, то возвращаем 404 ошибку

<a href="{% url 'post_full' post.id %}">{{ post.title }}</a> - динамически генерируем ссылку:
url - тэг url принимает имя name='post_full' из urls.py тем самым вызывает станицу /post/<post.id> c идентификатором post.id и описанием {{ post.title }}