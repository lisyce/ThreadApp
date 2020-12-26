from django.contrib import admin
from . import models

# Register your models here
class ThreadAdmin(admin.ModelAdmin):
    list_display = ('brand', 'id_number', 'style', 'color_name', 'length_owned', 'added_by')

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'added_by', 'status')

admin.site.register(models.Thread, ThreadAdmin)
admin.site.register(models.Collection, CollectionAdmin)