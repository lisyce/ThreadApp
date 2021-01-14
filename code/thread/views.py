from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import *
from .forms import *

# Create your views here.
def home(request):

    all_threads = Thread.objects.all()
    all_owned_threads = OwnedThread.objects.all()

    all_collections = Collection.objects.all().annotate(
        thread_count = Count('threads'),
    )
    #all public collections in database
    public_collections = Collection.public_manager.all()

    return render(request, 'index.html', {'threads' : all_threads, 'collections' : all_collections,
    'owned_threads': all_owned_threads})


def create_thread(request):
    form = ThreadForm()
    context = {'form':form}

    return render(request, 'thread_form.html', context)

    
def collection_single(request, collection):
    
    collection = get_object_or_404(Collection, slug=collection, status='public')

    return render(request, 'single_collection.html', {'collection' : collection})

