from django.urls import path
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('profil/<str:pk>/', views.profil, name="profil"),

    
    path('create_projet/<str:pk>/', views.createProjet, name="create_projet"),
    path('update_projet/<str:pk>/', views.updateProjet, name="update_projet"),
    path('delete/<str:pk>/', views.deleteProjet, name="delete_projet"),
]
