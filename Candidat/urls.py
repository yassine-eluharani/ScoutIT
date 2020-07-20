from django.urls import path
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('cv/', views.cv, name="profil"),
    path('Updateprofil/',views.updateProfil,name="Updateprofil"),
    path('profil/',views.profil,name="profil_personel"),

    path('personalite/',views.personalite,name='personalite'),


    
    #Academic Paths
    path('create_academic/', views.createAcademic, name="create_academic"),
    path('delete_academic/<str:pk>/', views.deleteAcademic, name="delete_academic"),
    
    #Experience_Pro Paths
    path('create_experience_pro/', views.createExperience_pro, name="create_experience_pro"),
    path('delete_experience_pro/<str:pk>/', views.deleteExperience_pro, name="delete_experience_pro"),
    
    #Projet_realise Paths
    path('create_projet/', views.createProjet, name="create_projet"),
    path('delete_projet/<str:pk>/', views.deleteProjet, name="delete_projet"),
    
    #Certificat Paths
    path('create_certificat/', views.createCertificat, name="create_certificat"),
    path('delete_certificat/<str:pk>/', views.deleteCertificat, name="delete_certificat"),
    
    #Language Paths
    path('create_language/', views.createLanguage, name="create_language"),
    path('delete_language/<str:pk>/', views.deleteLanguage, name="delete_language"),
]
