from django.shortcuts import render , redirect
from django.contrib.auth import authenticate ,login ,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


#Local imports
from .models import *
from Candidat.decorators import *

@login_required(login_url='login')
@allowed_users(allowed_roles=['Entreprise'])
def profilEntr(request):
    context={}
    return render(request ,'entreprise/profilEntr.html',context)
