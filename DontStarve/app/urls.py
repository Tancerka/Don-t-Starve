from django.urls import path
from .views import main, add_dish, add_to_basket, remove_from_basket, basket
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', main, name='main'),
    path("login/",views.login, name="login"),
    path("register/",views.register, name="register"),
    path("reservation/",views.reservation, name="reservation"),
    path('logout/', views.custom_logout, name='logout'),
    path('account/',views.account,name='account'),
    path('basket/', basket, name='basket'),
    path('order/',views.order_summary,name='order'),
    path('takeaway/',views.takeaway,name='takeaway'),
    path('order_summary/', views.order_summary, name='order_summary'),
    path('add_dish/', add_dish, name='add_dish'),
    path('add_to_basket/<int:dish_id>/', add_to_basket, name='add_to_basket'),
    path('remove_from_basket/<int:item_id>/', remove_from_basket, name='remove_from_basket'),
]
