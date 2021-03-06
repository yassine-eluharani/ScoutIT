from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate ,login ,logout
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import Group

#Local imports
from .decorators import unauthenticated_user , allowed_users
from .models import *
from .forms import *


@unauthenticated_user
def index(request):
    return render(request,'index.html')


def indexCandidat(request):
    return render(request,'candidat/startCandidat.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Candidat'])
def cv(request):
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


@login_required(login_url='login')
@allowed_users(allowed_roles=['Candidat'])
def updateProfil(request):
    profil = request.user.profil
    user = request.user
    try:
        score = ScorePersonalite.objects.get(Profil=profil)
    except:
        score = None    
    formUser = EmailUsenameUpdateForm(instance=user)
    form = CreateProfil(instance=profil)
    if request.method == 'POST':        
        formUser = EmailUsenameUpdateForm(request.POST,instance=user)
        form = CreateProfil(request.POST, request.FILES, instance=profil)
        if form.is_valid() and formUser.is_valid():        
            formUser.save()
            form.save()        
    context={
        'form':form,
        'formUser' :formUser,
        'score' : score
    }
    return render(request,'candidat/update-profil-personel.html',context)

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

            group = Group.objects.get(name="Candidat")
            user.groups.add(group)
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
                    return redirect('Updateprofil')
                else:
                    return redirect('profilEntr')
                    
        else:
            messages.info(request,'Username or Password is incorrect')
    context={}
    return render(request ,'registration/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

#Projet_realise
@login_required(login_url='login')
@allowed_users(allowed_roles=['Candidat'])
def createProjet(request):
    
    ProjetFormSet = inlineformset_factory(Profil,
    Projet_realise,
    fields=('annee_projet','description_projet'),
    extra=1,
    can_delete=False,
    widgets={
        'annee_projet' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Year of project'}),
        'description_projet' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
    }
    )
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
    


#Experience_Pro
@login_required(login_url='login')
@allowed_users(allowed_roles=['Candidat'])
def createExperience_pro(request):
    
    ProjetFormSet = inlineformset_factory(Profil,
    Experience_Pro,
    fields=('annee_debut' ,'annee_fin' ,'nbr_annee','description_exp_pro'),
    extra=1,
    can_delete=False,
    widgets={
        'annee_debut' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Start'}),
        'annee_fin' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'End'}),
        'nbr_annee' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Number of years'}),
        'description_exp_pro' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
    }
    )
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
    


#Academic
@login_required(login_url='login')
@allowed_users(allowed_roles=['Candidat'])
def createAcademic(request):
    
    ProjetFormSet = inlineformset_factory(Profil,
    Academic,
    fields=('annee_debut','annee_fin' ,'ecole','type_diplome','description_academic'),
    extra=1,
    can_delete=False,
    widgets={
        'annee_debut' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Start'}),
        'annee_fin' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'End'}),
        'type_diplome' : forms.Select(attrs={'class':'form-control', 'placeholder':'EZEZ'}),
        'description_academic' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
        'ecole' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'School'}),
    }
    )
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


#Certificat
@login_required(login_url='login')
@allowed_users(allowed_roles=['Candidat'])
def createCertificat(request):
    
    ProjetFormSet = inlineformset_factory(Profil,
    Certificat,
    fields=('accreditation','titre_cert','date_cert'),
    extra=1,
    can_delete=False,
    widgets={
        'date_cert' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Issued in'}),
        'titre_cert' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Certification'}),
        'accreditation' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Credential ID'}),
    }
    )
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
    

#Language
@login_required(login_url='login')
@allowed_users(allowed_roles=['Candidat'])
def createLanguage(request):
    
    ProjetFormSet = inlineformset_factory(Profil,
    Language,
    fields=('langue','level'),
    extra=1,
    can_delete=False,
    widgets={
        'langue' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Language'}),
        'level' : forms.Select(attrs={'class':'form-control', 'placeholder':'Level'}),        
    }
    )
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
    if request.method == 'POST':
        langue.delete()
        return redirect("profil")


#Personality
@login_required(login_url='login')
@allowed_users(allowed_roles=['Candidat'])
def personalite(request):
    questions= Question.objects.all()
    profil = request.user.profil
    if request.method == 'POST':
        try:
            reponse = ScorePersonalite.objects.create(Profil=profil)
            allRep = []
            allRep = request.POST.getlist('poll')
            for Rep in allRep:                
                if Rep == 'openness':
                    reponse.ScoreOp +=  1

                elif Rep == 'conscientiousness':
                    reponse.ScoreCon += 1

                elif Rep == 'extraversion':
                    reponse.ScoreExt += 1

                elif Rep == 'agreeableness':
                    reponse.ScoreAgr += 1

                elif Rep == 'neuroticism':
                    reponse.ScoreNeu += 1                                            
            reponse.save()
            return redirect("Updateprofil")      
        except:
            return redirect("Updateprofil")
    context={
        'questions':questions
    }
    return render(request , 'candidat/personalite.html' , context)
    























