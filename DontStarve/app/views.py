from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "home.html")

def logowanie(request):
    return render(request, "resto/index.html")
