from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

# Register your models here
class ThreadUserAdmin(UserAdmin):
    model = models.ThreadUser
    list_display = ('username', 'is_staff',)
    search_fields = ('username', 'first_name', 'email', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name',)}),
        ('Psermissions', {'fields': ('is_staff', 'is_active',)}),
        ('Personal', {'fields': ('about',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'password1', 'password2', 'is_active', 'is_staff',)
        }),
    )

class ThreadAdmin(admin.ModelAdmin):
    list_display = ('brand', 'id_number', 'style', 'color_name', 'added_by')
    search_fields = (('brand', 'id_number', 'style', 'color_name', 'added_by'))

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'added_by', 'status')
    search_fields = ('name', 'slug', 'added_by', 'status')

class OwnedThreadAdmin(admin.ModelAdmin):
    list_display = ('owned_by', 'owned_thread', 'length_owned')
    search_fields = ('owned_by', 'owned_thread', 'length_owned')

admin.site.register(models.ThreadUser, ThreadUserAdmin)
admin.site.register(models.Thread, ThreadAdmin)
admin.site.register(models.Collection, CollectionAdmin)
admin.site.register(models.OwnedThread, OwnedThreadAdmin)