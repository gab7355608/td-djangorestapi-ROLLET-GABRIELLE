# api/forms.py

from django import forms
from .models import Chercheur, ProjetDeRecherche, Publication

class ChercheurForm(forms.ModelForm):
    class Meta:
        model = Chercheur
        fields = ['nom', 'specialite', 'projets']


class ProjetDeRechercheForm(forms.ModelForm):
    class Meta:
        model = ProjetDeRecherche
        fields = ['titre', 'description', 'date_debut', 'date_fin_prevue', 'chef_projet']

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['titre', 'resume', 'projet_associe', 'date_publication']
