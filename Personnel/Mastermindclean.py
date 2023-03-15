# -*- coding: utf-8 -*-
"""
Créé le Jeudi 9 Juin 2022 à 10:26:38
@author: JANTOGNELLI
"""

import pyxel as pyx  # Moteur du jeu
from random import randint
from pyxelunicode import PyxelUnicode

# On définis la taille de l'écran de jeu
x, y = 1920, 1080
# On définit la police d'écriture
font_path = "pixel_unicode/Pixel-UniCode.ttf"
pyuni = PyxelUnicode(font_path, original_size=250)


class Game:  # Main loop
    def __init__(self, ecranx: int, ecrany: int) -> None:
        # Initialisations des variables
        self.tailleecranx = ecranx  # Largeur de l'écran
        self.tailleecrany = ecrany  # Hauteur de l'écran
        self.colist = [randint(1, 8), randint(1, 8),
                       randint(1, 8), randint(1, 8)]  # couleurs à deviner
        self.selected_color = 1  # Couleur sélectionné actuellement
        self.ChosenList = [None, None, None, None]  # Combinaison actuelle
        self.essais = 1  # La numérotation de l'essai en cours
        self.EcranAct = 1  # L'écran affiché actuellement (1 -> menu)
        self.todraw = 1  # Dessine les scènes pré enregistrés
        # On crée la fenêtre
        pyx.init(self.tailleecranx, self.tailleecrany, title="Mastermind")
        pyx.mouse(visible=True)
        # On lance le jeu
        pyx.run(self.update, self.draw)

    def update(self):
        # Actions clavier

        # Selection de la couleur à l'aide du clavier
        if pyx.btn(pyx.KEY_1):
            self.selected_color = 1
        if pyx.btn(pyx.KEY_2):
            self.selected_color = 2
        if pyx.btn(pyx.KEY_3):
            self.selected_color = 3
        if pyx.btn(pyx.KEY_4):
            self.selected_color = 4
        if pyx.btn(pyx.KEY_5):
            self.selected_color = 5
        if pyx.btn(pyx.KEY_6):
            self.selected_color = 6
        if pyx.btn(pyx.KEY_7):
            self.selected_color = 7
        if pyx.btn(pyx.KEY_8):
            self.selected_color = 8

        if self.EcranAct == 3 and pyx.btn(pyx.KEY_RETURN):
            # Initialisations des variables
            self.colist = [randint(1, 8), randint(1, 8),
                           randint(1, 8), randint(1, 8)]  # couleurs à deviner
            self.selected_color = 1  # Couleur sélectionné actuellement
            self.ChosenList = [None, None, None, None]  # Combinaison actuelle
            self.essais = 1  # La numérotation de l'essai en cours
            self.EcranAct = 1  # L'écran affiché actuellement (1 -> menu)
            self.todraw = 1  # Dessine les scènes pré enregistrés

        # Gestion des clics de souris

    def draw(self):
        if self.todraw == 1:
            # On dessine un fond noir
            pyx.rect(0, 0, x, y, 0)
            # On affiche le Titre
            pyuni.text(x/4, y/10, 'MasterMind', 8)
            # Boutton play
            pyx.rect(x/4, y/2, 900, 200, 7)
            pyuni.text((x/4)+275, (y/2)-50, "Play", 0)


Game(x, y)
