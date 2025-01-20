from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.main, name="main"),
    path("login/",views.login, name="login"),
    path("register/",views.register, name="register"),
    path("reservation/",views.reservation, name="reservation"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('account/',views.account,name='account'),
    path('basket/',views.basket,name='basket'),
    path('order/',views.order_summary,name='order'),
    path('takeaway/',views.takeaway,name='takeaway'),
]
