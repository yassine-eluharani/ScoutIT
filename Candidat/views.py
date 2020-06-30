from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate ,login ,logout
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
#Local imports
from .decorators import unauthenticated_user
from .models import *
from .forms import *

def index(request):
    return render(request,'index.html')

@login_required(login_url='login')
def profil(request):
    projets = request.user.profil.projet_realise_set.all()
    context={
        'projets' :projets
    }
    return render(request ,'profil.html',context)

@unauthenticated_user
def register(request):
    form = CreateUserForm()
    profil_form = CreateProfil()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        profil_form = CreateProfil(request.POST)
        if form.is_valid() and profil_form.is_valid():
            user = form.save()            
            profil = profil_form.save(commit=False)
            profil.user = user
            profil.save()
            username = form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + username)
            return redirect('login')
    context ={
        'form':form,
        'profil_form' :profil_form
    }
    return render(request ,'registration/register.html',context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        user = authenticate(request,username = username , password=password)  
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Username or Password is incorrect')
    context={}
    return render(request ,'registration/login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def createProjet(request):
    
    ProjetFormSet = inlineformset_factory(Profil , Projet_realise , fields=('annee_projet','description_projet') ,extra=2)
    profil = request.user.profil
    formset = ProjetFormSet(queryset=Projet_realise.objects.none() ,instance=profil)    
    if request.method == 'POST':
        formset = ProjetFormSet(request.POST ,instance=profil) 
        if formset.is_valid():
            formset.save()
            return redirect("profil")
    
    context ={
        'formset':formset  
    }
    return render(request,'form/projet_realse-from.html',context)

@login_required(login_url='login')
def updateProjet(request,pk):

    project = Projet_realise.objects.get(id=pk)
    print(project)
    form = Projet_realiseForm(instance=project)
    if request.method == 'POST':
        form = Projet_realiseForm(request.POST,instance=project)
        if form.is_valid():
            form.save()
            return redirect("profil")
    context ={
        'form':form  
    }
    return render(request,'form/projet_realse-from.html',context)

@login_required(login_url='login')
def deleteProjet(request ,pk):
    project = Projet_realise.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect("profil")
    context = {
        'item':project
    }
    return render(request,'form/delete.html',context)