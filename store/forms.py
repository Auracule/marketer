from django import forms
from django.forms import ModelForm 
from . models import *

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['quantity']
