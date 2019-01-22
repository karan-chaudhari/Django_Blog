from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='myapp-home'),
    path('about/', views.about, name='myapp-about'),
    path('contact/', views.contact, name='myapp-contact'),
]