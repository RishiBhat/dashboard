# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.core.exceptions import NON_FIELD_ERRORS
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template


@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

def dash(request):
    return render(request,'index.html')


def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')


#---------------------will start the user portfolio tempering from here---------------------> 

from .models import Station, Product
from .forms import ProductForm, StationForm 

#This is the user profile formm which is been made here , now  I will post the query here

def user_profile(request):
    userfm=StationForm(request.POST or None, request.FILES or None)
    userfm1=Station.objects.all()
    for i in userfm1: 
        print(i.name)
    if userfm.is_valid():
        userfm.save()
        return redirect('user_profile')
    return render(request,'rishi_forms.html',{'userfm':userfm})


def dashboard(request):
  
  #This is for the user object display, we declare different variables
    disck= Station.objects.all()
    
  #This is for the products display  
    prdisck=Product.objects.all()



    return render(request,'rishi_index.html',{'disck': disck,'prdisck':prdisck })


def update(request,id):
        takidd = Station.objects.get(id=id) 
        
        userfm = StationForm(instance=takidd, data=request.POST or None, files=request.FILES or None)
        if request.POST:
            if userfm.is_valid:
                print(userfm.name)
                userfm.save()
                return redirect('/')
        return render(request,'rishi_forms.html',{'userfm':userfm})


def delete(request,id):
    de=Station.objects.get(id=id)
    de.delete()
    
    return redirect('/dashboard')




#--------------->> Here we are adding the product listing done here


def product_form(request):
    prform=ProductForm(request.POST or None, request.FILES or None)
    if prform.is_valid():
        prform.save()
        return redirect('product_form')
    return render(request,'product_form.html', {'prform':prform })




def product_update(request,id):
    prodid=Product.objects.get(id=id)
    prform = ProductForm(instance=prodid, data=request.POST or None, files=request.FILES or None)
    
    if request.POST:
        if prform.is_valid():
            prform.save()
            return redirect('dashboard')
    return render(request,'product_form.html', {'prform':prform})


def product_delete(request,id):
    prodel=Product.objects.get(id=id)
    prodel.delete()
    return redirect('dashboard')





#inclduing the quickview for the product

def product_quickview(request,id):
    prolist=Product.objects.get(id=id)
    return render(request, 'prolist.html',{'prolist':prolist})



#include here to map the products for the cx
def product_display(request):
    showpr= Product.objects.all()   
    return render(request,'product_display.html',{'showpr':showpr})
