from django.urls import path,include
from . import  views
urlpatterns = [

path('',views.one),
path('products', views.products , name="products"),
path('restaurants', views.all_restourants,name="restaurants"),
path('menu',views.restourants_menu,name="menu"),
path('order',views.order_detail,name="order"),
path('addrestaurants',views.addrestaurants,name="addrestaurants"),
path("edit/<int:id>", views.data_edit, name="edit"),
path("delete/<int:id>", views.data_delete, name="delete"),
path("restourant_menu",views.addrestaurant_menu,name='restourant_menu'),
path("orders",views.orders,name='orders'),
path("orders_edit/<int:id>", views.order_edit, name="orders_edit"),
path("menu_edit/<int:id>", views.menu_edit, name="menu_edit"),
path("menu_delete/<int:id>", views.menu_delete, name="menu_delete"),
path("order_delete/<int:id>", views.order_delete, name="order_delete"),
]
