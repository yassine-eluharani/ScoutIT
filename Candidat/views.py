from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate ,login ,logout
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
#Local imports
from .decorators import unauthenticated_user , allowed_users
from .models import *
from .forms import *



def index(request):
    return render(request,'index.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Candidat'])
def profil(request):
    academics = request.user.profil.academic_set.all()
    exp_pros = request.user.profil.experience_pro_set.all()
    projets = request.user.profil.projet_realise_set.all()
    certificats = request.user.profil.certificat_set.all()
    langues = request.user.profil.language_set.all()    
    context={
        'academics' : academics,
        'exp_pros':exp_pros,
        'projets' :projets,
        'certificats':certificats,
        'langues' : langues
    }
    return render(request ,'candidat/profil.html',context)



#Registartion
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
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name               
                if group == 'Candidat':
                    return redirect('profil')
                else:
                    return redirect('profilEntr')
                    
        else:
            messages.info(request,'Username or Password is incorrect')
    context={}
    return render(request ,'registration/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('index')


#Projet_realise
@login_required(login_url='login')
@allowed_users(allowed_roles=['Candidat'])
def createProjet(request):
    
    ProjetFormSet = inlineformset_factory(Profil , Projet_realise , fields=('annee_projet','description_projet') ,extra=2)
    profil = request.user.profil
    formset = ProjetFormSet(instance=profil)    
    if request.method == 'POST':
        formset = ProjetFormSet(request.POST ,instance=profil) 
        if formset.is_valid():
            formset.save()
            return redirect("profil")
    
    context ={
        'formset':formset  
    }
    return render(request,'form/add-from.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Candidat'])
def deleteProjet(request ,pk):

    project = Projet_realise.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect("profil")
    context = {
        'item':project
    }
    return render(request,'form/delete.html',context)


#Experience_Pro
@login_required(login_url='login')
@allowed_users(allowed_roles=['Candidat'])
def createExperience_pro(request):
    
    ProjetFormSet = inlineformset_factory(Profil , Experience_Pro , fields=('annee_debut' ,'annee_fin' ,'description_exp_pro') ,extra=2)
    profil = request.user.profil
    formset = ProjetFormSet(instance=profil)    
    if request.method == 'POST':
        formset = ProjetFormSet(request.POST ,instance=profil) 
        if formset.is_valid():
            formset.save()
            return redirect("profil")
    
    context ={
        'formset':formset  
    }
    return render(request,'form/add-from.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Candidat'])
def deleteExperience_pro(request ,pk):
    exp_pro = Experience_Pro.objects.get(id=pk)
    if request.method == 'POST':
        exp_pro.delete()
        return redirect("profil")
    context = {
        'item':exp_pro
    }
    return render(request,'form/delete.html',context)


#Academic
@login_required(login_url='login')
@allowed_users(allowed_roles=['Candidat'])
def createAcademic(request):
    
    ProjetFormSet = inlineformset_factory(Profil , Academic , fields=('annee_debut','annee_fin' ,'type_diplome','description_academic','ecole') ,extra=2)
    profil = request.user.profil
    formset = ProjetFormSet(instance=profil)    
    if request.method == 'POST':
        formset = ProjetFormSet(request.POST ,instance=profil) 
        if formset.is_valid():
            formset.save()
            return redirect("profil")
    
    context ={
        'formset':formset  
    }
    return render(request,'form/add-from.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Candidat'])
def deleteAcademic(request ,pk):

    academic = Academic.objects.get(id=pk)
    if request.method == 'POST':
        academic.delete()
        return redirect("profil")
    context = {
        'item': academic
    }
    return render(request,'form/delete.html',context)


#Certificat
@login_required(login_url='login')
@allowed_users(allowed_roles=['Candidat'])
def createCertificat(request):
    
    ProjetFormSet = inlineformset_factory(Profil , Certificat , fields=('accreditation','titre_cert','date_cert') ,extra=2)
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
    return render(request,'form/add-from.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Candidat'])
def deleteCertificat(request ,pk):

    certificat = Certificat.objects.get(id=pk)
    if request.method == 'POST':
        certificat.delete()
        return redirect("profil")
    context = {
        'item':certificat
    }
    return render(request,'form/delete.html',context)


#Language
@login_required(login_url='login')
@allowed_users(allowed_roles=['Candidat'])
def createLanguage(request):
    
    ProjetFormSet = inlineformset_factory(Profil , Language , fields=('langue','level') ,extra=2)
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
    return render(request,'form/add-from.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Candidat'])
def deleteLanguage(request ,pk):

    langue = Language.objects.get(id=pk)
    print(langue)
    if request.method == 'POST':
        langue.delete()
        return redirect("profil")
    context = {
        'item':langue
    }
    return render(request,'form/delete.html',context)
    






















