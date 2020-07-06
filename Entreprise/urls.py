from django.urls import path
from Candidat.views import index
from .views import *


urlpatterns = [
    path('', index,name='index'),
    path('profilEntr/', profilEntr, name='profilEntr')
]