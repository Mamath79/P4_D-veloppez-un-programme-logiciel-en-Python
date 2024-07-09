# OpenClassrooms: Projet 4: Chess Tournament
Ce programme a été créé dans le cadre du projet 4 d'OpenClassrooms. Il s'agit d'un gestionnaire de tournois d'échecs.
## Installation:
Veuillez installer Python.
telecharger le fichier zip P4_Developpez-un-programme-logiciel-en-Python-main depuis cette adresse:
```
https://github.com/Mamath79/P4_Developpez-un-programme-logiciel-en-Python.git
```
Unzipper le fichier

Placez vous dans le dossier OC_P4_CHESSCONTEST, puis créez un nouvel environnement virtuel:
```
python -m venv env
```
Ensuite, activez-le.
Sous Windows:
```
env\scripts\activate.bat
```
Sous Linux ou Mac OS:
```
source env/bin/activate
```
Installattion les packages requis:
```
pip install -r requirements.txt
```
Vous pouvez enfin lancer le script:
```
python main.py
```

## Utilisation
Le menu principal est divisé en 3 options.
### 1) Gestion des joueurs
Dans cette section vous pourrez:
1. Creer un profil pour un nouveau joueur
2. Editer les information sur un joueur déjà existant
3. Afficher la liste des joueurs créés sous forme de tableau et trier ce tableau en fonction de l'Id du joueur , de sa date de naissance  ou de son nom de famille (ordre alphabetique)
### 2) Gestion des tournois
1. Creation d'un nouveau tournoi
2. Edition des information suivantes: nom, localisation, date de debut et de fin de tournois
3. Affichage sous forme de tableau de tous les tournois existants
4. Section servant à la creation des rounds et des matches qui les composent dans un tournois selectionné par son ID
### 3) Menu destiné a l'affichage des rapport

## Creation rapport Flake 8

Installez flake8 avec la commande:

```
pip intall flake8-html
```

S'il n'existe pas, créer un fichier setup.cfg pour parametrer Flake 8 de la façon suivante.

[flake8]
exclude = .git, venv, __pycache__, .gitignore
max-line-length = 119

Tapez la commande:

```
flake8 . --format=html --htmldir=flake8_rapport
```

Le rapport sera généré dans le dossier flake8.
