from django.shortcuts import render, redirect
from .logowanie.form import CustomLoginForm
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    return render(request, "home.html")

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
    
