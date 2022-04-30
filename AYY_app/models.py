from django.db import models
from django.forms import PasswordInput

# Create your models here.


class Product(models.Model):

    name = models.CharField(max_length=255)
    price = models.FloatField()
    type = models.CharField(max_length=255)
    reference = models.CharField(max_length=255, unique=True, primary_key=True)
    image_url = models.CharField(max_length=2083)

    def __str__(self):
        return self.name


class user(models.Model):
    
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    dateofcreation = models.DateTimeField(max_length=255)
   
    def __str__(self):
        return self.firstname
