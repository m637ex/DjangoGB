## Работа с административной панелью

cd myproject
python manage.py startapp myapp5
python manage.py runserver

http://127.0.0.1:8000/admin

settings.py:
LANGUAGE_CODE = 'ru-ru'

# Создание суперпользователя
python manage.py createsuperuser

смена пароля
python manage.py changepassword <username>
admin
lesson - Aa!030586 
seminar- Aa!123123

## Добавление пользовательских моделей в административную панель
# Создание моделей
создаём модель в models.py

Мигрируем:
python manage.py makemigrations myapp5
python manage.py migrate

# Подключение моделей к административной панели
Открываем файл admin.py приложения

# Персонализация моделей в админ панели

# Настройка списка изменения
***Отображение дополнительных полей***
в admin.py

from django.contrib import admin
from .models import Category, Product

@admin.action(description="Сбросить количество в ноль") #- Добавление новых действий по выбору галочкой в админке
def reset_quantity(modeladmin, request, queryset): # модель, запрос, данные
queryset.update(quantity=0)
class ProductAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['name', 'category', 'quantity'] #- Отображение дополнительных полей
    ordering = ['category', '-quantity'] #- Сортировка строк
    list_filter = ['date_added', 'price'] #- Добавление фильтрации в список изменения
    search_fields = ['description'] #- Текстовый поиск
        search_help_text = 'Поиск по полю Описание продукта (description)' #- Текстовый поиск (подсказка)
    actions = [reset_quantity] #- Добавление новых действий с декоратором @admin.action
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)

***Настройка изменения отдельной записи***
class ProductAdmin(admin.ModelAdmin):
    """Отдельный продукт."""
    fields = ['name', 'description', 'category', 'date_added', 'rating'] # поля видимые
    readonly_fields = ['date_added', 'rating'] # поля только для чтения

***Детальная настройка отображения полей***
переменная fieldsets противоречит fields, поэетому её закомментируем

   fieldsets = [
    (
        None,
        {
            'classes': ['wide'], # wide - максимально широко
            'fields': ['name'], # поле name из БД
        },
    ),
    (
        'Подробности', # Блок "подробности"
        {
            'classes': ['collapse'], # collapse - поле схлопнулось(скрыто)
            'description': 'Категория товара и его подробное описание', # описание
            'fields': ['category', 'description'], # поля из БД
        },
    ),
    (
        'Бухгалтерия', # Блок
        {
            'fields': ['price', 'quantity'], # поля из БД
        }
    ),
    (
        'Рейтинг и прочее', # Блок
        {
            'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
            'fields': ['rating', 'date_added'], # поля из БД
        }
    ),
]

