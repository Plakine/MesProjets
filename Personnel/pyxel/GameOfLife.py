"""
Game of life
"""
from random import randint
import pyxel as px

# Le blanc devient du vrai blanc
px.colors[7] = 0xFFFFFF


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
            # Dessine les nouveaux morts
            for (i, j) in self.todraw[0]:
                px.rect(i*self.SquareSize, j*self.SquareSize, self.SquareSize,
                        self.SquareSize, 7)
            # Dessine les nouveaux vivants
            for (i, j) in self.todraw[1]:
                px.rect(i*self.SquareSize, j*self.SquareSize, self.SquareSize,
                        self.SquareSize, 0)
            self.hasdrawn = 1

    def update(self):
        """
        Calculate the next frame
        """
        if self.hasdrawn == 0:
            # S'il n'a pas fini de dessiner on ne touche à rien
            return 0
        # Mode dessin
        if not self.gamestarted:
            px.mouse(True)  # Affichage sours
            self.tokill = []
            self.tolife = []
            # Lancement de la simulation
            if px.btn(px.KEY_E):
                self.gamestarted = True
                px.mouse(False)
                self.startinggrid = self.grid

            # Changment d'état d'une case
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
            # On ajoute tout au taches de dessin
            # Pour recouvrir la souris
            px.cls(7)
            for i in range((self.gs)):
                for j in range((self.gs)):
                    if self.grid[i][j] == 0:
                        self.todraw[0].append((i, j))
                    elif self.grid[i][j] == 1:
                        self.todraw[1].append((i, j))
            self.hasdrawn = 0
            return 0
        self.hasdrawn = 0
        # Reset du tableau
        if px.btn(px.KEY_CTRL):
            self.reset()
            return 0
        # Activation mode dessin
        if px.btn(px.KEY_D):
            self.gamestarted = False
            return 0

        self.Calcul()

        self.Actualisation()

        # On ajoute les modifications à dessiner
        self.todraw = [self.tokill, self.tolife]

    def Calcul(self):
        """
        Calcule l'état du tableau dans la prochaine frame
        """
        self.tokill = []
        self.tolife = []
        # On itere chaque carre
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
        necesserairement post calcul pour eviter que le tableau change au fur
        et a mesure des calculs"""
        for (c, l) in self.tokill:
            self.grid[c][l] = 0
        for (c, l) in self.tolife:
            self.grid[c][l] = 1

    def CompteVoisins(self, i, j):
        """
        Compte les huit voisins du carré (i,j)
        """
        Somme = 0
        for ligne in range(i-1, i+2):
            for colonne in range(j-1, j+2):
                try:
                    if not (ligne == i and colonne == j):
                        Somme += self.grid[ligne][colonne]
                except IndexError:  # Si la case passe par un bord
                    if ligne == len(self.grid) and colonne == len(self.grid):
                        # Bas droite
                        Somme += self.grid[0][0]
                    elif ligne == len(self.grid):  # bas
                        Somme += self.grid[0][colonne]
                    elif colonne == len(self.grid):  # droite
                        Somme += self.grid[ligne][0]
        return Somme

    def reset(self):
        """
        On initialise un tableau et on l'affiche
        """
        if self.israndom == 1:
            # Tableau aléatoire
            self.grid = [[1 if randint(0, 100) < self.sp else 0
                         for i in range(self.gs)] for j in range(self.gs)]
        else:
            try:
                self.grid = self.startinggrid
            except IndexError:
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


Game(800, 10, 80, 25, 1)
