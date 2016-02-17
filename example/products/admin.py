# coding: utf-8
from django.contrib import admin

from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
admin.site.register(Product, ProductAdmin)
