from django.urls import path, re_path
from .import views
from django.contrib import admin

urlpatterns = [
    # dashboard is included here 
    
    path('cxdash/', views.cxdash, name="cxdash"),
    path('', views.customerapp, name="customerapp"),
    path('product_inventory/', views.product_inventory, name="product_inventory"),
    path('contact/', views.contact, name="contact"),
    path('checkout/', views.checkout, name="checkout"),
    path('clogin/', views.login_temp, name="clogin"),
    
]