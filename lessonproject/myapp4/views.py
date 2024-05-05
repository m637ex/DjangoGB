from django.shortcuts import render

# Create your views here.

import logging
from .forms import UserForm, ManyFieldsForm, ManyFieldsFormWidget, ImageForm # импортируем из файла forms.py
from .models import User
from django.core.files.storage import FileSystemStorage # для работы с файлами и картинками



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

def many_fields_form(request):
    if request.method == 'POST':
        # form = ManyFieldsForm(request.POST)
        form = ManyFieldsFormWidget(request.POST)
        if form.is_valid():
            # Делаем что-то с данными
            logger.info(f'Получили {form.cleaned_data=}.')
    else:
        # form = ManyFieldsForm()
        form = ManyFieldsFormWidget(request.POST)
    return render(request, 'myapp4/many_fields_form.html', {'form': form})

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f'Получили {name=}, {email=}, {age=}.')
            user = User(name=name, email=email, age=age)
            user.save()
            message = 'Пользователь сохранён'
    else:
        form = UserForm()
        message = 'Заполните форму'
    return render(request, 'myapp4/user_form.html', {'form': form, 'message': message})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage() # экземпляр файл систем стор
            fs.save(image.name, image) # сохраним объект image в файл image.name
    else:
        form = ImageForm()
    return render(request, 'myapp4/upload_image.html', {'form':form})