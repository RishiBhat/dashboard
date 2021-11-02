from django.urls import path, re_path
from .import views
from django.contrib import admin

urlpatterns = [
    # dashboard is included here 
    
    path('cxdash/', views.cxdash, name="cxdash"),
    path('', views.customerapp, name="customerapp"),
    path('product_inventory/', views.product_inventory, name="product_inventory"),
]