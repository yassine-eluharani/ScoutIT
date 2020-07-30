from django.urls import path
from Candidat.views import index
from .views import *


urlpatterns = [
    path('', index,name='index'),
    path('Entreprise/', indexEntreprise ,name='indexEntreprise'),
    path('profilEntr/', profilEntr, name='profilEntr'),
    path('scout/<int:my_id>/', scout, name='scout'),
    path('registerEntr/', registerEntr, name='registerEntr'),
    
    path('profil/<int:my_id>/',profil,name="profil_personel"),
    path('profilcv/<int:my_id>/',cvEntr,name="cv"),

    path('add_offer/', AddOffer, name="add_offer"),
    path('delete_offre/<str:pk>/', deleteOffre, name="delete_offre"),

    path('about/', about , name='about'),
    path('contact/', contact , name='contact'),


]