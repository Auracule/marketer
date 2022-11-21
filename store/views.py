from django.shortcuts import render
from django.http import HttpResponse
from . models import *

# Create your views here.

def indexs(request):
    return HttpResponse('hello nigga')