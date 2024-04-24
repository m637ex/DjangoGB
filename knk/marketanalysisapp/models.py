from django.db import models

# Create your models here.

# class Inpars_cache(models.Model): # модель по inpars json запросу. https://inpars.ru/api/v2/estate?access-token=8XAn0yBldZqPGNKL64fBtfpkIEK3Cx5P&sourceId=1&withAgent=1&parseId=3632582681
#     id = models.IntegerField(primary_key=True)
#     regionId = models.IntegerField()
#     cityId = models.IntegerField()
#     metroId = models.IntegerField()
#     typeAd = models.IntegerField()
#     sectionId = models.IntegerField()
#     categoryId = models.IntegerField()
#     title = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     floor = models.IntegerField()
#     floors = models.IntegerField()
#     sq = models.FloatField()
#     sqLand = models.FloatField(null=True)
#     cost = models.IntegerField()
#     text = models.TextField()
#     images = models.JSONField()
#     lat = models.CharField(max_length=20)
#     lng = models.CharField(max_length=20)
#     name = models.CharField(max_length=255, null=True)
#     phones = models.JSONField(null=True)
#     url = models.URLField()
#     agent = models.IntegerField()
#     source = models.CharField(max_length=20)
#     sourceId = models.IntegerField()
#     created = models.DateTimeField()
#     updated = models.DateTimeField()

#     def __str__(self):
#         return self.title