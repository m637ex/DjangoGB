from django.db import models
from django.utils import timezone

# Create your models here.

class Coin(models.Model): # Орёл или решка
    site = models.CharField(max_length=10) # стороная монеты
    datatime = models.DateTimeField(default=timezone.now)
    
    @staticmethod   # статический метод, принадлежит классу а не экземплюяру класса.
    def last_five_values(): # 5 последних значений        
        value = Coin.objects.order_by('-datatime')[:5]    # order_by - сортируем по столбцу datatime где - сортировка в обратном порядке [:5] - срез
        # print(value)
        return value

    def __str__(self):
        return f'Выпало {self.site}, время: {self.datatime}'



