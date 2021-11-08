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