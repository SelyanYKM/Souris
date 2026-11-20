# Souris

Petit programme Python qui bouge la souris automatiquement (pour éviter la mise en veille / le statut « absent »).

## Installation

1. Installer [Python 3](https://www.python.org/downloads/) (cocher « Add Python to PATH » sous Windows).
2. Dans un terminal, dans ce dossier :
   ```
   pip install -r requirements.txt
   ```

## Utilisation

```
python souris.py                  # petit mouvement toutes les 30 s
python souris.py -i 10            # toutes les 10 s
python souris.py -m aleatoire     # se déplace au hasard sur l'écran
python souris.py -m cercle        # petit cercle
python souris.py -d 60            # s'arrête au bout de 60 minutes
```

**Arrêter :** `Ctrl+C` dans le terminal, ou envoyer la souris dans un coin de l'écran.

### Notes
- **macOS** : autoriser le Terminal dans *Réglages Système → Confidentialité et sécurité → Accessibilité*.
- **Linux** : nécessite une session X11 (sous Wayland, pyautogui peut ne pas fonctionner).
