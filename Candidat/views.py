from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate ,login
from .models import *
# Create your views here.

def index(request):
    return render(request,'index.html')

# @login_required
def profil(request,pk):
    profil = Profil.objects.get(id=pk)
    projets = profil.projet_realise_set.all()
    print(projets)

    context={
        'profil' :profil,
        'projets' :projets
    }
    return render(request ,'profil.html',context)

def register(request):
    return render(request ,'registration/register.html')

def login(request):
    return render(request ,'registration/login.html')