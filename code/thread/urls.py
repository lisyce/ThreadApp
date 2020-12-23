from django.contrib import admin
from django.urls import path
from . import views

app_name = 'thread'

urlpatterns = [
    path('', views.home, name='homepage'),
]