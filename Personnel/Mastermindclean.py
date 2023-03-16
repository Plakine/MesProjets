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
font_path = "pixel_unicode\\Pixel-UniCode.ttf"
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
        elif pyx.btn(pyx.KEY_2):
            self.selected_color = 2
        elif pyx.btn(pyx.KEY_3):
            self.selected_color = 3
        elif pyx.btn(pyx.KEY_4):
            self.selected_color = 4
        elif pyx.btn(pyx.KEY_5):
            self.selected_color = 5
        elif pyx.btn(pyx.KEY_6):
            self.selected_color = 6
        elif pyx.btn(pyx.KEY_7):
            self.selected_color = 7
        elif pyx.btn(pyx.KEY_8):
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
        if pyx.btn(pyx.MOUSE_BUTTON_LEFT):
            mspos_x = pyx.mouse_x
            mspos_y = pyx.mouse_y
            if self.EcranAct == 1:
                if mspos_x >= x/4 and mspos_x <= (x/4)+900:
                    if mspos_y >= y/2 and mspos_y <= (y/2)+200:
                        self.EcranAct = 2
                        self.todraw = 2

    def draw(self):
        if self.todraw == 1:
            # On dessine un fond noir
            pyx.rect(0, 0, x, y, 0)
            # On affiche le Titre
            pyuni.text(x/4, y/10, 'MasterMind', 8)
            # Boutton play
            pyx.rect(x/4, y/2, 900, 200, 7)
            pyuni.text((x/4)+275, (y/2)-50, "Play", 0)
        elif self.todraw == 2:
            # Fond noir
            pyx.rect(0, 0, x, y, 0)
            # Carré menu des couleurs
            pyx.rectb(x/8*6, y/4*3.7, x, y, 7)
            # On dessine les ronds de selection des couleurs
            for i in range(1, 9):
                pyx.circ(x/8*6+55*i, y/4*3.8, 20, i)

            # Boitier de sélection
            pyx.rectb(x/6, y/10*8.7, 500, 100, 7)
            pyx.circb(x/6+500/5, y/10*8.7+50, 30, 7)
            pyx.circb(x/6+500/5*2, y/10*8.7+50, 30, 7)
            pyx.circb(x/6+500/5*3, y/10*8.7+50, 30, 7)
            pyx.circb(x/6+500/5*4, y/10*8.7+50, 30, 7)

            # Hitbox du boitier d'essai
            self.Positions_test = [
                    (x/6+500/5-30, y/10*8.7+20, 60, 60),
                    (x/6+500/5*2-30, y/10*8.7+20, 60, 60),
                    (x/6+500/5*3-30, y/10*8.7+20, 60, 60),
                    (x/6+500/5*4-30, y/10*8.7+20, 60, 60),
                    ]

            # Bouton entrer

            # La flèche
            pyx.rect(x/6*2.6, y/10*8.7+50, 50, 40, 7)
            pyx.tri(x/6*2.6+50, y/10*8.7+40, x/6*2.6+75, y/10*8.7+70,
                    x/6*2.6+50, y/10*8.7+100, 7)


Game(x, y)
