from django.contrib import admin
from . models import *

# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ('user','product', 'quantity','price','amount','order_no','paid','created_at')
admin.site.register(Cart, CartAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 'amount', 'paid', 'phone', 'pay_code', 'shop_code', 'payment_date', 'admin_update', 'admin_note']
admin.site.register(Payment, PaymentAdmin)