from django.shortcuts import render
from . models import restourant,restourant_menu,order_details
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
def one(request):
    return render(request,'slice/index.html')
def products(request):
    return  render(request,'slice/product.html')
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
    #id=id
    data = restourant.objects.all()
    if request.method == 'POST':
        food_name = request.POST['food_name']
        isveg = request.POST['is_veg']
        food_price=request.POST['food_price']
        id = request.POST['res']
        rest_id=restourant.objects.get(id=id)
        menu_data = restourant_menu(
            food_name = food_name,
             is_veg= isveg,
            price =food_price,
            restourant_id=rest_id,

        )
        menu_data.save()
        return render(request,'slice/restourant_menu.html',{'food_data':data})
    else:
        return render(request,'slice/restourant_menu.html',{'food_data':data})

def menu_edit(request,id):
    y=order_details.objects.get(id=id)
    if request.method == 'POST':
        fname = request.POST['fname']
        isveg= request.POST['isveg']
        price= request.POST['price']
        rid=request.POST['rid']

        y.food_name=fname
        y.is_veg=isveg
        y.price=price
        y.restouranr_id=rid
        y.save()
        return HttpResponseRedirect(reverse('addrestaurant_menu'))

    else:
        return render(request,"slice/menu_edit.html",{"data":y})

def menu_delete(request,id):
    z=restourant_menu.objects.get(id=id)
    z.delete()
    return HttpResponseRedirect(reverse('addrestaurant_menu'))


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
