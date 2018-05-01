
# Projet Unicorns_Blog

Projet réalisé en python sur le framework Django

### Pré-requis : 
- Python : [Site officiel](https://www.python.org/downloads/)
- Pip : [Installation](https://pip.pypa.io/en/stable/installing/)
- npm : [Téléchargement et installation](https://www.npmjs.com/get-npm)

## Installation




### Création du virtualenv : 

    $ virtualenv -p python3 unicorns_blog_env

Lancement du virtualenv : 
   
	$ cd unicorns_blog_env
    $ source bin/activate
    
  Déplacer ou cloner le dépôt du projet dans le répertoire créé (unicorns_blog_env)
  
### Installation des dépendances du projet : 

Se placer dans le dossier du projet : 

    $ cd unicorns_blog
    $ pip install -r requirements.txt
    $ npm install

Si les sources de CKEditor (éditeur HTML du projet) sont absentes lors de l'installation, il faudra les installer. Pour cela, la commande est la suivante : 

    $ python manage.py collectstatic
    
### Lancement du serveur : 

    $ python manage.py runserver

### Lancement de grunt : 

ouvrir un second terminal, se placer dans le répertoire du projet puis lancer : 

    $ grunt

> Grunt est un taskmanager : sur ce projet, il se charge de compiler les sources css (rédigées en scss), et il utilise le module browsersync pour synchroniser le navigateur avec les sources à chaque modification. 
