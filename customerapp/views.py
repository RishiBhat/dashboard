from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ContactForm
from .import views
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Contact
from django.shortcuts import render, redirect
from app.models import Product
from app.forms import ProductForm
from math import ceil
from django.contrib.auth.decorators import login_required

# Create your views here.


def customerapp(request):
    prod_disc = Product.objects.all()
    for i in prod_disc:
        print("===========================////////////////////", i.prname)
        print("++++++++++++++++++", i.prprice)
    return render(request, 'customerapp/cxabout.html', {'prod_disc': prod_disc})


def product_inventory(request):
    prod_get = Product.objects.all()
    return render(request, 'customerapp/product_display.html', {'prod_get': prod_get})


# Contact page form


def contact(request):
    cxd = ContactForm(request.POST or None, request.FILES or None)
    if cxd.is_valid():
        cxd.save()
        return redirect('contact')
    return render(request, 'customerapp/cxcontact.html', {'cxd': cxd})


# creating a customer dashboard


@login_required(login_url="login")
def cxdash(request):
    allProds = []
    catprods = Product.objects.values('prtype','id')
    cats = {item['prtype'] for item in catprods}
    for cat in cats:
        prd = Product.objects.filter(prtype=cat)
        n = len(prd)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prd, range(1, nSlides), nSlides])
    points = {'allProds': allProds}
    return render(request, 'customerindex.html', points)
  

def register(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['pwd']
        pwdcheck = request.POST['pwdcheck']

        # check for errorneous input
        if len(username) < 10:
            messages.error(
                request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(
                request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pwd != pwdcheck):
            messages.error(request, " Passwords do not match")
            return redirect('home')

        # Create the user
        myuser = User.objects.create_user(username, email, pwd)
        myuser.username = username
        myuser.save()
        messages.success(
            request, " Your Account has been successfully created")
        return redirect('register')
    else:
        return HttpResponse("404 - Not found")


def login(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("cxdash")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("cxdash")
    return HttpResponse("404- Not found")
    return HttpResponse("login")


def logout(request):
    messages.success(request, "Successfully logged out")
    return redirect('cxdash')


def checkout(request, id):
    gt = Product.objects.all()
    for i in gt:
        print("================================================>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",i.id)
    if request.method == 'POST':
        prqty = request.POST['prqty']
    if len(prqty) > 10:
        messages.error(request, "Your added quantity can not be satisfied")
        return redirect('cxdash')
    return render(request, 'customerapp/checkout.html', {'gt': gt})
