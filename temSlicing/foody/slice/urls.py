from django.urls import path, include
from . import views

urlpatterns = [

    path('home', views.home, name="home"),
    path('items', views.items, name="items"),

    path('addRestaurants', views.addRestaurants, name="addRestaurants"),
    path('viewRestaurants', views.viewRestaurants, name="viewRestaurants"),
    path("editRestaurants/<int:id>", views.editRestaurants, name="editRestaurants"),
    path("deleteRestaurants/<int:id>", views.deleteRestaurants, name="deleteRestaurants"),

    path('addMenu', views.addMenu, name="addMenu"),
    path("viewMenus", views.viewMenus, name='viewMenus'),
    path("editMenu/<int:id>", views.editMenu, name="editMenu"),
    path("deleteMenu/<int:id>", views.deleteMenu, name="deleteMenu"),

    path('orders', views.orders, name="orders"),
    path("changestatus/",views.changestatus,name="changestatus"),

    path('', views.adminLogin, name='adminLogin'),
    path('adminLogout', views.adminLogout, name='adminLogout'),

]
