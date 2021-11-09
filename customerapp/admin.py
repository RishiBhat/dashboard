from django.contrib import admin
from .models import Contact, Orders, OrderUpdate
# Register your models here.



admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)

