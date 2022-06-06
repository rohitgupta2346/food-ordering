from sqlite3 import IntegrityError

from django.shortcuts import render, redirect
from slice.models import Restaurant, RestaurantMenu, User, OrderDetails
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def userLogin(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username,
                            password=password)
        # Check if authentication successful
        if user is not None:
            if user.is_staff == 0:
                login(request, user)
                return redirect(allRestaurants)
            else:
                return render(request, "UserSide/userLogin.html", {
                    "message": "Invalid username and/or password."
                })
        else:
            return render(request, "UserSide/userLogin.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, 'UserSide/userLogin.html')


def userRegister(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "UserSide/userRegister.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "UserSide/userRegister.html", {
                "message": "Username already taken."
            })
        return redirect(userLogin)
    else:
        return render(request, "UserSide/userRegister.html")


@login_required(login_url='userLogin')
def userLogout(request):
    logout(request)
    return redirect(userLogin)


@login_required(login_url='userLogin')
def masterPage(request):
    return render(request, 'UserSide/masterPage.html')


@login_required(login_url='userLogin')
def allRestaurants(request):
    if request.method == "POST":
        if request.POST.get("search") is not None:
            srh = request.POST["search"]
            rt = Restaurant.objects.filter(name__icontains=srh)
            return render(request, 'UserSide/allRestaurants.html', {"res": rt})
        else:
            rt = Restaurant.objects.all()
            return render(request, 'UserSide/allRestaurants.html', {"res": rt})
    else:
        rt = Restaurant.objects.all()
        return render(request, 'UserSide/allRestaurants.html', {"res": rt})


@login_required(login_url='userLogin')
def restaurantsMenus(request, pk):
    rm = RestaurantMenu.objects.filter(restaurantId_id=pk)
    return render(request, 'UserSide/restaurantsMenus.html', {"rm": rm})


@login_required(login_url='userLogin')
def placeOrder(request, pk):
    if request.method == "POST":
        qnty = request.POST['quantity']
        dP = request.POST['dish_Price']
        userId = request.user
        rmId = RestaurantMenu.objects.get(id=pk)
        newDp = int(dP)
        print("Dp - ", type(newDp))
        intQnty = int(qnty)
        oD = OrderDetails()
        oD.user_id = userId
        oD.food_id = rmId
        oD.quantity = qnty
        oD.total_amount = intQnty * newDp
        print("qn - ", qnty, "dp - ", dP, "user - ", userId, "rm - ", rmId, "total - ", intQnty * newDp)
        oD.save()
        return redirect(allRestaurants)
    else:
        rmId = RestaurantMenu.objects.get(id=pk)
        return render(request, 'UserSide/orderForm.html', {"data": rmId})


@login_required(login_url='userLogin')
def orderDetails(request):
    oD = OrderDetails.objects.filter(user_id_id=request.user.id)
    return render(request, 'UserSide/ordersDetails.html', {"oD": oD})
