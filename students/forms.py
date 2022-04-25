from django import forms
from .models import Etudiant, Matiere, Note

# Création formulaire

class AjoutForm(forms.Form):
    etudiant = forms.ModelChoiceField(
        queryset=Etudiant.objects.order_by('name'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    matiere = forms.ModelChoiceField(
        queryset=Matiere.objects.order_by('name'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    note = forms.FloatField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )


class AjoutEtudiantForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
