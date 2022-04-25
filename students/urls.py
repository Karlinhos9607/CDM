from django.urls import path

from . import views

# CRéation des chemins urls

urlpatterns = [
    path('', views.index, name='index'),
    path('ajout/', views.ajout_note, name="ajout_note"),
    path('ajoutEtudiant', views.ajout_etudiant, name="ajout_etudiant")
]