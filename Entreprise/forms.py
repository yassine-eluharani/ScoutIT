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
        
class AddOfferForm(forms.ModelForm):
    class Meta:
        model = Offre
        fields = ['poste','diplome','experience','description','entreprise']
        widgets = {
            'poste' : forms.Select(attrs={'class':'form-control', 'placeholder':'Position'}),
            'diplome' : forms.Select(attrs={'class':'form-control', 'placeholder':'Degree'}),
            'experience' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Experience'}),           
            'description' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Other skills'}),
            'entreprise'  : forms.HiddenInput()
        }


