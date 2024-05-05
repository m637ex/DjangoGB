# Формы!!!

формы в Django начинается с создания класса формы, который наследуется от класса forms.Form

.\.venv\Scripts\activate    
python manage.py startapp myapp4

# Создание форм
формы пишутся в файле form.py d корне приложения:

from django import forms
class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=0, max_value=120)

# Представление для формы
формы обрабатывают post запросы

создадим  view.py
import logging
from .forms import UserForm # импортируем из файла forms.py

logger = logging.getLogger(__name__)

def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST) # заполняем форму полученными данными возвращенными пользователем
        if form.is_valid(): # если прошли валидацию сохраняем данные в переменных.
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # Делаем что-то с данными
            logger.info(f'Получили {name=}, {email=}, {age=}.')
    else:
        form = UserForm() # создаём пустой экземпляр класса формы
    return render(request, 'myapp4/user_form.html', {'form': form}) # открываем страницу отправляем форрму на неё

# Прописываем url
в файле проекта urls.py:

urlpatterns = [
path('admin/', admin.site.urls),
...
path('les4/', include('myapp4.urls')),
]

создадим файл приложения urls.py:
from django.urls import path
from .views import user_form

urlpatterns = [
    path('user/add/', user_form, name='user_form'),
]

# Отрисовка шаблона
шаблон user_form.html

{% extends 'base.html' %}
{% block content %}
  <form action="" method="post"> # action="" - форма отправляется по тому же адресу что и пришла методом post
    {% csrf_token %} # - шиврование безопасности
    {{ form }} № - сама форма
    <input type="submit" value="Отправить" />
  </form>
{% endblock %}

# Поля форм
Перечислим некоторые из наиболее популярных классов Field в Django:
● CharField — используется для создания текстовых полей, таких как имя, фамилия, электронная почта и т.д.
● EmailField — используется для создания поля электронной почты.
● IntegerField — используется для создания поля для ввода целых чисел.
● FloatField — используется для создания поля для ввода чисел с плавающей точкой.
● BooleanField — используется для создания поля флажка.
● DateField — используется для создания поля даты.
● DateTimeField — используется для создания поля даты и времени.
● FileField — используется для создания поля для загрузки файла.
● ImageField — используется для создания поля для загрузки изображения.
● ChoiceField — используется для создания выпадающего списка с выбором одного из нескольких вариантов.


# Виджеты форм
Вот некоторые из наиболее популярных классов виджетов в Django:
● TextInput — используется для создания текстового поля ввода.
● EmailInput — используется для создания поля ввода электронной почты.
● PasswordInput — используется для создания поля ввода пароля.
● NumberInput — используется для создания поля ввода чисел.
● CheckboxInput — используется для создания флажка.
● DateInput — используется для создания поля ввода даты.
● DateTimeInput — используется для создания поля ввода даты и времени.
● FileInput — используется для создания поля загрузки файла.
● Select — используется для создания выпадающего списка с выбором одного из нескольких вариантов.
● RadioSelect — используется для создания списка радиокнопок.
● Textarea — используется для создания многострочного текстового поля ввода.

создадим класс class ManyFieldsFormWidget(forms.Form): в form.py c их использованием


# Обработка данных форм
## Пользовательская валидация данных с помощью метода clean_()
в forms.py

class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=0, max_value=120)
    def clean_name(self): # данном случае clean_ для name
    """Плохой пример. Подмена параметра min_length."""
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError('Имя должно содержать не менее 3 символов')
        return name

# !!!!!!!!!Сохранение формы в базу данных!!!!!!!!!!!!!!
Обычное использование - сохранение в базу данных.
## Модель данных
Начнём с создания модели.Для этого в файле myapp4/models.py пропишем следующий код:

from django.db import models
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    def __str__(self):
        return f'Name: {self.name}, email: {self.email}, age: {self.age}'

Перед тем как продолжить создадим и применим миграции:
python manage.py makemigrations myapp4
python manage.py migrate

## Представление
создаём новое предствление в view.py

## Маршрут
добавляем сылку в urls.py


# !!!!!!!!! Сохранение изображений (файлов) !!!!!!!!!!!
Загрузка изображений через форму Django происходит с помощью класса виджета ImageField
Файлов - а FileField

forms.py:
class ImageForm(forms.Form):
    image = forms.ImageField()

# Настройка settings.py
пропишем следующие пару констант:
...
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Представление views.py
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'myapp4/upload_image.html', {'form':form})

# Маршрут urls.py
path('upload/', upload_image, name='upload_image'),

#  создать шаблон upload_image.html
{% extends 'base.html' %}

{% block content %}
  <h2>Загрузите изображение</h2>
  <form method="post" enctype="multipart/form-data"> # enctype="multipart/form-data" для рабоыт формы с файлами
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Загрузить</button>
  </form>
{% endblock %}

Важно! Чтобы форма отправляет файлы необходимо в теге форм прописать enctype="multipart/form-data". Без этого мы не получим доступ к файлам.
