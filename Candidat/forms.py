from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User



class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password confirm'}))
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),           
        }

class EmailUsenameUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),           
        }

class DateInput(forms.DateInput):
    input_type = 'date'
    value = 'Birthdate'

class CreateProfil(forms.ModelForm):
    profil_pic = forms.ImageField(label=('Profile Picture'),required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)
    class Meta:
        model= Profil
        fields=['nom', 'prenom', 'date_n', 'sex', 'status', 'nationalite', 'pays', 'ville', 'telephone', 'adresse', 'linkdin' ,'profil_pic']        
        widgets = {
            'nom' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'prenom' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),  
            'date_n' : DateInput(attrs={'class':'form-control'}),  
            'sex' : forms.Select(attrs={'class':'form-control', 'placeholder':'Sex'}),  
            'status' : forms.Select(attrs={'class':'form-control', 'placeholder':'Status'}),  
            'nationalite' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nationality'}),  
            'pays' : forms.Select(attrs={'class':'form-control', 'placeholder':'County'}),           
            'ville' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}),           
            'telephone' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone number'}),           
            'adresse' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Address'}),           
            'linkdin' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Linkdin'}),           
            
        }
