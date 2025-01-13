from django.shortcuts import render, redirect
from .logowanie.form import CustomLoginForm, CustomRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        username = request.user.username  # Pobierz nazwę użytkownika
    else:
        username = None  # Brak zalogowanego użytkownika
    return render(request, "home.html",{'username': username})

def logowanie(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Przekierowanie po zalogowaniu
    else:
        form = CustomLoginForm()

    return render(request, "resto/index.html", {'form': form})

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
            login(request, user)
            return redirect('main')  # Przekierowanie po zalogowaniu
    else:
        form = CustomLoginForm()
    return render(request, "resto/login.html",{'form': form})


def register(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('resto/main.html')  # Przekierowanie po rejestracji
    else:
        form = CustomRegisterForm()
    return render(request, "resto/register.html",{'form': form})


def reservation(request):
    if request.user.is_authenticated:
        username = request.user.username  # Pobierz nazwę użytkownika
    else:
        username = None  # Brak zalogowanego użytkownika
    return render(request, "resto/reservation.html",{'username': username})
  
