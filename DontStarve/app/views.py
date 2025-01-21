from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import CustomLoginForm ,CreateUserForm #CustomRegisterForm,

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
            login(request, user)
            return redirect('/main')  # Przekierowanie po zalogowaniu
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
 
def order_summary(request):
    return render(request, "resto/order_summary.html")
 
def takeaway(request):
    return render(request, "resto/takaway.html")

