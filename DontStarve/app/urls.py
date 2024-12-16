from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.home, name="home"),
    path("login/",views.logowanie, name="login"),
    path("logout/",views.logowanie, name="logout"),
    path("login2/",views.login, name="login"),
    path("register/",views.register, name="login"),
    path("reservation/",views.reservation, name="login"),
    path("main/",views.main, name="login"),
    path('logout/', LogoutView.as_view(), name='logout')
]
