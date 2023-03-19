"""
Game of life
"""
from random import randint
import pyxel as px


class Game:
    def __init__(self, x, y, speed, gridsize, spawnpercent):
        """
        X : int -> taille de l'écran
        Y : int -> taille de l'écran
        speed : int -> image par seconde
        gridsize : int -> quantité de carrés en une longeur ou hauteur
        spawnpercent: int -> chance qu'un carré soit vivant au démarrage
        """
        self.SquareSize = int(x/gridsize)
        print(self.SquareSize)
        self.gs = gridsize
        self.sp = spawnpercent
        self.grid = [[1 if randint(0, 100) <= self.sp else 0
                      for i in range(gridsize)] for i in range(gridsize)]
        self.todraw = [[], []]
        for i in range((self.gs)):
            for j in range((self.gs)):
                if self.grid[i][j] == 0:
                    self.todraw[0].append((i, j))
                elif self.grid[i][j] == 1:
                    self.todraw[1].append((i, j))
        px.init(x, y, "Game Of Life", speed)
        self.draw()
        px.run(self.update, self.draw)

    def draw(self):
        """
        Draw the changes
        """
        for (i, j) in self.todraw[0]:
            px.rect(i*self.SquareSize, j*self.SquareSize, self.SquareSize,
                    self.SquareSize, 7)
        for (i, j) in self.todraw[1]:
            px.rect(i*self.SquareSize, j*self.SquareSize, self.SquareSize,
                    self.SquareSize, 0)

    def update(self):
        """
        Calculate the next frame
        """
        if px.btn(px.KEY_CTRL):
            self.reset()
        tokill = []
        tolife = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                So = self.check(i, j)
                if (So < 2 or So > 3) and self.grid[i][j] == 1:
                    tokill.append((i, j))
                elif So == 3 and self.grid[i][j] == 0:
                    tolife.append((i, j))
        for (c, l) in tokill:
            self.grid[c][l] = 0
        for (c, l) in tolife:
            self.grid[c][l] = 1
        self.todraw = [tokill, tolife]

    def check(self, i, j):
        Somme = 0
        for col in range(i-1, i+2):
            for line in range(j-1, j+2):
                try:
                    if not (col == i and line == j) and col >= 0 and line >= 0:
                        Somme += self.grid[col][line]
                except IndexError:
                    pass
        return Somme

    def reset(self):
        self.grid = [[1 if randint(0, 100) < self.sp else 0
                      for i in range(self.gs)] for i in range(self.gs)]
        self.todraw = [[], []]
        for i in range((self.gs)):
            for j in range((self.gs)):
                if self.grid[i][j] == 0:
                    self.todraw[0].append((i, j))
                elif self.grid[i][j] == 1:
                    self.todraw[1].append((i, j))
        self.draw()


Game(1440, 1440, 5, 1440, 75)
