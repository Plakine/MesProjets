"""
Test de systeme de gravite et colisions
"""

import pyxel as px

class Game:
    class Player:
        def __init__(self):
            self.x = 0
            self.y = 64
            self.touchground = False
            self.hasreachedmax = True
    def __init__(self) -> None:
        px.init(128, 128)
        self.tmx = 0
        self.move = [0, 0]
        self.player = self.Player()
        px.load("1.pyxres")
        px.run(self.update, self.draw)

    def update(self):
        self.move = [0, self.move[1]+0.5]        
        if px.btn(px.KEY_RIGHT):
            self.move[0] += 2
        if px.btn(px.KEY_DOWN):
            self.move[1] += 2        
        if px.btn(px.KEY_UP) and self.player.touchground:
            self.move[1] = -5.5
            self.player.hasreachedmax= False
            self.player.touchground = False
        if px.btn(px.KEY_LEFT):
            if self.player.x >= 2:
                self.move[0] -= 2
        if px.pget(self.player.x+5, self.player.y+8) != 1:
            self.player.touchground = True
        move = self.isallowedmove(self.move)
        if self.player.x > 45 and (move[0] > 0 or self.tmx > 2):
            self.tmx += move[0]
        else:
            self.player.x += move[0]
        self.player.y += move[1]
    def draw(self):
        px.cls(1)
        px.bltm(0, 0, 0, self.tmx, 0, 128, 128, 2)
        px.blt(self.player.x, self.player.y, 0, 0, 16, 8, 8, 2)
    
    def isallowedmove(self, move):
        addx = 0
        addy = 0
        diff = [0,0]
        if move[0] > 0:
            diff[0] = 8
        else:
            diff[0] = -1
        while abs(addx) <= abs(move[0]) and move[0] != 0:
            x1 = px.pget(self.player.x+addx+diff[0], self.player.y)
            x2 = px.pget(self.player.x+addx+diff[0], self.player.y+7)
            if x1 == 1 and x2 == 1:
                if move[0] < 0:
                    addx -= 1
                elif move[0] > 0:
                    addx += 1
            else:
                break
        while abs(addy) <= abs(move[1]) and move[1] != 0:
            if move[1] > 0:
                y1 = px.pget(self.player.x+3, self.player.y+addy+8) in [1, 3,5,11]
                y2 = px.pget(self.player.x+5, self.player.y+addy+8) in [1, 3,5,11]
            else:
                y1 = px.pget(self.player.x, self.player.y+addy-1) in [1,3,5,6,7,11]
                y2 = px.pget(self.player.x+7, self.player.y+addy-1) in [1,3,5,6,7,11]
            if y1 and y2:
                if move[1] < 0:
                    addy -= 0.5
                elif move[1] > 0:
                    addy += 0.5
            else:
                break

        if abs(addy) < abs(move[1]):
            move[1] = addy
            self.player.hasreachedmax = True
        if abs(addx) < abs(move[0]):
            move[0] = addx
        return move

Game()