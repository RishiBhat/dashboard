# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.forms import AdminPasswordChangeForm
from django.db import models
from django.contrib.auth.models import User


# Create your models here.




class Station(models.Model):
    name=models.CharField(max_length=500, unique=True) 
    email=models.EmailField(max_length=254)
    number=models.IntegerField(default=20)
    address = models.TextField(max_length=10000)
    location= models.CharField(max_length=100)
    city=models.CharField(max_length=500)
    country=models.CharField(max_length=50)                                
    state=models.CharField(max_length=50)                                
    
    maritialstatus=models.CharField(max_length=50,
    
                                    choices=    (
                                        ('Married','married'),
                                        ('Engaged','engaged'),
                                        ('Unmarried','unmarried'),
                                        ),)

    urimage=models.ImageField(upload_to='image/', default='', blank=True)
    urdoc=models.FileField(upload_to='files/', blank=True)
    date_time=models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.name    


#Now I will add up the ecommerce products from here

class Product(models.Model):
    prname=models.CharField(max_length=5000)
    prtype=models.CharField(max_length=5000)
    prprice=models.IntegerField(default=50)
    prname=models.CharField(max_length=5000)
    prdesc=models.CharField(max_length=5000)
    primage=models.ImageField(upload_to='image/', default='')
    prdate_time=models.DateTimeField(auto_now_add=True, null=True)
    prqty=models.IntegerField(default=50)

    def __str__(self):
        return self.prname