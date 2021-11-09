from django.db import models

# Create your models here.




from django.contrib.auth.forms import AdminPasswordChangeForm
from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    cxname=models.CharField(max_length=50)
    cxemail=models.EmailField(max_length=254)
    subject=models.CharField(max_length=75)
    message=models.TextField(max_length=100)

    def __str__(self):
        return self.cxname


#including the order details here 
class Orders(models.Model):
    
    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=90)
    email = models.EmailField(max_length=111)    
    
    def __str__(self):
        return self.name

class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."

