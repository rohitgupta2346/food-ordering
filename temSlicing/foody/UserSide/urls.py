from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.userLogin, name="userLogin"),
    path('userRegister', views.userRegister, name="userRegister"),
    path('userLogout', views.userLogout, name="userLogout"),

    path('masterPage', views.masterPage, name="masterPage"),
    path('allRestaurants', views.allRestaurants, name="allRestaurants"),
    path('restaurantsMenus/<int:pk>', views.restaurantsMenus, name="restaurantsMenus"),

    path('placeOrder/<int:pk>', views.placeOrder, name="placeOrder"),
    path('orderDetails', views.orderDetails, name="orderDetails"),

]
