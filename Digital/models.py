from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null= True)
    email = models.CharField(max_length=200, null= True)
    profile_pic = models.ImageField(null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Principal(models.Model):

    nume = models.CharField(max_length=200, null=True)
    pret = models.IntegerField(null=True)
    descriere =models.CharField(max_length=200, null=True, blank=True)
    poza = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nume


class Desert(models.Model):
    nume = models.CharField(max_length=200, null=True)
    pret = models.IntegerField(null=True)
    descriere = models.CharField(max_length=200, null=True, blank=True)
    poza = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nume


class Bauturi(models.Model):

    nume = models.CharField(max_length=200, null=True)
    pret = models.IntegerField(null=True)
    descriere = models.CharField(max_length=200, null=True, blank=True)
    poza = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nume




