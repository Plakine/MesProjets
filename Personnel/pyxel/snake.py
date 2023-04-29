"""
Snake pyxel
"""

import pyxel as px
from random import randint


class Game():
    def __init__(self, width, squaresize, speed):
        """
        width -> largeur et hauteur de l'écran
        squaresize -> longueur d'un carré
        speed -> ips"""
        self.qcarre = width//squaresize
        self.squaresize = squaresize
        self.score = 0
        # Liste des blocs occupés par le serpet
        self.snakecoos = [(width//(squaresize*2), width//(squaresize*2)),
                          (width//(squaresize*2), width//(squaresize*2))]
        # Liste de choses à dessiner
        self.todraw = []
        self.todraw.append((self.snakecoos[0], 7))
        # Direction du serpet
        self.dir = (0, 0)
        # Crée un nouveau fruit
        self.NewFruit()
        px.init(width, width, "Snake", fps=speed)
        self.draw()
        px.run(self.update, self.draw)

    def update(self):
        # Change la direction
        if (px.btn(px.KEY_Z) or px.btn(px.KEY_UP)) and self.dir != (0, 1):
            self.dir = (0, -1)
        elif (px.btn(px.KEY_Q) or px.btn(px.KEY_LEFT)) and self.dir != (1, 0):
            self.dir = (-1, 0)
        elif (px.btn(px.KEY_S) or px.btn(px.KEY_DOWN)) and self.dir != (0, -1):
            self.dir = (0, 1)
        elif (px.btn(px.KEY_D) or px.btn(px.KEY_RIGHT))\
                and self.dir != (-1, 0):
            self.dir = (1, 0)
        # Calcul des prochaines coordonées
        newx = self.snakecoos[-1][0] + self.dir[0]
        newy = self.snakecoos[-1][1] + self.dir[1]
        if (newx, newy) in self.snakecoos and self.dir != (0, 0)\
                or (newx < 0 or newx == self.qcarre or newy < 0
                    or newy == self.qcarre):
            # Game over
            # colision avec le serpent, et les bords
            px.quit()

        # * Mouvement serpent
        self.snakecoos.append((newx, newy))
        if (newx, newy) == self.fruit:  # Serpent mange fruit
            # Ajoute à dessiner le nouveau bloc
            self.todraw.append((self.snakecoos[-1], 7))
            # Nouveau fruit
            self.NewFruit()
            self.score += 1
        else:
            self.todraw.append((self.snakecoos[0], 0))
            # Enleve dernier bloc du serpent
            self.todraw.append((self.snakecoos[-1], 7))  # Pour le joueur
            self.snakecoos.pop(0)  # Pour l'ordi

    def draw(self):
        """Dessine"""
        # Chaque carré dans la liste
        for square in self.todraw:
            px.rect(square[0][0]*self.squaresize, square[0][1]*self.squaresize,
                    self.squaresize, self.squaresize, square[1])
        # Réinitialisation de la liste
        self.todraw = []
        # Affichage du texte
        text = "score : " + str(self.score)
        px.rect(31, 0, 4*len(str(self.score)), 5, 0)
        px.text(0, 0, text, 15)

    def NewFruit(self):
        """
        Crée un nouveau fruit"""
        self.fruit = (randint(0, self.qcarre-1), randint(0, self.qcarre-1))
        # On vérifie qu'il ne se trouve pas dans le joueur
        while self.fruit in self.snakecoos:
            self.fruit = (randint(0, self.qcarre-1), randint(0, self.qcarre-1))
        self.todraw.append((self.fruit, 8))


Game(256, 8, 21)
