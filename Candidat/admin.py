from django.contrib import admin
from .models import Profil,Experience_Pro,Academic,Ecole,Projet_realise,Certificat,Language,Question,ScorePersonalite

# Register your models here.
admin.site.register(Ecole)
admin.site.register(Profil)
admin.site.register(Academic)
admin.site.register(Experience_Pro)
admin.site.register(Projet_realise)
admin.site.register(Certificat)
admin.site.register(Language)
admin.site.register(Question)
admin.site.register(ScorePersonalite)


