# tp_recherche/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from api import views 
from django.contrib.auth import views as auth_views


schema_view = get_schema_view(
   openapi.Info(
      title="Research Project Tracking API",
      default_version='v1',
      description="API for managing research projects, researchers, and publications",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('chercheurs/', views.chercheurs_list, name='chercheurs_list'),
    path('chercheurs/create/', views.chercheur_create, name='chercheur_create'),
    path('chercheurs/<int:pk>/delete/', views.chercheur_delete, name='chercheur_delete'),
    path('projets/', views.projets_list, name='projets_list'),
    path('projets/create/', views.projet_create, name='projet_create'),
    path('projets/<int:pk>/delete/', views.projet_delete, name='projet_delete'),
    path('publications/', views.publications_list, name='publications_list'),
    path('publications/create/', views.publication_create, name='publication_create'),
    path('publications/<int:pk>/delete/', views.publication_delete, name='publication_delete'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
