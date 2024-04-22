from django.urls import path
from . import views # или from views import index # тогда далее index вместо views.index

urlpatterns = [
    path('', views.index, name='index'),    
    path('coin/', views.coin, name='coin'),    
    path('coin_values/', views.coin_values, name='coin_values'), # последние 5 бросков
    path('cube6/', views.cube6, name='cube6'),
    path('random100/', views.random100, name='random100'),
]
