from django.urls import path
from . import views # или from views import index # тогда далее index вместо views.index
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),    
    path('about/', views.about, name='about'),
    path('store/', views.store, name='store'),
    path('clients/', views.all_clients, name='all_clients'),
    path('clients/<int:client_id>/all_product_clients/<int:days>', views.all_product_clients, name='all_product_clients'),    
    path('products/', views.all_products, name='all_products'),
    path('upload/<int:product_id>/', views.upload_image, name='upload_image'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# /<int:days>