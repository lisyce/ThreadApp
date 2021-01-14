from django.forms import ModelForm
from .models import *

#at some point, have this check to see if this already exists in the database of Thread
#if it exists, just create an owned thread.
#if it doesn't exist, create the thread then prompt the user to add how much they own
class ThreadForm(ModelForm):
    class Meta:
        model = OwnedThread
        fields = '__all__'