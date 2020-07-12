from django.urls import path
from Candidat.views import index
from .views import *


urlpatterns = [
    path('', index,name='index'),
    path('profilEntr/', profilEntr, name='profilEntr'),
    path('registerEntr/', registerEntr, name='registerEntr'),
    path('add_offer/', AddOffer, name="add_offer"),
    path('delete_offre/<str:pk>/', deleteOffre, name="delete_offre"),

]