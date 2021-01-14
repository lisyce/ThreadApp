from django.contrib import admin
from django.urls import path
from . import views

app_name = 'thread'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('create_thread/', views.create_thread, name='create_thread'),
    path('<slug:collection>/', views.collection_single, name='collection_single'),
    
]