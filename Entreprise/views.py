from django.shortcuts import render , redirect
from django.contrib.auth import authenticate ,login ,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

#Local imports
from Candidat.models import Profil,Experience_Pro,Academic
from .models import *
from Candidat.decorators import *
from Candidat.forms import CreateUserForm
from .forms import CreateProfilEntr ,AddOfferForm

@login_required(login_url='login')
@allowed_users(allowed_roles=['Entreprise'])
def profilEntr(request):
    offres = request.user.profilentreprise.offre_set.all()
    context={        
        'offres':offres
    }
    return render(request ,'entreprise/profilEntr.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Entreprise'])
def AddOffer(request):    
    entreprise = request.user.profilentreprise        
    form = AddOfferForm(initial={'entreprise' : entreprise})
    if request.method == 'POST':            
        form = AddOfferForm(request.POST, initial={'entreprise' : entreprise})        
        if form.is_valid():
            form.save()            
            return redirect("profilEntr")
    context={
        'form' : form
    }
    return render(request,'form/add-formEntr.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Entreprise'])
def scout(request,my_id):
    o = Offre.objects.get(id=my_id)
    poste = o.poste
    degree = o.diplome
    expPoste = o.experience
    profils = Profil.objects.filter(poste=poste)
    countExp = 0
    for p in profils:
        exps = Experience_Pro.objects.filter(profil=p)   
        for exp in exps:
            p.nbr_annee += exp.nbr_annee          
    
    for p in profils:
        academics = Academic.objects.filter(profil=p)
        for academic in academics:
            if academic.type_diplome == 'Doctorat':                
                p.type_diplome = academic.type_diplome
            elif academic.type_diplome == 'Master':                
                p.type_diplome = academic.type_diplome
            elif academic.type_diplome == 'Bachelor':
                p.type_diplome = academic.type_diplome
    
    context = {
        'profils':profils,
        'degree' : degree,
        'expPoste' : expPoste,
    }
    
    return render(request,'Entreprise/scouting.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Entreprise'])
def deleteOffre(request ,pk):
    offre = Offre.objects.get(id=pk)
    if request.method == 'POST':
        offre.delete()
        return redirect("profilEntr")
    context = {
        'item':offre
    }
    return render(request,'form/delete.html',context)

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



@login_required(login_url='login')
@allowed_users(allowed_roles=['Entreprise'])
def cvEntr(request,my_id):
    profil = Profil.objects.get(id=my_id)
    academics = profil.academic_set.all()
    exp_pros = profil.experience_pro_set.all()
    projets = profil.projet_realise_set.all()
    certificats = profil.certificat_set.all()
    langues = profil.language_set.all()
    context={
        'profil':profil,
        'academics' : academics,
        'exp_pros':exp_pros,
        'projets' :projets,
        'certificats':certificats,
        'langues' : langues
    }
    return render(request ,'entreprise/cv.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Entreprise'])
def profil(request,my_id):
    profil = Profil.objects.get(id=my_id)
    try:  
        score = ScorePersonalite.objects.get(Profil=profil)
    except:
        score=None
    context = {
       'score' : score ,
       'profil':profil
    }
    return render(request,'entreprise/profil-personel.html',context)


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


def indexEntreprise(request):
    return render(request,'Entreprise/startEntreprise.html')