from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate ,login ,logout
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
#Local imports
from .models import *
from .forms import *

def index(request):
    return render(request,'index.html')

@login_required(login_url='login')
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
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account was created for ' + user)
                return redirect('login')
        context ={
            'form':form
        }
        return render(request ,'registration/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password') 
            user = authenticate(request,username = username , password=password)  
            if user is not None :
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
def createProjet(request,pk):
    
    ProjetFormSet = inlineformset_factory(Profil , Projet_realise , fields=('annee_projet','description_projet') ,extra=2)
    profil = Profil.objects.get(id=pk)
    formset = ProjetFormSet(queryset=Projet_realise.objects.none() ,instance=profil)    
    if request.method == 'POST':
        formset = ProjetFormSet(request.POST ,instance=profil) 
        if formset.is_valid():
            formset.save()
            return redirect("/")
    
    context ={
        'formset':formset  
    }
    return render(request,'form/projet_realse-from.html',context)

@login_required(login_url='login')
def updateProjet(request,pk):

    project = Projet_realise.objects.get(id=pk)
    profile = project.profil.id
    print(profile)
    form = Projet_realiseForm(instance=project)
    if request.method == 'POST':
        form = Projet_realiseForm(request.POST,instance=project)
        if form.is_valid():
            form.save()
            return redirect("profil",profile)
    context ={
        'form':form  
    }
    return render(request,'form/projet_realse-from.html',context)

@login_required(login_url='login')
def deleteProjet(request ,pk):
    project = Projet_realise.objects.get(id=pk)
    profile = project.profil.id
    if request.method == 'POST':
        project.delete()
        return redirect("profil",profile)
    context = {
        'item':project
    }
    return render(request,'form/delete.html',context)