from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import CustomLoginForm ,CreateUserForm #CustomRegisterForm,
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.

def main(request):
    if request.user.is_authenticated:
        username = request.user.username  # Pobierz nazwę użytkownika
    else:
        username = None  # Brak zalogowanego użytkownika
    return render(request, "resto/main.html",{'username': username})

def login(request):
     if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            # Ensure the user has a profile
            Profile.objects.get_or_create(user=user)
            return redirect('/')  # Redirect to the main page after login
     else:
        form = CustomLoginForm()
     return render(request, "resto/login.html",{'form': form})


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Przekierowanie po rejestracji
        context = {'form': form}
        return render(request, "resto/register.html", context)
    else:
        form = CreateUserForm()
    return render(request, "resto/register.html",{'form': form})


def reservation(request):
    if request.user.is_authenticated:
        username = request.user.username  # Pobierz nazwę użytkownika
    else:
        username = None  # Brak zalogowanego użytkownika
    return render(request, "resto/reservation.html",{'username': username})
 
def account(request):
    return render(request, "resto/account.html")
 
def basket(request):
    return render(request, "resto/basket.html")
 
@login_required
def order_summary(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        address = request.POST.get('address')
        
        # Update the user's first name, last name, and address
        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.profile.address = address  # Assuming you have a Profile model with an address field
        user.profile.save()
        user.save()
        
        return redirect('/')  # Redirect to the same page after saving

    return render(request, 'resto/order_summary.html')
 
def takeaway(request):
    return render(request, "resto/takaway.html")

def custom_logout(request):
    logout(request)
    return redirect('/')  # Redirect to the main page after logout
