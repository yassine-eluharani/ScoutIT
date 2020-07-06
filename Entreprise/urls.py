from django.urls import path
from Candidat.views import index


urlpatterns = [
path('', index,name='index'),
]