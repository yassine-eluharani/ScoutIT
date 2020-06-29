from django.urls import path
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(), name="login"),
    path('profil/<str:pk>/', views.profil, name="profil"),
    
    path('create_projet/', views.createProjet, name="create_projet"),
    path('update_projet/<str:pk>/', views.updateProjet, name="update_projet"),
]
