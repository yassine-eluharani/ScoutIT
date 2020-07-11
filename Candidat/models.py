from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User

# Create your models here.

class Profil(models.Model):
    SEX = (
        ('', '(Gender)'),
        ('Homme','Male'),
        ('Femme','Female'),
    )
    STATUS = (
        ('', '(Status)'),
        ('Single','Single'),
        ('Married','Married'),
        ('Widowed','Widowed'),
        ('Divorced','Divorced'),
    )
    user = models.OneToOneField(User, null =True,on_delete=models.CASCADE)
    profil_pic = models.ImageField(null=True, blank=True)
    nom = models.CharField(max_length=20 ,null=True)
    prenom = models.CharField(max_length=20 ,null=True)
    date_n = models.DateField(null=True)
    sex = models.CharField(max_length=6,choices=SEX ,null=True)
    status = models.CharField(max_length=12,choices=STATUS ,null=True)
    nationalite = models.CharField(max_length=20 ,null=True)
    pays = CountryField(blank_label='(Country)' ,null=True)
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
        ('CPGE/BTS/DEUG/...','CPGE/BTS/DEUG/...'),
        ('Licence','Licence '),
        ('Master','Master'),
        ('Doctorat','Doctorat'),
    )
    profil = models.ForeignKey('Profil',on_delete=models.CASCADE ,null=True)
    annee_debut = models.IntegerField(null=True)
    annee_fin = models.IntegerField(null=True)
    type_diplome = models.CharField(max_length=20,choices=TYPE ,null=True)
    description_academic = models.TextField(null=True,blank=True)
    ecole = models.ForeignKey('Ecole' , on_delete=models.DO_NOTHING ,null=True)
    def __str__(self):
        return self.description_academic + " de " + self.profil.nom




class Experience_Pro(models.Model):
    profil = models.ForeignKey('Profil',on_delete=models.CASCADE ,null=True)
    annee_debut = models.IntegerField( null=True)
    annee_fin = models.IntegerField( null=True)
    description_exp_pro = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.description_exp_pro + " de " + self.profil.nom

class Projet_realise(models.Model):
    profil = models.ForeignKey('Profil',on_delete=models.CASCADE ,null=True)
    annee_projet = models.IntegerField( null=True)
    description_projet = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.description_projet + " de " + self.profil.nom

class Certificat(models.Model):
    profil = models.ForeignKey('Profil',on_delete=models.CASCADE ,null=True)
    accreditation = models.CharField(max_length=100 ,null=True)
    titre_cert = models.CharField(max_length=50 ,null=True)
    date_cert = models.IntegerField( null=True)
    def __str__(self):
        return  self.titre_cert + " " + self.profil.nom

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

    def __str__(self):
        return  self.langue + " " + self.level + " " + self.profil.nom
    
