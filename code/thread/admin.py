from django.contrib import admin
from . import models

# Register your models here
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('brand', 'id_number', 'style', 'color_name', 'length_owned', 'added_by')

admin.site.register(models.Thread, AuthorAdmin)