from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ProfilEntreprise(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nom_entr = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.nom_entr
    

class Poste(models.Model):
    poste_n = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.poste_n


class Offre(models.Model):
    TYPE = (
        ('', '(Degree)'),
        ('Bachelor','Bachelor '),
        ('Master','Master'),
        ('Doctorat','Doctorat'),
    )
    entreprise = models.ForeignKey('ProfilEntreprise', on_delete = models.DO_NOTHING)
    poste = models.ForeignKey('Poste', on_delete=models.DO_NOTHING, null=True)
    diplome = models.CharField(max_length=20,choices=TYPE ,null=True)
    experience = models.IntegerField(null=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.poste.poste_n + " for " + self.entreprise.nom_entr