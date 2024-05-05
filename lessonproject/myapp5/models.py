from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(default='', blank=True)
    price = models.DecimalField(default=999999.99, max_digits=8, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=0) # Positive - положительное, SmallInteger - целое, Field - поле
    date_added = models.DateTimeField(auto_now_add=True) # auto_now_add - текущая дата
    rating = models.DecimalField(default=5.0, max_digits=3, decimal_places=2) # max_digits=3 - 0-9.99

    
    def __str__(self):
        return self.name
