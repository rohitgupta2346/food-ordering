from django.shortcuts import render
from django.shortcuts import HttpResponse



def first(request):
    return render(request, "adminn/layout.html")
def restaurants(request):
    return render(request,"adminn/restaurants.html")

