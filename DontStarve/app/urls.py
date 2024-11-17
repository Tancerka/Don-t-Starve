from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.home, name="home"),
    path("login/",views.logowanie, name="login"),
    path('logout/', LogoutView.as_view(), name='logout')
]
