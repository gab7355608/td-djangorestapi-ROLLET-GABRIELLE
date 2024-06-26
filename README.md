Installation
Clonez le repository

git clone <url_du_repository>
cd tp_recherche
Créez un environnement virtuel (recommandé)


python -m venv venv
Activez l'environnement virtuel

Sur Windows :


venv\Scripts\activate
Sur macOS/Linux :


source venv/bin/activate
Installez les dépendances

pip install -r requirements.txt
Effectuez les migrations de la base de données


python manage.py migrate
Créez un super utilisateur pour accéder à l'interface d'administration Django


python manage.py createsuperuser

Lancez le serveur de développement
python manage.py runserver

Le serveur devrait être accessible à l'adresse : http://127.0.0.1:8000/

Routes disponibles
Admin Django : /admin/

Interface d'administration pour gérer les chercheurs, projets et publications.
API Endpoints : /api/

Endpoints pour interagir avec les données via une API REST.

Chercheurs :

Liste des chercheurs : /chercheurs/
Création d'un chercheur : /chercheurs/create/
Suppression d'un chercheur : /chercheurs/<id>/delete/

Projets :

Liste des projets : /projets/
Création d'un projet : /projets/create/
Suppression d'un projet : /projets/<id>/delete/

Publications :

Liste des publications : /publications/
Création d'une publication : /publications/create/
Suppression d'une publication : /publications/<id>/delete/
Documentation API :

Swagger UI : /swagger/
ReDoc : /redoc/
