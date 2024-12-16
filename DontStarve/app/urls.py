from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.main, name="main"),
    path("login/",views.logowanie, name="login-old"),
    path("logout/",views.logowanie, name="logout-old2"),
    path("login2/",views.login, name="login"),
    path("register/",views.register, name="register"),
    path("reservation/",views.reservation, name="reservation"),
    path('logout/', LogoutView.as_view(), name='logout')
]
