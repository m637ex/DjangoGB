from django.db import models

# Create your models here.


class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.CharField(max_length=1000)
    birthday = models.DateField()

    def full_name(self):
        return f'{self.firstname} {self.lastname}'