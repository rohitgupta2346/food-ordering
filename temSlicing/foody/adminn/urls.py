from django.urls import path,include
from . import views
from .import views
urlpatterns = [
path('',views.adminlogin),
path('firstt',views.first,name='firstt'),
path('all_data',views.all_data,name="all_data"),



]