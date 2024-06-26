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