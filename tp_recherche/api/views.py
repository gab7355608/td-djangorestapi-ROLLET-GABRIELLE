# api/views.py

from rest_framework import viewsets
from .models import Chercheur, ProjetDeRecherche, Publication
from .serializers import ChercheurSerializer, ProjetDeRechercheSerializer, PublicationSerializer
from .forms import ChercheurForm, ProjetDeRechercheForm, PublicationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

class ChercheurViewSet(viewsets.ModelViewSet):
    queryset = Chercheur.objects.all()
    serializer_class = ChercheurSerializer

class ProjetDeRechercheViewSet(viewsets.ModelViewSet):
    queryset = ProjetDeRecherche.objects.all()
    serializer_class = ProjetDeRechercheSerializer

class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer



#CHERCHEURS
def chercheurs_list(request):
    chercheurs = Chercheur.objects.all()
    return render(request, 'chercheurs_list.html', {'chercheurs': chercheurs})

def chercheur_create(request):
    if request.method == 'POST':
        form = ChercheurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chercheurs_list')
    else:
        form = ChercheurForm()
    
    return render(request, 'chercheur_form.html', {'form': form})

def chercheur_update(request, pk):
    chercheur = get_object_or_404(Chercheur, pk=pk)
    if request.method == 'POST':
        form = ChercheurForm(request.POST, instance=chercheur)
        if form.is_valid():
            form.save()
            return redirect('chercheurs_list')
    else:
        form = ChercheurForm(instance=chercheur)
    return render(request, 'chercheur_form.html', {'form': form})

def chercheur_delete(request, pk):
    chercheur = get_object_or_404(Chercheur, pk=pk)
    if request.method == 'POST':
        chercheur.delete()
        return redirect('chercheurs_list')  # Rediriger vers la liste des chercheurs après la suppression
    return render(request, 'chercheur_delete.html', {'chercheur': chercheur})

#PROJET
@login_required
def projet_create(request):
    if request.method == 'POST':
        form = ProjetDeRechercheForm(request.POST)
        if form.is_valid():
            projet = form.save(commit=False)
            projet.save()
            return redirect('projets_list')
    else:
        form = ProjetDeRechercheForm()
    return render(request, 'projet_form.html', {'form': form})

def projets_list(request):
    projets = ProjetDeRecherche.objects.all()
    return render(request, 'projet_list.html', {'projets': projets})

def projet_update(request, pk):
    projet = get_object_or_404(ProjetDeRecherche, pk=pk)
    if request.method == 'POST':
        form = ProjetDeRechercheForm(request.POST, instance=projet)
        if form.is_valid():
            form.save()
            return redirect('projets_list')
    else:
        form = ProjetDeRechercheForm(instance=projet)
    return render(request, 'projet_form.html', {'form': form})

def projet_delete(request, pk):
    projet = get_object_or_404(ProjetDeRecherche, pk=pk)
    if request.method == 'POST':
        projet.delete()
        return redirect('projets_list')
    return render(request, 'projet_delete.html', {'projet': projet})

#PUBLICATIONS
def publication_create(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publications_list')
    else:
        form = PublicationForm()
    return render(request, 'publication_form.html', {'form': form})


def publications_list(request):
    publications = Publication.objects.all()
    return render(request, 'publications_list.html', {'publications': publications})

def publication_update(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    if request.method == 'POST':
        form = PublicationForm(request.POST, instance=publication)
        if form.is_valid():
            form.save()
            return redirect('publications_list')
    else:
        form = PublicationForm(instance=publication)
    return render(request, 'publication_form.html', {'form': form})

def publication_delete(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    if request.method == 'POST':
        publication.delete()
        return redirect('publications_list')  # Rediriger vers la liste des publications après la suppression
    return render(request, 'publication_confirm_delete.html', {'publication': publication})