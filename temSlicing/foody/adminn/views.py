from django.shortcuts import render
from django.shortcuts import HttpResponse,HttpResponseRedirect
from slice.models import *
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError





# def first(request):
#     return render(request, "adminn/layout.html")
# def restaurants(request):
#     return render(request,"adminn/restaurants.html")
# def all_data(request):
#     allRestaurants = restourant.objects.all()
#     return render(request,"adminn/heloo.html",{"allRestaurants":allRestaurants})
# def adminlogin(request):
#
#     return render(request,'adminn/loginindex.html')
from slice.models import User, profile

from slice.models import restourant_menu


def first(request):
    return render(request,"adminn/indexx.html")


def registers(request):
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
            return render(request, "adminn/registers.html", {
                "message": "Username already taken."
            })
        return render(request, "adminn/registers.html", {"message": 'Registered successfully.'})
    else:
        return render(request, "adminn/registers.html")


def user_login(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username,
        password=password)
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("firstt"))
        else:
            return render(request, "adminn/loginindex.html", {
            "message": "Invalid username and/or password."
        })
    else:
        return render(request, "adminn/loginindex.html")


def logout_view(request):
    logout(request)
    return render(request,'adminn/loginindex.html')


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
            return redirect('change_pass')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'adminn/changp.html', {
        'form': form,
    })


def profilee(request):
    uid = request.user

    pdata=profile.objects.all()
    print(uid)
    if request.method == 'POST':
        emaill= request.POST['emaill']
        ji= request.POST['ji']
        p_data = profile(
            user_profile = uid,
            email=emaill,
            usernamep=ji,
        )
        p_data.save()
        return render(request, 'adminn/profile.html', {'p_datas': pdata})
    else:
        return render(request, 'adminn/profile.html')

def food_show(request):
    fdata=restourant_menu.objects.all()
    rdata=restourant.objects.all()
    return render(request,'adminn/food_items.html',{'fdata':fdata,'rdata':rdata})



