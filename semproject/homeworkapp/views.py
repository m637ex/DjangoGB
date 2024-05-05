from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
import logging
from .forms import ImageForm 
from .models import Client, Product, Order, PhotoProduct
from django.utils import timezone
from django.core.files.storage import FileSystemStorage # для работы с файлами и картинками

logger = logging.getLogger(__name__)

_links_menu = [ # список ссылок для меню
    {'url': '/hw/',
        'name': 'Главная'},
    {'url': '/hw/about/',
        'name': 'Обо мне'},
    {'url': '/hw/store/',
        'name': 'Магазин'},
    {'url': '/hw/clients/',
        'name': 'Все клиенты'},
    {'url': '/hw/products/',
        'name': 'Все товары'},    
]

def index(request):
    context = {
        "title": "Главная страница",
        'links_menu': _links_menu,
    }
    logger.info('Index page accessed')    
    context['content'] = "Это мой первый сайт и он работает!!!!"
    context['image_url'] = "/images/cat.jpg"
    return render(request, "homeworkapp/index.html", context=context)
    # return HttpResponse(html_index)

def about(request):   
    context = {
        "title": "Обо мне",
        "name": "Andrey",
        'links_menu': _links_menu,
    } 
    logger.info('About page accessed')
    context['content'] = "Это мой первый сайт и он работает!!!!"
    context['image_url'] = "/images/foto.jpg"
    return render(request, "homeworkapp/about.html", context=context)
    # return HttpResponse(html_about)

def store(request):    
    context = {
        "title": "Магазин",
        'links_menu': _links_menu,
    } 
    logger.info('Store page accessed')
    context['content'] = "Это мой первый сайт и он работает!!!!"
    return render(request, "homeworkapp/store.html", context=context)
    # return HttpResponse('<h1>Store page accessed</h1>')
    
# Представление для отображения всех клиентов
def all_clients(request):
    context = {
        "title": "Все клиенты",
        'links_menu': _links_menu,
    } 
    context['clients'] = Client.objects.all()
    logger.info('all_clients_view page accessed')
    # return HttpResponse('<h1>Store page accessed</h1>')
    return render(request, 'homeworkapp/all_clients.html', context=context)

# Представление для отображения заказов клиентов
def all_product_clients(request, client_id, days):
    context = {
        "title": "Все товары из заказа клиента",
        'links_menu': _links_menu,
    } 
    
    # Определите дату, за которую вы хотите получить заказы
    end_date = timezone.now()
    start_date = end_date - timezone.timedelta(days=days)   
    
    # Получаем все заказы клиента за заданный период времени
    all_orders = Order.objects.filter(customer=client_id, date_created__range=(start_date, end_date)) # В Django __range используется для фильтрации объектов, которые попадают в определенный диапазон значений

    
    # Получите список товаров из всех заказов клиента
    ordered_products = []
    for order in all_orders:
        ordered_products.extend(order.products.all())
    
    # Удалите повторяющиеся товары из списка
    unique_ordered_products = list(set(ordered_products))  
    print(unique_ordered_products)
    
    # Отсортируйте товары по времени заказа
    sorted_ordered_products = sorted(unique_ordered_products, key=lambda x: x.date_created, reverse=True)

    
    context['products'] = sorted_ordered_products  
    
    # context['clients'] = Client.objects.all()
    logger.info('all_product_clients page accessed')
     
    # return HttpResponse(unique_ordered_products)
    return render(request, 'homeworkapp/all_product_clients.html', context=context)

def all_products(request):    
    context = {
        "title": "Все товары",
        'links_menu': _links_menu,
    } 
    context['products'] = Product.objects.all()
    logger.info('all_products_view page accessed')
    # return HttpResponse('<h1>All_products_view page accessed</h1>')
    return render(request, 'homeworkapp/all_products.html', context=context)


def upload_image(request, product_id):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            try:
                product = Product.objects.get(pk=product_id) # Используем get() для получения конкретного объекта Product по его id
            except Product.DoesNotExist:
                # Обработка случая, когда объект Product не найден
                return HttpResponse("Product does not exist")
            
            # Создаем экземпляр PhotoProduct, связанный с найденным товаром
            product_image = PhotoProduct(product=product, image=image)
            product_image.save()
    else:
        form = ImageForm()    
    context = {
        "title": "Все товары",
        'links_menu': {'url': '/hw/products/',
                       'name': 'Все товары'},
        'form': form,
        'title': 'Download Photo Product'
    } 
    return render(request, 'homeworkapp/upload_image.html', context)

