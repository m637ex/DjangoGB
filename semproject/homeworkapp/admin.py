from django.contrib import admin

# Register your models here.
from .models import Product, Client, Order

#class ProductAdmin(admin.ModelAdmin):

# обнулим колличество
@admin.action(description="Сбросить количество в ноль") #- Добавление новых действий по выбору галочкой в админке
def reset_quantity(modeladmin, request, queryset): # модель, запрос, данные
    queryset.update(quantity=0)

class ProductAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['name', 'description', 'price', 'quantity', 'date_created'] #- Отображение дополнительных полей
    ordering = ['name', 'date_created'] #- Сортировка строк
    list_filter = ['name', 'price', 'quantity', 'date_created'] #- Добавление фильтрации в список изменения
    search_fields = ['name', 'description'] #- Текстовый поиск
    search_help_text = 'Поиск по полю Описание продукта (description) и название товара (name)' #- Текстовый поиск (подсказка)
    actions = [reset_quantity] #- Добавление новых действий с декоратором @admin.action
    """Отдельный продукт."""
    readonly_fields = ['date_created'] # поля только для чтения


class ClientAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['name', 'email', 'phone', 'address', 'date_created'] #- Отображение дополнительных полей
    ordering = ['name', 'date_created'] #- Сортировка строк
    list_filter = ['name', 'date_created'] #- Добавление фильтрации в список изменения
    search_fields = ['name', 'email', 'phone', 'address'] #- Текстовый поиск
    search_help_text = 'Поиск по всем полям' #- Текстовый поиск (подсказка)
    """Отдельный продукт."""
    fieldsets = [
    (
        None,
        {
            'classes': ['wide'], # wide - максимально широко
            'fields': ['name'], # поле name из БД
        },
    ),
    (
        'Контакты', # Блок "подробности"
        {
            'classes': ['collapse'], # collapse - поле схлопнулось(скрыто)
            'description': 'Контакты (email, phone, address)', # описание
            'fields': ['email', 'phone', 'address'], # поля из БД
        },
    ),
    (
        None,
        {
            #'classes': ['wide'], # wide - максимально широко
            'fields': ['date_created'], # поле name из БД
        },
    ),
    ]
    readonly_fields = ['date_created'] # поля только для чтения

class OrderAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['get_customer', 'get_products', 'total_price', 'date_created'] #- Отображение дополнительных полей
    ordering = ['total_price', 'date_created'] #- Сортировка строк
    
    """Отдельный продукт."""    
    fields = ['customer', 'products', 'total_price', 'date_created'] # поля видимые
    readonly_fields = ['date_created'] # поля только для чтения
    
    def get_products(self, obj):
        return ', '.join([f"{p.name}" for p in obj.products.all()]) # получаем список товаров
    get_products.short_description = 'Товары'

    def get_customer(self, obj):
        return obj.customer.name  # получаем только имя

admin.site.register(Product, ProductAdmin) # Регистрируем класс в админке
admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
