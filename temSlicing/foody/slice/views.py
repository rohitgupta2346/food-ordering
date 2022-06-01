from django.shortcuts import render
from . models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from . models import User
def one(request):
    return render(request,'slice/index.html')
def products(request):
    return  render(request,'slice/product.html')

def contactt(request):
    return render(request,'contact.html')

def aboutus(request):
    return render(request,'slice/about.html')
# Create your views here.

def all_restourants(request):
   res =  restourant.objects.all()
   return render(request,'slice/restarants.html',{'res':res})

def restourants_menu(request):
   res_menu =  restourant_menu.objects.all()
   return render(request,'slice/restourant_menu.html',{'res_menu':res_menu})

def order_detail(request):
   ord_details =  order_details.objects.all()
   return render(request,'slice/order_details.html',{'ord_details':ord_details})

def addrestaurants(request):
    data = restourant.objects.all()
    if request.method == 'POST':
        name = request.POST['restourant_name']
        location = request.POST['restourant_location']
        res_image = request.FILES['restourant_logo']
        a = restourant(
            name = name,
            location = location,
            image = res_image
        )
        a.save()
        return render(request,'slice/restarants.html',{'data':data})
    else:
        return  render(request,'slice/restarants.html',{'data':data})

def data_edit(request,id):
    y=restourant.objects.get(id=id)
    if request.method == 'POST':
        res_name = request.POST['res_name']
        res_location = request.POST['res_location']
        res_image = request.FILES['res_image']
        y.name=res_name
        y.location=res_location
        y.image=res_image
        y.save()
        return HttpResponseRedirect(reverse('addrestaurants'))

    else:
        return render(request,"slice/data_edit.html",{"data":y})

def data_delete(request,id):
    z=restourant.objects.get(id=id)
    z.delete()
    return HttpResponseRedirect(reverse('addrestaurants'))

def addrestaurant_menu(request):
    # id=id
    data = restourant.objects.all()
    tdata=restourant_menu.objects.all()
    if request.method=='POST':
        food_name=request.POST['food_name']
        isveg=request.POST['is_veg']
        food_price=request.POST['food_price']
        id=request.POST['res']
        rest_id=restourant.objects.get(id=id)
        menu_data=restourant_menu(
            food_name=food_name,
            is_veg=isveg,
            price=food_price,
            restourant_id=rest_id,

        )
        menu_data.save()
        print(tdata)
        return render(request,'slice/restourant_menu.html',{'food_data':tdata,'data' : data})
    else:
        return render(request,'slice/restourant_menu.html',{'food_data':tdata,'data' : data})
    # if request.method == 'POST':
    #     print('hello')
    #     food_name = request.POST['food_name']
    #     # isveg = request.POST['is_veg']
    #     food_price=request.POST['food_price']
    #     id = request.POST['res']
    #     rest_id=restourant.objects.get(id=id)
    #     print(food_name, food_price, rest_id)
    #     menu_data = restourant_menu(
    #         food_name = food_name,
    #          # is_veg= isveg,
    #         price =food_price,
    #         restourant_id=rest_id,
    #
    #     )
    #     menu_data.save()
    #     return render(request,'slice/restourant_menu.html',{'food_data':data})
    # else:
    #     return render(request,'slice/restourant_menu.html',{'food_data':data})
def menu_edit(request,id):
    mdata = restourant.objects.all()
    p=restourant_menu.objects.get(id=id)
    if request.method == 'POST':
        fdname = request.POST['fdname']
        isveg = request.POST['isveg']
        price = request.POST['price']

        id = request.POST['res']
        rid = restourant.objects.get(id=id)
        p.food_name=fdname
        p.is_veg=isveg
        p.price=price
        p.restourant_id=rid
        p.save()
        return HttpResponseRedirect(reverse('restourant_menu'))

    else:
        return render(request,"slice/menu_edit.html",{"data":p,'mdata':mdata})


def menu_delete(request,id):
    z=restourant_menu.objects.get(id=id)
    z.delete()
    return HttpResponseRedirect(reverse('restourant_menu'))


def order_edit(request,id):
    y=order_details.objects.get(id=id)
    if request.method == 'POST':
        user_id = request.POST['u_id']
        food_id= request.POST['f_id']
        quantity= request.POST['quan']
        total_amount=request.POST['amnt']
        status=request.POST['ststs']
        y.user_id=user_id
        y.food_id=food_id
        y.quantity=quantity
        y.total_amount=total_amount
        y.status=status
        y.save()
        return HttpResponseRedirect(reverse('orders'))

    else:
        return render(request,"slice/order_edit.html",{"order_data":y})

def order_delete(request,id):
    z=order_details.objects.get(id=id)
    z.delete()
    return HttpResponseRedirect(reverse('orders'))



def orders(request):
    data = order_details.objects.all()
    if request.method == 'POST':
        user_id = request.POST['user_id']
        food_id= request.POST['food_id']
        quantity=request.POST['quantity']
        price=request.POST['amount']
        status=request.POST['status']
        order = order_details(
            user_id = user_id,
            food_id= food_id,
            quantity =quantity,
            total_amount=price,
            status=status

        )
        order.save()
        return render(request,'slice/order_details.html',{'order_detail':data})

    else:
        return render(request,'slice/order_details.html',{'order_detail':data})

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

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username,
        password=password)
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "slice/loginindex.html", {
            "message": "Invalid username and/or password."
        })
    else:
        return render(request, "slice/loginindex.html")

def logout_view(request):
    logout(request)
    return render(request,'slice/index.html')


from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'slice/changp.html', {
        'form': form
    })

def profiles(request):
    uid = User.id

    pdata=profile.objects.all()
    print(uid)
    if request.method == 'POST':
        emaill= request.POST['emaill']
        ji= request.POST['ji']
        p_data = profile(
            user_profile = User.email,
            email=emaill,
            usernamep=ji,
        )
        p_data.save()
        return render(request, 'slice/profile.html', {'p_data': pdata})
    else:
        return render(request, 'slice/profile.html')






