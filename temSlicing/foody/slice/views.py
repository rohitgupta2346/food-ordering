from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .models import User
import os
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='adminLogin')
def home(request):
    return render(request, 'slice/productItems.html')


@login_required(login_url='adminLogin')
def items(request):
    r = Restaurant.objects.all().count()
    rm = RestaurantMenu.objects.all().count()
    return render(request, 'slice/productItems.html', {"r": r, "rm": rm, "pageTitle": "Home"})


@login_required(login_url='adminLogin')
def addRestaurants(request):
    if request.method == 'POST':
        name = request.POST['restaurantName']
        location = request.POST['restaurantLocation']
        phone_number = request.POST['restaurantNumber']
        email = request.POST['restaurantEmail']
        res_image = request.FILES['restaurantLogo']
        a = Restaurant(
            name=name,
            location=location,
            phoneNumber=phone_number,
            email=email,
            image=res_image
        )
        a.save()
        res = Restaurant.objects.all()
        return render(request, 'slice/viewRestaurants.html',
                      {'message': "Restaurant added successfully", "res": res, "pageTitle": "Restaurants List"})
    else:
        return render(request, 'slice/addRestaurants.html', {"pageTitle": "Add Restaurant"})


@login_required(login_url='adminLogin')
def viewRestaurants(request):
    res = Restaurant.objects.all()
    return render(request, 'slice/viewRestaurants.html', {'res': res, "pageTitle": "Restaurants List"})


@login_required(login_url='adminLogin')
def editRestaurants(request, id):
    y = Restaurant.objects.get(id=id)
    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(y.image) > 0:
                os.remove(y.image.path)
            y.image = request.FILES['res_image']
        res_name = request.POST['res_name']
        res_location = request.POST['res_location']
        res_number = request.POST['restaurantNumber']
        res_email = request.POST['restaurantEmail']
        y.name = res_name
        y.location = res_location
        y.phoneNumber = res_number
        y.email = res_email
        y.save()
        res = Restaurant.objects.all()
        return render(request, 'slice/viewRestaurants.html',
                      {'message': "Restaurant update successfully", "res": res, "pageTitle": "Restaurants List"})
    else:
        return render(request, "slice/editRestaurants.html", {"data": y, "pageTitle": "Update Restaurant"})


@login_required(login_url='adminLogin')
def deleteRestaurants(request, id):
    z = Restaurant.objects.get(id=id)
    z.delete()
    res = Restaurant.objects.all()
    return render(request, 'slice/viewRestaurants.html',
                  {'message': "Restaurant delete successfully", "data": res, "pageTitle": "Restaurants List"})


@login_required(login_url='adminLogin')
def addMenu(request):
    if request.method == 'POST':
        name = request.POST['dishName']
        dish_price = request.POST['dishPrice']
        res_id = request.POST['restaurantId']
        res_image = request.FILES['dishImage']
        a = RestaurantMenu(
            food_name=name,
            price=dish_price,
            menuImage=res_image,
            restaurantId=Restaurant.objects.get(id=res_id),
        )
        a.save()
        res = RestaurantMenu.objects.all()
        return render(request, 'slice/viewMenu.html',
                      {'message': "Restaurant Menu added successfully", "data": res, "pageTitle": "Menus List"})
    else:
        rt = Restaurant.objects.all()
        return render(request, 'slice/addMenu.html', {"rt": rt, "pageTitle": "Add Menu"})


@login_required(login_url='adminLogin')
def viewMenus(request):
    tdata = RestaurantMenu.objects.all()
    return render(request, 'slice/viewMenu.html', {'data': tdata, "pageTitle": "Menus List"})


@login_required(login_url='adminLogin')
def editMenu(request, id):
    a = RestaurantMenu.objects.get(id=id)
    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(a.menuImage) > 0:
                os.remove(a.menuImage.path)
            a.res_image = request.FILES['dishImage']
        print("Restaurant Id - ", request.POST['restaurantId'])
        if (request.POST['dishPrice']):
            dPrice = int(request.POST['dishPrice'])
        else:
            dPrice = a.price
        print("Price - ", dPrice, "Type - ", type(dPrice))
        name = request.POST['dishName']
        print(name, dPrice)
        a.food_name = name
        a.price = dPrice
        a.restaurantId = Restaurant.objects.get(id=request.POST['restaurantId'])
        a.save()
        res = RestaurantMenu.objects.all()
        return render(request, 'slice/viewMenu.html',
                      {'message': "Restaurant Menu updated successfully", "data": res, "pageTitle": "Menus List"})
    else:
        rt = Restaurant.objects.all()
        return render(request, 'slice/editMenu.html', {"a": a, "rt": rt, "pageTitle": "Update Menu"})


@login_required(login_url='adminLogin')
def deleteMenu(request, id):
    z = RestaurantMenu.objects.get(id=id)
    z.delete()
    res = RestaurantMenu.objects.all()
    return render(request, 'slice/viewMenu.html',
                  {'message': "Restaurant Menu deleted successfully", "res": res, "pageTitle": "Menus List"})


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "slice/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "slice/register.html", {
                "message": "Username already taken."
            })
        return render(request, "slice/register.html", {"message": 'Registered successfully.'})
    else:
        return render(request, "slice/register.html")


def adminLogin(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username,
                            password=password)
        # Check if authentication successful
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect(items)
            else:
                return render(request, "slice/adminLogin.html", {
                    "message": "Invalid username and/or password."
                })
        else:
            return render(request, "slice/adminLogin.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "slice/adminLogin.html")


@login_required(login_url='adminLogin')
def adminLogout(request):
    logout(request)
    return redirect(adminLogin)


@login_required(login_url='adminLogin')
def orders(request):
    ord_details = OrderDetails.objects.all()
    return render(request, 'slice/order_details.html', {'ord_details': ord_details, "pageTitle": "Orders List"})


@login_required(login_url='adminLogin')
def changestatus(request):
    b = OrderDetails.objects.get(id=request.GET['id'])
    b.status = request.GET['status']
    b.save()
    ord_details = OrderDetails.objects.all()
    return render(request, 'slice/order_details.html', {'ord_details': ord_details, "pageTitle": "Orders List"})


@login_required(login_url='adminLogin')
def viewUser(request):
    all_user = User.objects.filter(is_superuser = False)
    return render(request, 'slice/user_details.html', {'data': all_user})

@login_required(login_url='adminLogin')
def deleteUser(request, id):
    a = User.objects.get(id=id)
    a.delete()
    return HttpResponseRedirect(reverse('viewUsers'))