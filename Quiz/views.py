from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    a = HttpResponse(b'welcome to this section')
    return a