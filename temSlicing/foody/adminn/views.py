from django.shortcuts import render
from django.shortcuts import HttpResponse

from slice.models import *

def first(request):
    return render(request, "adminn/layout.html")
def restaurants(request):
    return render(request,"adminn/restaurants.html")
def all_data(request):
    allRestaurants = restourant.objects.all()
    return render(request,"adminn/heloo.html",{"allRestaurants":allRestaurants})
def adminlogin(request):

    return render(request,'adminn/loginindex.html')



