
# 🚀 TLS Flooding Script

Ce script Python est conçu pour réaliser une attaque DDoS en utilisant des requêtes HTTP sur un serveur cible via des proxys. Il utilise des threads pour simuler plusieurs connexions en parallèle et envoie des requêtes HTTP en utilisant des User-Agents aléatoires. Ce script est principalement destiné à des fins d'apprentissage et de tests dans un environnement contrôlé.

## 📋 Prérequis

Avant d'exécuter ce script, assurez-vous d'avoir installé Python 3.7 ou une version plus récente, ainsi que les bibliothèques suivantes:

- `httpx` pour la gestion des requêtes HTTP
- `colorama` pour afficher des messages colorés dans le terminal

### Installation des dépendances

Utilisez la commande suivante pour installer les dépendances nécessaires via `pip`:

```bash
pip install httpx colorama
```

## 🛠️ Utilisation

### Lancer le script

Pour exécuter le script, vous devez spécifier quatre paramètres dans la ligne de commande:

1. **host** : L'URL de la cible (exemple : `https://triplemonstre.com`)
2. **time** : La durée de l'attaque en secondes
3. **rps** : Le nombre de requêtes par seconde
4. **threads** : Le nombre de threads pour paralléliser l'attaque

### Exemple de commande

```bash
python tls.py https://triplemonstre.com 60 100 10
```

Cela enverra des requêtes HTTP à `https://triplemonstre.com` pendant 60 secondes, avec un débit de 100 requêtes par seconde, en utilisant 10 threads pour répartir la charge.

### Fichiers requis

- **proxy.txt** : Liste des proxys (un par ligne, format `IP:PORT`).
- **ua.txt** : Liste des User-Agents (un par ligne).

Le script lira ces fichiers pour récupérer aléatoirement des proxys et des User-Agents à chaque requête.

## 🔧 Fonctionnement du script

1. **Lecture des fichiers de proxys et de User-Agents** : Le script lit les fichiers `proxy.txt` et `ua.txt` pour obtenir des proxys et des User-Agents aléatoires.
2. **Génération d'en-têtes HTTP** : Chaque requête est envoyée avec des en-têtes HTTP générés dynamiquement, y compris un User-Agent aléatoire et une adresse IP aléatoire dans l'en-tête `X-Forwarded-For` pour masquer l'origine des requêtes.
3. **Envoi de requêtes** : Le script envoie des requêtes HTTP à la cible en utilisant les proxys spécifiés. Chaque requête est envoyée via une connexion HTTPS sécurisée.
---
## ⚠️ Avertissements

- **Utilisation responsable** : Ce script est destiné à des fins éducatives et ne doit être utilisé que sur des systèmes pour lesquels vous avez l'autorisation de tester la résistance. L'utilisation de ce script sur des systèmes sans autorisation peut être illégale.
- **Proxies** : Vous devez fournir une liste de proxys fonctionnels dans le fichier `proxy.txt`. Assurez-vous que les proxys sont valides et non bloqués par la cible.


---

🚨 **Disclaimer** : Ce script ne doit être utilisé que dans un cadre légal et contrôlé. Toute utilisation à des fins malveillantes est strictement interdite.
