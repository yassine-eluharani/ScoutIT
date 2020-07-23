from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User

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
    user = models.OneToOneField(User, null =True,on_delete=models.CASCADE , default="images/user.png")
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
    specialite = models.CharField(max_length=50 , null =True , blank=True)
    adresse = models.TextField(null=True,blank=True)
    linkdin = models.URLField(max_length=200,null=True,blank=True)

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