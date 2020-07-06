from django.shortcuts import render , redirect
from django.contrib.auth import authenticate ,login ,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

#Local imports
from .models import *
from Candidat.decorators import *
from Candidat.forms import CreateUserForm
from .forms import CreateProfilEntr

@login_required(login_url='login')
@allowed_users(allowed_roles=['Entreprise'])
def profilEntr(request):
    context={}
    return render(request ,'entreprise/profilEntr.html',context)

@unauthenticated_user
def registerEntr(request):
    form = CreateUserForm()
    profil_form = CreateProfilEntr()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        profil_form = CreateProfilEntr(request.POST)
        if form.is_valid() and profil_form.is_valid():
            user = form.save()            
            profil = profil_form.save(commit=False)
            profil.user = user
            profil.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name="Entreprise")
            user.groups.add(group)
            messages.success(request,'Account was created for ' + username)
            return redirect('login')
    context ={
        'form':form,
        'profil_form' :profil_form
    }
    return render(request ,'registration/registerEntr.html',context)
