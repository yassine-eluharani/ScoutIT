from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate ,login
# Create your views here.

def index(request):
    return render(request,'index.html')

@login_required
def profil(request):
    return render(request ,'profil.html')

def register(request):
    return render(request ,'registration/register.html')

def login(request):
    return render(request ,'registration/login.html')