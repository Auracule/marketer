from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.forms import ModelForm
from . models import *

class SignupForm(UserCreationForm):
    username = forms.CharField(max_length= 50)
    first_name = forms.CharField(max_length= 50)
    last_name = forms.CharField(max_length= 50)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class ProfileUpdate(forms.ModelForm):
    class Meta: 
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'state', 'nationality', 'gender', 'pix']
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Last Name'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Phone number'}),
            'address':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Home Address'}),
            'state':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'state'}),
            'nationality':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'state'}),
            'gender':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'state'}),
            'pix':forms.FileInput(attrs={'class':'form-control'}),
        }