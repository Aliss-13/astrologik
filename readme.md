# 🪐 ASTRO-LOGIK

### Des calculs astronomiques irréprochables au service d'interprétations parfaitement invérifiables.

**ASTRO-LOGIK** est un projet Python de calcul astrologique utilisant de véritables données astronomiques fournies par la NASA.

L'objectif est de développer progressivement une application capable de calculer les positions planétaires et de les exploiter dans différents systèmes astrologiques.

> 🔧 **Statut : en développement**  
> Version expérimentale, interface en ligne de commande (CLI).

## ✨ Fonctionnalités actuelles

- Saisie d'une date et d'une heure.
- Validation du format de la date.
- Conversion de l'heure locale en UTC avec prise en charge des fuseaux horaires.
- Récupération des longitudes écliptiques géocentriques via l'API JPL Horizons de la NASA.
- Calcul des signes du zodiaque occidental à partir des longitudes.
- Calcul de la position en degrés dans chaque signe.
- Affichage des positions de dix corps célestes : Soleil, Lune, Mercure, Vénus, Mars, Jupiter, Saturne, Uranus, Neptune et Pluton.

## 🛠️ Technologies utilisées

- **Python**
- **Requests** : communication avec l'API NASA JPL Horizons.
- **datetime** : manipulation des dates et des heures.
- **zoneinfo / tzdata** : gestion des fuseaux horaires.
- **pytest** : tests unitaires automatisés.

## 📁 Architecture du projet

```text
ASTROLOGIK/
├── api/
│   └── astronomy.py          # Requêtes vers JPL Horizons
├── astrology/
│   └── western.py            # Calculs du zodiaque occidental
├── dates_and_time.py         # Conversion des dates en UTC
├── display.py                # Présentation du programme
├── tests/                    # Tests unitaires
└── main.py                   # Point d'entrée
```

## 🚀 Installation et utilisation

Cloner le dépôt et se placer dans le dossier du projet.

Créer et activer un environnement virtuel sous Windows :

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Installer les dépendances :

```powershell
python -m pip install requests tzdata pytest
```

Lancer le programme :

```powershell
python main.py
```

Saisir une date au format `AAAA-MM-JJ HH:MM`.

**Remarque :** le fuseau horaire est actuellement fixé à `Europe/Paris` dans l'interface principale. La fonction de conversion accepte déjà d'autres fuseaux horaires.

Une connexion Internet est nécessaire pour interroger JPL Horizons.

## 🧪 Tests unitaires

Le projet utilise `pytest` pour vérifier les calculs et conversions.

Lancer les tests :

```powershell
python -m pytest -v
```

Les tests de conversion UTC couvrent notamment :

- Les heures d'été et d'hiver à Paris.
- Les changements de date.
- Plusieurs fuseaux horaires internationaux.
- Les décalages horaires non entiers, comme celui de l'Inde.

## 🔮 Évolutions envisagées

- Choix du lieu de naissance et du fuseau horaire.
- Gestion des heures ambiguës ou inexistantes lors des changements d'heure.
- Calcul de l'ascendant et des maisons astrologiques.
- Calcul des aspects entre les planètes.
- Génération d'un thème astral.
- Exploration de différents systèmes astrologiques.
- Interprétations astrologiques.

## 📚 Objectifs pédagogiques

Ce projet me permet d'approfondir :

- La consommation d'API REST.
- Le traitement de données astronomiques.
- La manipulation des dates et des fuseaux horaires.
- L'organisation modulaire d'une application Python.
- Les tests automatisés avec `pytest`.

---

*ASTRO-LOGIK : quand l'astronomie rencontre l'astrologie, sous la surveillance inquiète de Python.* 🪐