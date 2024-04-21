.python -m venv .venv
.venv\Scripts\activate.ps1 # Windows PowerShell
pip install django

# Создание проекта
django-admin startproject myproject

# Запуск сервера
python manage.py runserver # default запуск
python manage.py runserver 8080 # порт 8080
python manage.py runserver 0.0.0.0:80 # запуск в локальную сеть по всем ip, в ALLOWED_HOSTS нужно внести разрешенные адреса

# создание приложения
"python manage.py startapp <app_name>", где <app_name> - название приложения.
python manage.py startapp myapp

# Обзор структуры приложения 
● myapp/ - директория приложения
    ○ migrations/ - директория для хранения миграций базы данных
        ■ __init__.py - файл, указывающий на то, что директория является пакетом Python
    ○ __init__.py - файл, указывающий на то, что директория является пакетом Python
    ○ admin.py - файл для настройки административного интерфейса приложения
    ○ apps.py - файл для настройки приложения
    ○ models.py - файл, содержащий модели данных приложения
    ○ tests.py - файл для написания тестов приложения
    ○ views.py - файл, содержащий представления (views) приложения
● myproject/ - директория проекта
    ○ __init__.py - файл, указывающий на то, что директория является пакетом Python
    ○ settings.py - файл, содержащий настройки проекта
    ○ urls.py - файл, содержащий маршруты (routes) для обработки URLадресов
    ○ asgi.py - файл для запуска ASGI-сервера (Asynchronous Server Gateway Interface)
    ○ wsgi.py - файл для запуска WSGI-сервера (Web Server Gateway Interface)
● db.sqlite3 - файл базы данных SQLite
● manage.py - файл для управления проектом Django (запуск сервера, создание миграций и т.д.)

# Добавление приложения в проект
Для этого нужно добавить название приложения в список INSTALLED_APPS.  (файл settings.py):
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gameapp',  # <=== наше приложение
]

# Создание представления в приложении
Для создания представления нужно определить функцию в файле views.py:
from django.http import HttpResponse
def index(request):
    #logger.info('Index page accessed')
    return HttpResponse("<h1>Hello, world!</h1>")

# Настройка путей urls.py проекта
Маршруты (routes) определяются в файле urls.py проекта:
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')), # '' - корневой путь / сайта для вызова приложения myapp
]

# Создаем файл urls.py в директории приложения
Внутри myapp/urls.py пропишем следующий код:
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]

