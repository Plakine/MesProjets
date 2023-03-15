# -*- coding: utf-8 -*-
"""
Créé le Jeudi 9 Juin 2022 à 10:26:38
@author: JANTOGNELLI
"""

import pyxel as pyx #Moteur du jeu 

try:
    from win32api import GetSystemMetrics #Si on est sur Windows on récupère la taille de l'écran 
    x,y = GetSystemMetrics
except ModuleNotFoundError:
    x,y = 1920,1080    


class Game:  #Main loop
    def __init__(self,ecranx:int,ecrany:int) -> None:
        self.tailleecranx = ecranx
        self.tailleecrany = ecrany
    
    def update():
        pass
    def draw():
        pass