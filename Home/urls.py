"""Hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Home import views

admin.site.site_header  =  "Linky IceCreams admin"  
admin.site.site_title  =  "Linky IceCreams admin site"
admin.site.index_title  =  "Linky IceCreams Admin"

urlpatterns = [
    path('',views.index, name='Home'),
    path('about/',views.about, name='About'),
    path('contact/',views.contact, name='Contact'),
    path('services/',views.services, name='Services'),
]
