from django.contrib import admin
from . import models

# Register your models here
class ThreadAdmin(admin.ModelAdmin):
    list_display = ('brand', 'id_number', 'style', 'color_name', 'added_by')

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'added_by', 'status')

class OwnedThreadAdmin(admin.ModelAdmin):
    list_display = ('owned_by', 'owned_thread', 'length_owned')

admin.site.register(models.Thread, ThreadAdmin)
admin.site.register(models.Collection, CollectionAdmin)
admin.site.register(models.OwnedThread, OwnedThreadAdmin)