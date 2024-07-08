# OpenClassrooms: Projet 4: Chess Tournament
Ce programme a été créé dans le cadre du projet 4 d'OpenClassrooms. Il s'agit d'un gestionnaire de tournois d'échecs.
## Installation:
Veuillez installer Python.
Lancez ensuite la console, placez vous dans le dossier de votre choix puis clonez ce repository:
```
lien pour telechargement
```
Placez vous dans le dossier OC_P4_ChessTournament, puis créez un nouvel environnement virtuel:
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
Le menu principal est divisé en 4 options.
### 1) Gestion des joueurs
### 2) Gestion des tournois
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
