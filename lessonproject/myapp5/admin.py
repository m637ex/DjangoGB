from django.contrib import admin

# Register your models here.
from .models import Category, Product

@admin.action(description="Сбросить количество в ноль") #- Добавление новых действий(пр. сбросить счетчик)
def reset_quantity(modeladmin, request, queryset): # модель, запрос, данные
    queryset.update(quantity=0)

class ProductAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['name', 'category', 'quantity'] #- Отображение дополнительных полей
    ordering = ['category', '-quantity'] #- Сортировка строк по category 2 по quantity в обратном порядке
    list_filter = ['date_added', 'price'] #- Добавление фильтрации в список изменения
    search_fields = ['description'] #- Текстовый поиск
    search_help_text = 'Поиск по полю Описание продукта (description)' #- Текстовый поиск (подсказка)
    actions = [reset_quantity] #- Добавление новых действий с декоратором @admin.action и ф-ей reset_quantity()
    """Отдельный продукт."""
    #fields = ['name', 'description', 'category', 'date_added', 'rating'] # поля видимые
    readonly_fields = ['date_added', 'rating'] # поля только для чтения
    """Детальная настройка отображения полей переменной fieldsets, противоречит fields"""
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
    
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)