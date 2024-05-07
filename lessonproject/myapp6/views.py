from django.shortcuts import render

# Create your views here.

from django.db.models import Sum
from myapp5.models import Product

# Представление для суммирования в БД
def total_in_db(request):
    total = Product.objects.aggregate(Sum('quantity')) # агрегирующий запрос с суммированием всех значений столбца “количество”
    context = {
        'title': 'Общее количество посчитано в базе данных',
        'total': total,
    }
    return render(request, 'myapp6/total_count.html', context)

# Представление для суммирования в представлении
def total_in_view(request):
    products = Product.objects.all()
    total = sum(product.quantity for product in products)
    context = {
        'title': 'Общее количество посчитано в представлении',
        'total': total,
    }
    return render(request, 'myapp6/total_count.html', context)

# Представление для суммирования в модели из шаблона
def total_in_template(request):
    context = {
        'title': 'Общее количество посчитано в шаблоне',
        'products': Product, # Мы передаём модель Product в шаблон
    }
    return render(request, 'myapp6/total_count.html', context)