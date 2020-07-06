from django.forms import ModelForm
from .models import *
from django import forms


class CreateProfilEntr(forms.ModelForm):
    class Meta:
        model= ProfilEntreprise
        fields='__all__'
        exclude = ('user',)


