from django.contrib import admin

from api.models import Products, Customers

# Register your models here.
admin.site.register(Customers)
admin.site.register(Products)