# Логирование в Django #
Для настройки логирования в Django необходимо изменить файл settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process} {thread} {message}',
            'style': '{',
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose', # добавлен параметр formatter
        },
        'file': {
            'class': 'logging.FileHandler',
            # 'filename': '/path/to/django.log',
            'filename': './log/django.log',
            'formatter': 'verbose', # добавлен параметр formatter
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
        'myapp': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

'''
Давайте рассмотрим каждый параметр:
● version: версия формата конфигурации логирования. В настоящее время используется версия 1.
● disable_existing_loggers: если значение равно True, то все существующие логгеры будут отключены. 
    Если значение равно False, то существующие логгеры будут продолжать работать.
● handlers: определяет, какие обработчики будут использоваться для
    записи логов. Обработчики могут быть консольными или файловыми.
● loggers: определяет, какие логгеры будут использоваться для записи логов. 
    Логгеры могут быть определены для фреймворка Django или для конкретного приложения.

Для каждого обработчика и логгера можно указать следующие параметры:
● class: класс, который будет использоваться для записи логов. В нашем примере мы используем 
    классы StreamHandler и FileHandler для записи логов в консоль и файл соответственно.
● filename: путь к файлу, в который будут записываться логи. 
    В нашем примере мы записываем логи в файл /path/to/django.log.
    Внимание! Каталог path/ и вложенный в него каталог to/ необходимо создать самостоятельно. 
    Либо исправьте значение на django.log, чтобы создать файл логов в корневой директории проекта.
● level: минимальный уровень логирования, который будет записываться.
    В нашем примере мы указали уровень INFO для логгера django и уровень DEBUG для логгера myapp.
● propagate: если значение равно True, то сообщения будут передаваться родительским логгерам. 
    Если значение равно False, сообщения не будут передаваться родительским логгерам.
'''

====================================================
============ ЛЕКЦИЯ 2 ==============================
====================================================

# Определение моделей
Перейти в файл models.py внутри вашего приложения и определить класс Python, который будет наследоваться
от базового класса "models.Model".
from django.db import models
    class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField()

# Поля модели и их типы
1. CharField - поле для хранения строковых данных. Параметры: max_length (максимальная длина строки), blank (может ли поле быть пустым), null (может ли поле содержать значение Null), default (значение по умолчанию).
2. IntegerField - поле для хранения целочисленных данных. Параметры: blank, null, default.
3. TextField - поле для хранения текстовых данных большой длины. Параметры: blank, null, default.
4. BooleanField - поле для хранения логических значений (True/False). Параметры: blank, null, default.
5. DateField - поле для хранения даты. Параметры: auto_now (автоматически устанавливать текущую дату при создании объекта), auto_now_add (автоматически устанавливать текущую дату при добавлении объекта в базу данных), blank, null, default.
6. DateTimeField - поле для хранения даты и времени. Параметры: auto_now, auto_now_add, blank, null, default.
7. ForeignKey - поле для связи с другой моделью. Параметры: to (имя модели, с которой устанавливается связь), on_delete (действие при удалении связанного объекта), related_name (имя обратной связи). 
(пример: customer = models.ForeignKey(User, on_delete=models.CASCADE) - каждый заказ делает конкретный пользователь. У одного пользователя может быть несколько заказов, но заказ числится за одним пользователем)
8. ManyToManyField - поле для связи с другой моделью в отношении "многие-ко-многим". Параметры: to, related_name. 
(пример: products = models.ManyToManyField(Product) - заказа может содержать несколько разных продуктов. А продукт может входит в состав нескольких разных заказов.)
9. DecimalField - поле для хранения десятичных чисел. Параметры: max_digits (максимальное количество цифр), decimal_places (количество знаков после запятой), blank, null, default. 10.EmailField - поле для хранения электронной почты. Параметры: max_length, blank, null, default.
10. ImageField - **pip install Pillow** . Данная библиотека нужна для работы Python с изображениями.

Полный список всех полей Django доступен по ссылке: https://docs.djangoproject.com/en/4.2/ref/models/fields/#model-field-types

## Миграции
# создать миграции
чтобы создать миграции, мы должны выполнить следующую команду:
python manage.py makemigrations <myapp> # без <myapp> пройдет миграция по всем прилоджениям
пример: python manage.py makemigrations modelapp2

# Применить миграции
python manage.py migrate


## Cоздании собственных команд manage.py - файлов при запуске который происходит какое-либо действие
# Создаём структуру каталогов
myproject/
    manage.py
    modelapp2/
        __init__.py
        management/
            __init__.py
            commands/
                __init__.py
                my_command.py
        ...
    ...

# создаём файл c командой my_command.py
from django.core.management.base import BaseCommand
class Command(BaseCommand):
    help = "Print 'Hello world!' to output."    
    def handle(self, *args, **kwargs):
        self.stdout.write('Hello world!') # self - указатель самого на себя
                                          # stdout - стандартный вывод
                                          # write - функция для записи в консоль

# Файл my_command.py можно запускать из терминала командой
python manage.py my_command -h   # -h для справки

## Работа с данными в моделях (CRUD):
# Создание объектов модели, create
modelapp2/management/commands/create_user.py:
from django.core.management.base import BaseCommand
from modelapp2.models import User
class Command(BaseCommand):
    help = "Create user."
    def handle(self, *args, **kwargs):
        user = User(name='John', email='john@example.com', password='secret', age=25) # создаём модель пользователя
        user.save() # создаём экземпляр класса и сохраняем
        self.stdout.write(f'{user}') # Выведем данные в консоль

# Получение объектов модели из базы данных, read
"all()" , "get()", "filter()" класса модели. 
Метод "all()" возвращает все объекты модели:
modelapp2/management/commands/get_all_users.py:
from django.core.management.base import BaseCommand
from modelapp2.models import User
class Command(BaseCommand):
    help = "Get all users."
    def handle(self, *args, **kwargs):
        users = User.objects.all()
        self.stdout.write(f'{users}')

Вызов - python manage.py get_all_users


метод "get()" возвращает один объект
modelapp2/management/commands/get_user.py:
from django.core.management.base import BaseCommand
from modelapp2.models import User
class Command(BaseCommand):
    help = "Get user by id."
    def add_arguments(self, parser): # этот метод посде вызова команды позволит принимать аргументы
        parser.add_argument('id', type=int, help='User ID') # Принимаем id
    def handle(self, *args, **kwargs):
        id = kwargs['id']
        user = User.objects.get(id=id) # ide ругается на id!!!!
        self.stdout.write(f'{user}')

Вызов - python manage.py get_user 2     # где 2 - id


метод "filter()":
from django.core.management.base import BaseCommand
from modelapp2.models import User
class Command(BaseCommand):
    help = "Get user by id."
    def add_arguments(self, parser): # этот метод посде вызова команды позволит принимать аргументы
        parser.add_argument('pk', type=int, help='User ID') # Принимаем id
    def handle(self, *args, **kwargs):
        pk = kwargs['pk'] # меняем id на pk - pk - primary key, первичный ключ в таблице, т.е. ID.
        user = User.objects.filter(pk=pk).first()
        self.stdout.write(f'{user}')

# Фильтрация объектов модели:
Для фильтрации объектов модели по заданным условиям можно использовать
метод filter(): Model.objects.filter(param__filter=value)
Model - название модели
objects - зарезервированное слово для работы с моделями
filter - фильтрация
param__filter - параметр фильтра
value - значение

param__filter:
● exact - точное совпадение значения поля
● iexact - точное совпадение значения поля без учета регистра
● contains - значение поля содержит заданный подстроку
● icontains - значение поля содержит заданный подстроку без учета регистра
● in - значение поля находится в заданном списке значений
● gt - значение поля больше заданного значения
● gte - значение поля больше или равно заданному значению
● lt - значение поля меньше заданного значения
● lte - значение поля меньше или равно заданному значению
● startswith - значение поля начинается с заданной подстроки
● istartswith - значение поля начинается с заданной подстроки без учета регистра
● endswith - значение поля заканчивается на заданную подстроку
● iendswith - значение поля заканчивается на заданную подстроку без учета регистра
● range - значение поля находится в заданном диапазоне значений
● date - значение поля является датой, соответствующей заданной дате
● year - значение поля является годом, соответствующим заданному году
i - перед фильтром - поиск без учета регистра (пр exact и iexact)
***Более подробно познакомиться с возможностью фильтров для методов filter(), exclude() и get() можно на официальном сайте https://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookups***
ПР: user = User. Objects.filter(age__gt=age) # > age больше age


# Изменение объектов модели, update
Для изменения объектов модели можно использовать методы поиска get() илиfilter() в сочетании с save() экземпляра класса модели. Например, чтобы изменить имя пользователя с заданным id, мы можем использовать
следующий код в файле 
modelapp2/management/commands/update_user.py:
from django.core.management.base import BaseCommand
from modelapp2.models import User
class Command(BaseCommand):
    help = "Update user name by id."
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('name', type=str, help='User name')
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        user = User.objects.filter(pk=pk).first()
        user.name = name    # name найденого пользователя меняем на name переданное из командной строки
        user.save() # сохраняем в базу
        self.stdout.write(f'{user}')

Выполним команду > python manage.py update_user 2 Smith


# Удаление объектов модели, delete
modelapp2/management/commands/delete_user.py:
from django.core.management.base import BaseCommand
from modelapp2.models import User
class Command(BaseCommand):
    help = "Delete user by id."
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()
        if user is not None:
            user.delete()
        self.stdout.write(f'{user}')


## Дополнительные возможности моделей
# Связи между моделями
ForeignKey - один ко многим
ManyToManyField - многие ко многим 
OneToOneField - один к одному


# Использование QuerySet для получения данных из базы данных
Например, чтобы получить все посты, написанные определенным автором, мы можем использовать следующий код в файле
modelapp2/management/commands/get_post_by_author_id.py:


# Создание пользовательских методов
Например, мы можем создать метод "get_summary" для модели "Post", который будет возвращать краткое описание поста. Внесём изменения в класс Post в файле models.py:
def get_summary(self):
    words = self.content.split()
    return f'{" ".join(words[:12])}...'
Здесь мы создаем метод "get_summary", который возвращает первые 12 слов
контента поста и добавляет многоточие в конце.
в зпросе можно указать:
    text = '\n'.join(post.get_summary() for post in posts)