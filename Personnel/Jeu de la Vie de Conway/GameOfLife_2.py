"""
Game of life
"""
from random import randint
import pyxel as px


class Game:
    """
    Le squelette du jeu : tout ce passe ici !
    """

    def __init__(self,  x: int = 800, fps: int = 5,
                 gridsize: int = 20, spawnpercent: int = 75,
                 randomspawn: int = 1):
        """
        Démarre le jeu avec les paramètres suivant :
        X : int -> taille de l'écran (hauteur et largeur)
        speed : int -> image par seconde
        gridsize : int -> quantité de carrés en une longeur ou hauteur
        spawnpercent: int -> chance qu'un carré soit vivant au démarrage
        randomspawn: int -> L'utilisateur veut-il un tableau aléatoire
                            ou le créer lui meme
        """
        # On définit les variables
        self.israndom = randomspawn
        self.SquareSize = int(x/gridsize)
        self.gs = gridsize
        self.sp = spawnpercent
        self.hasdrawn = 0
        # On crée la fenêtre
        px.init(x, x, "Game Of Life", fps)
        if self.israndom == 1:
            # On crée le tableau aléatoire et on l'affiche
            self.reset()
            self.gamestarted = True
        else:
            self.reset()
            self.gamestarted = False
        # On lance le jeu
        px.run(self.update, self.draw)

    def draw(self):
        """
        Draw the changes
        """
        if self.hasdrawn == 0:
            # Dessine les morts
            for (i, j) in self.todraw[0]:
                px.rect(i*self.SquareSize, j*self.SquareSize, self.SquareSize,
                        self.SquareSize, 7)
            # Dessine les vivants
            for (i, j) in self.todraw[1]:
                px.rect(i*self.SquareSize, j*self.SquareSize, self.SquareSize,
                        self.SquareSize, 0)
            self.hasdrawn = 1

    def update(self):
        """
        Calculate the next frame
        """
        if self.hasdrawn == 0:
            return -1
        if px.btn(px.KEY_CTRL):
            self.reset()
        if not self.gamestarted:
            self.Canva()
            self.hasdrawn = 0
            return 0
        if px.btn(px.KEY_D):
            self.gamestarted = False
            self.hasdrawn = 0
            return 0

        self.Calcul()

        self.Actualisation()

        # On ajoute les modifications à dessiner
        self.todraw = [self.tokill, self.tolife]
        self.hasdrawn = 0

    def Canva(self):
        px.mouse(True)
        self.tokill = []
        self.tolife = []
        if px.btn(px.KEY_E):
            self.gamestarted = True
            px.mouse(False)
            self.startinggrid = self.grid
        if px.btnp(px.MOUSE_BUTTON_LEFT):
            x = px.mouse_x
            y = px.mouse_y
            col = x//self.SquareSize
            line = y//self.SquareSize
            if self.grid[col][line] == 1:
                self.grid[col][line] = 0
            elif self.grid[col][line] == 0:
                self.grid[col][line] = 1
            self.todraw = [[], []]
        px.cls(7)
        for i in range((self.gs)):
            for j in range((self.gs)):
                if self.grid[i][j] == 0:
                    self.todraw[0].append((i, j))
                elif self.grid[i][j] == 1:
                    self.todraw[1].append((i, j))

    def Calcul(self):
        """
        Calcule l'état du tableau dans la prochaine frame
        """
        self.tokill = []
        self.tolife = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                So = self.CompteVoisins(i, j)
                if (So < 2 or So > 3) and self.grid[i][j] == 1:
                    self.tokill.append((i, j))
                elif So == 3 and self.grid[i][j] == 0:
                    self.tolife.append((i, j))

    def Actualisation(self):
        """
        Modifie le tableau pour prendre en compte la prochaine frame
        """
        for (c, l) in self.tokill:
            self.grid[c][l] = 0
        for (c, l) in self.tolife:
            self.grid[c][l] = 1

    def CompteVoisins(self, i, j):
        """
        Compte les huit voisins du carré (i,j)
        """
        Somme = 0
        for col in range(i-1, i+2):
            for line in range(j-1, j+2):
                try:
                    if not (col == i and line == j):
                        Somme += self.grid[col][line]
                except IndexError:
                    if col == len(self.grid) and line == len(self.grid):
                        Somme += self.grid[0][0]
                    elif col == len(self.grid):
                        Somme += self.grid[0][line]
                    elif line == len(self.grid):
                        Somme += self.grid[col][0]
        return Somme

    def reset(self):
        """
        On initialise un tableau et on l'affiche
        """
        if self.israndom == 1:
            # Tableau aléatoire
            self.grid = [[1 if randint(0, 100) < self.sp else 0
                         for i in range(self.gs)] for i in range(self.gs)]
        else:
            try:
                self.grid = self.startinggrid
            except AttributeError:
                self.grid = [[0 for i in range(self.gs)]
                             for j in range(self.gs)]
        # On ajoute tout à dessiner
        self.todraw = [[], []]
        for i in range((self.gs)):
            for j in range((self.gs)):
                if self.grid[i][j] == 0:
                    self.todraw[0].append((i, j))
                elif self.grid[i][j] == 1:
                    self.todraw[1].append((i, j))
        # On actualise l'affichage
        self.draw()


Game(1120, 60, 1120, 75, 1)
