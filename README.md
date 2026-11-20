# Souris

Petit programme Python qui bouge la souris automatiquement (pour éviter la mise en veille / le statut « absent »).

## Version Windows sans installation : `Souris.exe`

Télécharge `Souris.exe` et double-clique dessus. Une fenêtre s'ouvre, et la souris bouge un tout petit peu toutes les 30 secondes. Le programme empêche aussi la mise en veille.
- Pour arrêter, ferme la fenêtre.
- Pour changer l'intervalle (en secondes), lance par exemple `Souris.exe 10` dans l'invite de commandes.
- Si Windows affiche « Windows a protégé votre ordinateur », clique sur **Informations complémentaires → Exécuter quand même**.

Le code source est dans `windows/souris.c`. Pour le recompiler :
`x86_64-w64-mingw32-gcc -O2 -s -static -o Souris.exe windows/souris.c`

## Version Python : installation

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
