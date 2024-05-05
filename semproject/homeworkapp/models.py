from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=100) # — имя клиента
    email = models.EmailField() # — электронная почта клиента
    phone = models.CharField(max_length=16) # — номер телефона клиента
    address = models.TextField() # — адрес клиента
    date_created = models.DateTimeField(auto_now_add=True) # — дата регистрации клиента
    
    def __str__(self):
        return f'Name: {self.name}, email: {self.email}, phone: {self.phone}, address: {self.address}'
    
     
class Product(models.Model):
    name = models.CharField(max_length=100) # — название товара
    description = models.TextField() # — описание товара
    price = models.DecimalField(max_digits=8, decimal_places=2) # — цена товара
    quantity = models.IntegerField() # — количество товара
    date_created = models.DateTimeField(auto_now_add=True) # — дата добавления товара
    
    def __str__(self):
        return f'Name: {self.name}, description: {self.description}, price: {self.price}, quantity: {self.quantity}'
    

class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE) # при удалении Client удаляются все его Order — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
    products = models.ManyToManyField(Product) # — связь с моделью «Товар», указывает на товары, входящие в заказ
    total_price = models.DecimalField(max_digits=16, decimal_places=2) # — общая сумма заказа
    date_created = models.DateTimeField(auto_now_add=True) # — дата создания заказа
    

class PhotoProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='photos') # добавили поле related_name='photos' для обратной связи от Product к PhotoProduct, чтобы упростить доступ к фотографиям товара.
    image = models.ImageField(upload_to='products/') # pip install Pillow