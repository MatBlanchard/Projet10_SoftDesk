# OpenClassrooms: Projet 10 - SoftDesk
Projet réalisé dans le cadre de ma formation OpenClassrooms Développeur d'Applications Python.  
Il s'agit d'une API réalisée avec Django pour une société fictive, SoftDesk.  
L'application permet de remonter et suivre des problèmes techniques.
## Documentation
Tout les endpoints, leurs détails ainsi que des exemples d'utilisation sont décrits dans la [documentation](https://documenter.getpostman.com/view/25251122/2s8ZDbXMGq).
## Installation et lancement
Commencez tout d'abord par installer Python.

https://www.python.org/downloads/

Lancez ensuite la console, placez-vous dans le dossier de votre choix puis clonez ce repository :
```
git clone https://github.com/MatBlanchard/Projet10_SoftDesk.git
```
Créez un nouvel environnement virtuel :
```
python -m venv env
```
Ensuite, activez-le.
Windows:
```
env\scripts\activate
```
Installez ensuite les packages :
```
pip install -r requirements.txt
```
Effectuez les migrations :
```
python manage.py makemigrations
```
Puis :
```
python manage.py migrate
```
Il ne vous reste plus qu'à lancer le serveur : 
```
python SoftDesk\manage.py runserver
```
Vous pouvez ensuite utiliser l'applicaton via les différents endpoints décrits dans la documentation. 
Vous devez d'abord créer un compte utilisateur à l'endpoint http://127.0.0.1:800/api/signup/ afin d'accéder aux fonctionnalités de l'application.
