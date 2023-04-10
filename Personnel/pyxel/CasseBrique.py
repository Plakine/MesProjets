"""
Brick Breaker
"""
from random import randint
import pyxel as px
px.colors[3] = 0x4169e1


class Game:

    class Brick:
        def __init__(self, x1, y1, x2, y2) -> None:
            self.x1 = x1
            self.x2 = x2
            self.y1 = y1
            self.color = 7
            self.visible = True
            self.degat = 0
            while self.color == 7 or self.color == 3:
                self.color = randint(1, 15)
            if self.color == 13:
                self.vie = 3
            else:
                self.vie = 1
            self.y2 = y2

        def Colision(self):
            self.vie -= 1
            self.degat += 1

    class Ball:
        def __init__(self, x, y, size) -> None:
            self.x = x
            self.y = y
            self.size = size
            if size < 2:
                self.size = 2
            self.speed = (randint(-size, size), randint(-size, size))
            while self.speed[1] == 0 or self.speed[0] == 0:
                self.speed = (randint(-size, size), randint(-size+1, size+1))

        def move(self):
            self.x += self.speed[0]
            self.y += self.speed[1]

        def bounce(self, bouncetype):
            if bouncetype == 1:  # Y bounce
                self.speed = (self.speed[0], -self.speed[1])
            elif bouncetype == 2:  # X bounce
                self.speed = (-self.speed[0], self.speed[1])
            elif bouncetype == 3:  # Wall
                self.speed = (-self.speed[0], self.speed[1])
            elif bouncetype == 4:  # Roof
                self.speed = (self.speed[0], -self.speed[1])

    class Player:
        def __init__(self, x, y, width, screenwid) -> None:
            self.x = int(x)
            self.y = int(y)
            self.width = int(width)
            self.height = self.width//6
            self.winwidth = screenwid
            self.vies = 3
            self.score = 0
            self.mvspeed = width//6

        def move(self):
            if px.btn(px.KEY_LEFT) and self.x-self.mvspeed >= 0:
                self.x -= self.mvspeed
            if px.btn(px.KEY_RIGHT)\
               and self.x+self.width+self.mvspeed <= self.winwidth:
                self.x += self.mvspeed

    def __init__(self, width) -> None:
        self.width = width
        self.height = (width*3)//4
        self.player = self.Player(width/2, ((self.height*55)/60),
                                  self.height/10, width)
        self.ecart = width//160
        self.balls = [self.Ball((width//2)+10, ((self.height*45)//60),
                                self.height//120)]
        self.brick_width = self.width//10
        self.brick_height = self.height//20
        self.bricks = [[self.Brick((i*self.brick_width),
                        (j*self.brick_height), ((i+1)*self.brick_width),
                         ((j+1)*self.brick_height)) for i in range(0, 10)]
                       for j in range(0, 10)]

        px.init(self.width, self.height, title="Casse Brique")
        px.load("Cassebrique.pyxres")
        px.run(self.update, self.draw)

    def draw(self):
        px.cls(0)
        for ball in self.balls:
            px.circ(ball.x, ball.y, ball.size, 7)
        for brickline in self.bricks:
            for brick in brickline:
                if brick.visible is True:
                    px.rect(brick.x1+self.ecart, brick.y1+self.ecart,
                            (brick.x2-(brick.x1+self.ecart)),
                            (brick.y2-(self.ecart+brick.y1)), brick.color)
                    if brick.degat > 0 and brick.degat < 3:
                        px.blt(brick.x1+(brick.x2-brick.x1)//2-7,
                               brick.y1+self.ecart, brick.degat, 0, 0, 15, 8,
                               7)
        px.rect(self.player.x, self.player.y,
                self.player.width, self.player.height, 3)
        txt = ("Score : " + str(self.player.score) + " Vies : "
               + str(self.player.vies))
        px.text(0, (self.height-5), txt, 7)

    def update(self):
        self.player.move()
        for ball in self.balls:
            ball.move()
            if ball.x >= self.width or ball.x <= 0:
                ball.bounce(3)
                while ball.x >= self.width or ball.x <= 0:
                    ball.move()
            if ball.y < self.height//2 and ball.x > 0 and ball.x < self.width:
                brick = self.bricks[ball.y//self.brick_height][
                    (ball.x//self.brick_width)]
                if brick.visible is True:
                    brick.Colision()
                    if brick.vie == 0:
                        brick.visible = False
                    self.player.score += 1
                    if ball.x == brick.x1 or ball.x == brick.x2:
                        ball.bounce(2)
                    else:
                        ball.bounce(1)
            # collision avec le joueur
            if ball.y >= self.player.y\
                and ball.y <= self.player.y+self.player.height\
                and ball.x >= self.player.x\
                    and ball.x <= self.player.x+self.player.width:
                decalage = ((ball.x - (self.player.x+(self.player.width//2)))
                            * 30)//(self.player.width//2)
                decalage = px.sin(decalage)
                if decalage > 0:
                    ball.speed = [abs(ball.speed[0]), ball.speed[1]]
                if decalage < 0:
                    ball.speed = [-abs(ball.speed[0]), ball.speed[1]]
                ball.speed = [ball.speed[0]+px.ceil(ball.speed[1]*decalage),
                              -ball.speed[1]]
                while ball.y >= self.player.y\
                    and ball.y <= self.player.y+self.player.height\
                        and ball.x >= self.player.x\
                        and ball.x <= self.player.x+self.player.width:
                    ball.move()
            # Collision avec les murs
            if ball.y > self.height:
                self.newball()
                self.player.vies -= 1
                self.balls.remove(ball)
                if self.player.vies == -1:
                    self.gamerestart()
            if ball.y < 0:
                ball.bounce(4)

    def newball(self):
        self.balls.append(self.Ball((self.width//2)+10,
                                    ((self.height*45)//60), self.height//120))

    def gamerestart(self):
        width = self.width
        height = self.height
        self.player = self.Player(width/2, ((height*55)/60), height/10, width)
        self.balls = [self.Ball((width//2)+10, ((height*45)//60), height//120)]
        self.bricks = [[self.Brick((i*self.brick_width),
                        (j*self.brick_height), ((i+1)*self.brick_width),
                        ((j+1)*self.brick_height)) for i in range(0, 10)]
                       for j in range(0, 10)]


Game(320)
