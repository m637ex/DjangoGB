from django.urls import path
from . import views # или from views import index # тогда далее index вместо views.index

urlpatterns = [
    path('', views.index, name='index'),    
    path('about/', views.about, name='about'),
    path('store/', views.store, name='store'),
    path('clients/', views.all_clients, name='all_clients'),
    path('clients/<int:client_id>/all_product_clients/<int:days>', views.all_product_clients, name='all_product_clients'),    
]
# /<int:days>