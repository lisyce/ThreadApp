from django.shortcuts import render
from django.db.models import Count
from .models import *

# Create your views here.
def home(request):

    all_threads = Thread.objects.all()
    all_collections = Collection.objects.all().annotate(
        thread_count = Count('threads'),
    )

    return render(request, 'index.html', {'threads' : all_threads, 'collections' : all_collections})