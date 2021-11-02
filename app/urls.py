# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from .import views
from django.contrib import admin

urlpatterns = [
    
    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    path('dash/', views.dash, name="dash"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('user_profile', views.user_profile, name="user_profile"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('update/<int:id>',views.update, name="update"),  
    path('delete/<int:id>',views.delete, name="delete"),

    #adding the product url mapping

    path('product_form',views.product_form,name="product_form" ),

    path('product_update/<int:id>',views.product_update,name="product_update"),
    path('product_delete/<int:id>',views.product_delete,name="product_delete"),
    path('product_quickview/<int:id>',views.product_quickview,name="product_quickview"),


    #with this url we map to get the products for the cx

    path('cxdashboard/',views.product_display,name="product_display"),





]
