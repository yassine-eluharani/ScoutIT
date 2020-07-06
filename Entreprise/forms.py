from django.forms import ModelForm
from .models import *
from django import forms


class CreateProfilEntr(forms.ModelForm):
    class Meta:
        model= ProfilEntreprise
        fields=['nom_entr']        
        widgets = {
            'nom_entr' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Business name'}),
        }
        


