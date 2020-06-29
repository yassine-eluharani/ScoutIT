from django.forms import ModelForm
from .models import Projet_realise


class Projet_realiseForm(ModelForm):
    class Meta:
        model = Projet_realise
        fields = '__all__'