from django.contrib import admin
from . models import *

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'message', 'status', 'when_sent', 'last_updated']
admin.site.register(Contact, ContactAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'img', 'slug', 'description']
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'name', 'slug', 'imgr', 'price', 'max_quantity', 'min_quantity',
     'description', 'shoes', 'bag', 'perfume', 'cloth', 'uploaded', 'updated']
admin.site.register(Product, ProductAdmin)
