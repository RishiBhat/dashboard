from django.shortcuts import render, redirect
from app.models import Product
from app.forms import ProductForm 




# Create your views here.

def cxdash(request):
    return render(request,'customerindex.html')


def customerapp(request): 
    prod_disc=Product.objects.all()
    for i in prod_disc:
        print("===========================////////////////////",i.prname)
        print("++++++++++++++++++",i.prprice)
    return render(request,'customerapp/cxabout.html', {'prod_disc': prod_disc})
    

def product_inventory(request):
    prod_get=Product.objects.all()
    return render(request,'customerapp/product_display.html', {'prod_get': prod_get})



