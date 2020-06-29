from django.db import models
from django_countries.fields import CountryField

# Create your models here.

class Profil(models.Model):
    SEX = (
        ('H','Homme'),
        ('F','Femme'),
    )
    STATUS = (
        ('C','célibataire'),
        ('M','marié(e)'),
        ('V','veuf(ve)'),
        ('D','divorcé(e)'),
    )
    nom = models.CharField(max_length=20 ,null=True)
    prenom = models.CharField(max_length=20 ,null=True)
    date_n = models.DateField(null=True)
    sex = models.CharField(max_length=1,choices=SEX ,null=True)
    status = models.CharField(max_length=1,choices=STATUS ,null=True)
    nationalite = models.CharField(max_length=20 ,null=True)
    pays = CountryField(blank_label='(select country)' ,null=True)
    ville = models.CharField(max_length=20 ,null=True)
    telephone = models.CharField(max_length=20 ,null=True)
    adresse = models.TextField(null=True,blank=True)
    linkdin = models.URLField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.nom + self.prenom

class Ecole(models.Model):
    nom_ecole = models.CharField(max_length=50 ,null=True)
    classement = models.IntegerField(null=True)
    def __str__(self):
        return self.nom_ecole
    

class Academic(models.Model):
    TYPE = (
        ('1','CPGE/BTS/DEUG/...'),
        ('2','Licence '),
        ('3','Master'),
        ('4','Doctorat'),
    )
    profil = models.ForeignKey('Profil',on_delete=models.CASCADE ,null=True)
    annee_debut = models.IntegerField(null=True)
    annee_fin = models.IntegerField(null=True)
    type_diplome = models.CharField(max_length=1,choices=TYPE ,null=True)
    description_academic = models.TextField(null=True,blank=True)
    ecole = models.ForeignKey('Ecole' , on_delete=models.DO_NOTHING ,null=True)




class Experience_Pro(models.Model):
    profil = models.ForeignKey('Profil',on_delete=models.CASCADE ,null=True)
    annee_debut = models.IntegerField( null=True)
    annee_fin = models.IntegerField( null=True)
    description_exp_pro = models.TextField(null=True,blank=True)

class Projet_realise(models.Model):
    profil = models.ForeignKey('Profil',on_delete=models.CASCADE ,null=True)
    annee_projet = models.IntegerField( null=True)
    description_projet = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.description_projet

class Certificat(models.Model):
    profil = models.ForeignKey('Profil',on_delete=models.CASCADE ,null=True)
    accreditation = models.CharField(max_length=100 ,null=True)
    titre_cert = models.CharField(max_length=50 ,null=True)
    date_cert = models.IntegerField( null=True)

class Language(models.Model):
    lvl = (
        ('A1','découverte'),
        ('A2','usuel'),
        ('B1','niveau seuil'),
        ('B2','niveau avancé'),
        ('C1','autonome'),
        ('C2','maîtrise'),
    )
    profil = models.ForeignKey('Profil',on_delete=models.CASCADE ,null=True)
    langue = models.CharField(max_length=20 ,null=True)
    level = models.CharField(max_length=2,choices=lvl ,null=True)
    
