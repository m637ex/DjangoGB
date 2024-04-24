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