from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    context=None
    return render(request,"index.html",context)

def about(request):
    context=None
    return render(request,"about.html",context)

def contact(request):
    context=None
    return render(request,"contact.html",context)

def services(request):
    context=None
    return render(request,"services.html",context)