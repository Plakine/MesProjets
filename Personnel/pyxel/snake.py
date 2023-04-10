"""
Snake pyxel
"""

import pyxel as px
from random import randint

class Game():
    def __init__(self, width, squaresize, speed):
        self.qcarre = width//squaresize
        self.squaresize = squaresize
        self.score = 0
        self.snakecoos = [(width//(squaresize*2), width//(squaresize*2)),(width//(squaresize*2), width//(squaresize*2))]
        self.todraw = []
        self.todraw.append((self.snakecoos[0], 7))
        self.dir = (0,0)
        self.NewFruit()
        px.init(width, width, "Snake", fps=speed)
        px.cls(0)
        self.draw()
        px.run(self.update, self.draw)

    def update(self):
        if (px.btn(px.KEY_Z) or px.btn(px.KEY_UP) ) and self.dir != (0, 1):
            self.dir = (0, -1)
        elif (px.btn(px.KEY_Q) or px.btn(px.KEY_LEFT)) and self.dir != (1, 0):
            self.dir = (-1, 0)
        elif (px.btn(px.KEY_S) or px.btn(px.KEY_DOWN)) and self.dir != (0, -1):
            self.dir = (0, 1)
        elif (px.btn(px.KEY_D) or px.btn(px.KEY_RIGHT)) and self.dir != (-1, 0):
            self.dir = (1, 0)
        
        newx = self.snakecoos[-1][0] + self.dir[0]
        newy = self.snakecoos[-1][1] + self.dir[1]
        if (newx, newy) in self.snakecoos and self.dir != (0, 0):
            # Game over
            px.quit()
        elif newx < 0 or newx == self.qcarre or newy < 0 or newy == self.qcarre:
            px.quit()
        if (newx, newy) == self.fruit or px.btn(px.KEY_G):
            self.snakecoos.append((newx, newy))
            self.todraw.append((self.snakecoos[-1], 7))
            self.NewFruit()
            self.score += 1
        else:
            self.snakecoos.append((newx, newy))
            self.todraw.append((self.snakecoos[0], 0))
            self.todraw.append((self.snakecoos[-1], 7))
            self.snakecoos.pop(0)

    def draw(self):
        for square in self.todraw:
            px.rect(square[0][0]*self.squaresize, square[0][1]*self.squaresize,
                    self.squaresize, self.squaresize, square[1])
        self.todraw = []
        text = "score : " + str(self.score)
        px.rect(31, 0, 4*len(str(self.score)), 5, 0)
        px.text(0, 0, text, 15)

    def NewFruit(self):
        self.fruit = (randint(0,self.qcarre-1), randint(0,self.qcarre-1))
        while self.fruit in self.snakecoos:
            self.fruit = (randint(0,self.qcarre-1), randint(0,self.qcarre-1))
        self.todraw.append((self.fruit, 8))

Game(128, 4, 21)