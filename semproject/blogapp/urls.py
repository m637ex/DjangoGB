from django.urls import path
from . import views # или from views import index # тогда далее index вместо views.index

urlpatterns = [
    path('', views.index, name='index'),    
    path('about', views.about, name='about'),   
    path('view_authors/', views.view_authors, name='view_authors'),
    path('create_author/', views.create_author, name='create_author'),    
]
 