from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import ChercheurViewSet, ProjetDeRechercheViewSet, PublicationViewSet
from .views import chercheur_create, projet_create, publication_create, chercheurs_list, projets_list, publications_list

urlpatterns = [
    path('chercheurs/', chercheurs_list, name='chercheurs_list'),
    path('chercheurs/create/', chercheur_create, name='chercheur_create'),
    path('projets/', projets_list, name='projets_list'),
    path('projets/create/', projet_create, name='projet_create'),
    path('publications/', publications_list, name='publications_list'),
    path('publications/create/', publication_create, name='publication_create'),
]


router = DefaultRouter()
router.register(r'chercheurs', ChercheurViewSet)
router.register(r'projets', ProjetDeRechercheViewSet)
router.register(r'publications', PublicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('chercheurs/', views.chercheurs_list, name='chercheurs_list'),
    path('chercheurs/create/', views.chercheur_create, name='chercheur_create'),
    path('projets/', views.projets_list, name='projets_list'),
    path('projets/create/', views.projet_create, name='projet_create'),
    path('publications/', publications_list, name='publications_list'),
    path('publications/create/', publication_create, name='publication_create'),
]
