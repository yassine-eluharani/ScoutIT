from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class Projet_realiseForm(ModelForm):
    class Meta:
        model = Projet_realise
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class CreateProfil(forms.ModelForm):
    class Meta:
        model= Profil
        fields='__all__'
        exclude = ('user',)
