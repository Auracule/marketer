from django.contrib import admin
from . models import *

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone', 'state', 'address', 'pix']
admin.site.register(Profile, ProfileAdmin)
