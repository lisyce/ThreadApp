from django.shortcuts import render
from .models import Thread

# Create your views here.
def home(request):

    all_threads = Thread.objects.all()

    return render(request, 'index.html', {'threads' : all_threads})