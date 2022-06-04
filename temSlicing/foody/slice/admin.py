from django.contrib import admin
from . models import *
# Register your models here.
class resstaurnats(admin.ModelAdmin):
    list_display =('name','location','image')
admin.site.register(restourant,resstaurnats)