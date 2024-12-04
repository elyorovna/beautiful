from django.db import models

# Create your models here.

class Maxsulot(models.Model):
    nomi = models.CharField(max_length=20)
    bio = models.TextField()
    narxi = models.IntegerField()
    rasm = models.ImageField(upload_to='maxsulot/')

    def __str__(self):
        return self.nomi


class Korinish(models.Model):
    nomi = models.CharField(max_length=30)
    bio = models.TextField()
    rasmi = models.ImageField(upload_to='korinish/')

    def __str__(self):
        return self.nomi


class Xaridor(models.Model):
    ismi = models.CharField(max_length=20)
    bio = models.TextField()
    rasmi = models.ImageField(upload_to='xaridor/')

    def __str__(self):
        return self.ismi















