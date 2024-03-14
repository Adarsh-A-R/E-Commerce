from django.contrib import admin
from .models import *


# Register your models here.
class Catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Categ, Catadmin)


class ProAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'img']
    list_editable = ['price', 'stock', 'img']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Products, ProAdmin)



