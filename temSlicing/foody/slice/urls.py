from django.urls import path,include
from . import  views
urlpatterns = [

path('home',views.one, name = 'home'),
path('products', views.products , name="products"),
path('about',views.aboutus,name="about"),
path('contact',views.contactt,name="contact"),
path('restaurants', views.all_restourants,name="restaurants"),
path('menu',views.restourants_menu,name="menu"),
path('order',views.order_detail,name="order"),
path('addrestaurants',views.addrestaurants,name="addrestaurants"),
# path("edit/<int:id>", views.data_editing, name="edit"),
path("delete/<int:id>", views.data_delete, name="delete"),
path("restourant_menu",views.addrestaurant_menu,name='restourant_menu'),
path("orders",views.orders,name='orders'),
path("orders_edit/<int:id>", views.order_edit, name="orders_edit"),
path("menu_edit/<int:id>", views.menu_edit, name="menu_edit"),
path("menu_delete/<int:id>", views.menu_delete, name="menu_delete"),
path("order_delete/<int:id>", views.order_delete, name="order_delete"),
path("registers", views.register, name="registers"),
path('', views.login_view, name='logins'),
path('logout', views.logout_view, name='logout'),
# path('logg',views.loginn,name='logg'),
path('pass', views.change_password, name='change_password'),
path('profilee',views.profiles,name='profilee'),
    path('search',views.article_overview,name='search'),
    path('editing/<int:id>',views.editview,name='editing'),

]

