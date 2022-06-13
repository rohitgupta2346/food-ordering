from django.urls import path,include
from . import views
from .import views
urlpatterns = [
# path('',views.adminlogin),
# path('firstt',views.first,name='firstt'),
# path('all_data',views.all_data,name="all_data"),
path('',views.first,name='firstt'),
path('login',views.user_login,name='login'),
path('register',views.registers,name='register'),
path('logouts',views.logout,name='logouts'),
path('change_pass',views.change_password,name='change_pass'),
path('profiles',views.profilee,name='profiles'),
path('fshow',views.food_show,name='fshow')



]