#!/usr/bin/env python3
"""
Souris - Bouge la souris automatiquement pour garder l'ordinateur actif.

Utilisation :
    python souris.py                  # bouge toutes les 30 s
    python souris.py -i 10            # bouge toutes les 10 s
    python souris.py -m aleatoire     # mouvements aléatoires sur l'écran
    python souris.py -d 60            # s'arrête au bout de 60 minutes

Arrêt : Ctrl+C, ou envoyer la souris dans un coin de l'écran (sécurité).
"""

import argparse
import random
import sys
import time

try:
    import pyautogui
except ImportError:
    sys.exit("Il faut installer pyautogui :  pip install pyautogui")

pyautogui.FAILSAFE = True  # souris dans un coin = arrêt d'urgence


def mouvement_discret(pixels: int) -> None:
    """Petit aller-retour quasi invisible."""
    pyautogui.moveRel(pixels, 0, duration=0.2)
    pyautogui.moveRel(-pixels, 0, duration=0.2)


def mouvement_aleatoire() -> None:
    """Déplace la souris vers un point au hasard de l'écran."""
    largeur, hauteur = pyautogui.size()
    marge = 50
    x = random.randint(marge, largeur - marge)
    y = random.randint(marge, hauteur - marge)
    pyautogui.moveTo(x, y, duration=random.uniform(0.3, 1.2),
                     tween=pyautogui.easeInOutQuad)


def mouvement_cercle(rayon: int) -> None:
    """Fait un petit cercle autour de la position actuelle."""
    import math
    cx, cy = pyautogui.position()
    for i in range(1, 25):
        angle = 2 * math.pi * i / 24
        pyautogui.moveTo(cx + rayon * math.cos(angle) - rayon,
                         cy + rayon * math.sin(angle), duration=0.02)
    pyautogui.moveTo(cx, cy)


def main() -> None:
    p = argparse.ArgumentParser(description="Bouge la souris automatiquement.")
    p.add_argument("-i", "--intervalle", type=float, default=30,
                   help="secondes entre deux mouvements (défaut : 30)")
    p.add_argument("-m", "--mode", choices=["discret", "aleatoire", "cercle"],
                   default="discret", help="type de mouvement (défaut : discret)")
    p.add_argument("-p", "--pixels", type=int, default=5,
                   help="amplitude en pixels pour discret/cercle (défaut : 5)")
    p.add_argument("-d", "--duree", type=float, default=0,
                   help="durée totale en minutes, 0 = illimité")
    args = p.parse_args()

    fin = time.time() + args.duree * 60 if args.duree > 0 else None
    print(f"Souris active : mode {args.mode}, toutes les {args.intervalle:g} s.")
    print("Ctrl+C pour arrêter (ou souris dans un coin de l'écran).")

    nb = 0
    try:
        while fin is None or time.time() < fin:
            if args.mode == "discret":
                mouvement_discret(args.pixels)
            elif args.mode == "aleatoire":
                mouvement_aleatoire()
            else:
                mouvement_cercle(args.pixels * 4)
            nb += 1
            print(f"\r[{time.strftime('%H:%M:%S')}] mouvements : {nb}", end="", flush=True)
            time.sleep(args.intervalle)
    except KeyboardInterrupt:
        pass
    except pyautogui.FailSafeException:
        print("\nArrêt d'urgence (souris dans un coin).")
    print(f"\nTerminé après {nb} mouvement(s).")


if __name__ == "__main__":
    main()
