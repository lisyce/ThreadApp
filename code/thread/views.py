from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import *

# Create your views here.
def home(request):

    all_threads = Thread.objects.all()
    all_collections = Collection.objects.all().annotate(
        thread_count = Count('threads'),
    )
    #all public collections in database
    public_collections = Collection.public_manager.all()

    return render(request, 'index.html', {'threads' : all_threads, 'collections' : all_collections})

def collection_single(request, collection):
    
    collection = get_object_or_404(Collection, slug=collection, status='public')

    return render(request, 'single_collection.html', {'collection' : collection})