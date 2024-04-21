from django.urls import path
from . import views # или from views import index # тогда далее index вместо views.index

urlpatterns = [
    path('', views.index, name='index'),    
    path('heads_or_tails/', views.heads_or_tails, name='heads_or_tails'),
    path('cube6/', views.cube6, name='cube6'),
    path('random100/', views.random100, name='random100'),
]
