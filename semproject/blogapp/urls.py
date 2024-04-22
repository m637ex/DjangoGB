from django.urls import path
from . import views # или from views import index # тогда далее index вместо views.index

urlpatterns = [
    path('', views.index, name='index'),    
    path('blog/', views.blog, name='blog'),
]
