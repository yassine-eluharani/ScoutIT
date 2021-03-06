from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User

from Entreprise.models import Poste

# Create your models here.

class Profil(models.Model):
    SEX = (
        ('', '(Gender)'),
        ('Male','Male'),
        ('Female','Female'),
    )
    STATUS = (
        ('', '(Status)'),
        ('Single','Single'),
        ('Married','Married'),
        ('Widowed','Widowed'),
        ('Divorced','Divorced'),
    )
    user = models.OneToOneField(User, null =True,on_delete=models.CASCADE)
    profil_pic = models.ImageField(null=True, blank=True , default="images/user.png" )
    nom = models.CharField(max_length=20 ,null=True)
    prenom = models.CharField(max_length=20 ,null=True)
    date_n = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=6,choices=SEX ,null=True , blank=True)
    status = models.CharField(max_length=12,choices=STATUS ,null=True , blank=True)
    nationalite = models.CharField(max_length=20 ,null=True, blank=True)
    pays = CountryField(blank_label='(Country)' ,null=True, blank=True)
    ville = models.CharField(max_length=20 ,null=True, blank=True)
    telephone = models.CharField(max_length=20 ,null=True, blank=True)
    poste = models.ForeignKey(Poste, on_delete=models.DO_NOTHING, null=True,blank=True)
    adresse = models.TextField(null=True,blank=True)
    linkdin = models.URLField(max_length=200,null=True,blank=True)
    facebook = models.URLField(max_length=200,null=True,blank=True)
    twitter = models.URLField(max_length=200,null=True,blank=True)
    nbr_annee = models.IntegerField(null = True , default=0,blank=True)
    type_diplome = models.CharField(max_length=20 ,null=True)

    def __str__(self):
        return self.nom + self.prenom


    

class Academic(models.Model):
    TYPE = (
        ('', '(Degree)'),
        ('Bachelor','Bachelor '),
        ('Master','Master'),
        ('Doctorat','Doctorat'),
    )
    profil = models.ForeignKey('Profil',on_delete=models.CASCADE ,null=True)
    annee_debut = models.IntegerField(null=True)
    annee_fin = models.IntegerField(null=True)
    ecole = models.CharField(max_length=50 ,null=True)
    type_diplome = models.CharField(max_length=20,choices=TYPE ,null=True)
    description_academic = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.description_academic + " de " + self.profil.nom




class Experience_Pro(models.Model):
    profil = models.ForeignKey('Profil',on_delete=models.CASCADE ,null=True)
    annee_debut = models.IntegerField( null=True)
    annee_fin = models.IntegerField( null=True)
    nbr_annee = models.IntegerField(null = True , default=0)
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
        ('', '(Level)'),
        ('A1','Beginner'),
        ('A2','Elementary'),
        ('B1','Intermediate'),
        ('B2','Upper Intermediate'),
        ('C1','Advanced'),
        ('C2','Proficiency'),
    )
    profil = models.ForeignKey('Profil',on_delete=models.CASCADE ,null=True)
    langue = models.CharField(max_length=20 ,null=True)
    level = models.CharField(max_length=2,choices=lvl ,null=True)

    def __str__(self):
        return  self.langue + " " + self.level + " " + self.profil.nom

class Question(models.Model):

    Question = models.CharField(max_length=100,blank=True)
    openness = models.CharField(max_length=150,blank=True)
    conscientiousness = models.CharField(max_length=150,blank=True)
    extraversion = models.CharField(max_length=150,blank=True)
    agreeableness = models.CharField(max_length=150,blank=True)
    neuroticism = models.CharField(max_length=150,blank=True)
    
    def __str__(self):
        return self.Question

class ScorePersonalite(models.Model):
    ScoreOp = models.IntegerField(blank=True,default=0)
    ScoreCon = models.IntegerField(blank=True,default=0)
    ScoreExt = models.IntegerField(blank=True,default=0)
    ScoreAgr = models.IntegerField(blank=True,default=0)
    ScoreNeu = models.IntegerField(blank=True,default=0)
    Profil = models.OneToOneField("Profil", on_delete=models.CASCADE,null=True)

    def __str__(self):
        return 'Score Personalite ' + self.Profil.nom