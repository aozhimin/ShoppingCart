# -*-coding=utf-8-*-
from django.contrib import admin
from .models import Product, Price

class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'brand_type', 'description')
    list_display = ('id', 'name', 'brand_type', 'create_time', 'update_time')
    search_fields = ('id', 'name')


class PriceAdmin(admin.ModelAdmin):
    fields = ('product', 'unit_price', 'config_type')
    list_display = ('id' ,'product', 'unit_price', 'config_type', 'create_time', 'update_time')
    search_fields = ('id', 'product')


# class ProductAdmin(admin.ModelAdmin):
#     fields = ('Product', 'brand_type', 'description', 'price')
#     list_display = ('id', 'name', 'brand_type', 'price', 'create_time', 'update_time')
#     search_fields = ('id', 'name')

admin.site.register(Product, ProductAdmin)
admin.site.register(Price, PriceAdmin)



