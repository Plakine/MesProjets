"""
Pong

"""
import pyxel as px
from random import randint
px.colors[3] = 0x4169e1


class Game():

    class Bot():

        def __init__(self, number) -> None:
            if number == 2:
                self.x = 780
                self.maxx = 800
            elif number == 1:
                self.x = 20
                self.maxx = 20
            self.y = 200
            self.score = 0
            self.num = number
            self.width = 20
            self.height = 60

        def move(self, balls):
            closestBall = 0
            closestdistance = 900
            for i in range(len(balls)):
                distance = ((self.maxx-balls[i].x)/balls[i].speed[0])
                if distance < closestdistance and distance > 0:
                    closestdistance = distance
                    closestBall = i
            closestBall = balls[closestBall]
            if closestBall.speed[0] < 0 and self.num == 2\
                    or closestBall.speed[0] > 0 and self.num == 1:
                if self.y < 160:
                    self.y += 10
                elif self.y > 170:
                    self.y -= 10
                return 0
            delta_y = closestBall.speed[1]*closestdistance
            curr_y = closestBall.y
            changed = 0
            for i in range(int(closestdistance)+1):
                if changed == 0:
                    if curr_y + closestBall.speed[1] < 0\
                          or curr_y + closestBall.speed[1] > 400:
                        changed = 1
                    else:
                        curr_y += closestBall.speed[1]
                else:
                    if curr_y - closestBall.speed[1] > 400\
                         or curr_y - closestBall.speed[1] < 0:
                        changed = 0
                    else:
                        curr_y += -closestBall.speed[1]
            if curr_y > self.y+30\
                    and (closestBall.y + (delta_y)) - self.y+30 > 19:
                if self.y+60 + 5 < 400:
                    self.y += 10
            elif curr_y < self.y+30 and self.y+30\
                    - (closestBall.y + (delta_y)) > 19:
                if self.y + 5 > 0:
                    self.y -= 10

    class Player():

        def __init__(self, playernum):
            if playernum == 1:
                self.x = 20
            elif playernum == 2:
                self.x = 780
            self.num = playernum
            self.y = 200
            self.score = 0
            self.width = 20
            self.height = 60

        def move(self):
            if self.num == 1:
                if px.btn(px.KEY_Z) and self.y > 0:
                    self.y -= 10
                elif px.btn(px.KEY_S) and (self.y+self.height) < 400:
                    self.y += 10
            elif self.num == 2:
                if px.btn(px.KEY_UP) and self.y > 0:
                    self.y -= 10
                elif px.btn(px.KEY_DOWN) and (self.y+self.height) < 400:
                    self.y += 10

    class Ball():
        def __init__(self, x, y, speed):
            self.x = x
            self.y = y
            self.speed = speed

        def move(self, player_y, bot_y):
            if self.y + self.speed[1] > 400\
                 or self.y + self.speed[1] < 0:
                self.Bounce(0)
            if (self.x <= 41 and self.x >= 20):
                if self.y-player_y <= 60 and self.y-player_y >= 0:
                    self.Bounce(1)
                    while (self.x <= 40) or (self.x >= 780):
                        self.x += self.speed[0]*2
                        self.y += self.speed[1]*2
            if self.y <= 800 and (self.x >= 781):
                if self.y-bot_y <= 60 and self.y-bot_y >= 0:
                    self.Bounce(1)
                    while (self.x <= 40) or (self.x >= 780):
                        self.x += self.speed[0]*2
                        self.y += self.speed[1]*2
            self.x += self.speed[0]*2
            self.y += self.speed[1]*2

        def Bounce(self, entity):
            """
            entity : int
            0 -> wall
            1 -> player/bot
            """
            if entity == 0:
                self.speed = (self.speed[0], -self.speed[1])
            elif entity == 1:
                self.speed = (-self.speed[0], self.speed[1])

    def __init__(self, playercount=1):
        self.screen_width = 800
        self.screen_height = 400
        self.plcount = playercount
        if playercount == 0:
            self.bot = self.Bot(2)
            self.player = self.Bot(1)
        elif playercount == 1:
            self.bot = self.Bot(2)
            self.player = self.Player(1)
        elif playercount == 2:
            self.bot = self.Player(2)
            self.player = self.Player(1)

        self.Balls = []
        self.NewBall()
        self.texte = str(self.player.score) + " | " + str(self.bot.score)
        px.init(self.screen_width, self.screen_height, title="Pong", fps=60)
        px.load("Pong.pyxres")
        px.run(self.update, self.draw)

    def update(self):
        if self.plcount != 0:
            self.player.move()
        else:
            self.player.move(self.Balls)
        if self.plcount != 2:
            self.bot.move(self.Balls)
        else:
            self.bot.move()
        self.MoveBall()
        if px.frame_count % 600 == 0 and px.frame_count != 0:
            self.NewBall()
        if px.btnp(px.KEY_SPACE):
            self.Balls = []
            if self.plcount == 0:
                self.player = self.Bot(1)
                self.bot = self.Bot(2)
            if self.plcount == 1:
                self.player = self.Player(1)
                self.bot = self.Bot(2)
            elif self.plcount == 2:
                self.player = self.Player(1)
                self.bot = self.Player(2)
            self.NewBall()
            self.texte = str(self.player.score) + " | " + str(self.bot.score)

    def draw(self):
        px.cls(0)
        px.rectb(0, 0, 800, 400, 7)
        if type(self.player) == self.Player:
            px.blt(self.player.x, self.player.y,
                   1, 30, 0, 21, 60)
        else:
            px.blt(self.player.x, self.player.y,
                   0, 30, 0, 21, 60)
        if type(self.bot) == self.Player:
            px.blt(self.bot.x, self.bot.y,
                   1, 0, 0, 20, 60)
        else:
            px.blt(self.bot.x, self.bot.y,
                   0, 0, 0, 20, 60)

        for ball in self.Balls:
            px.circ(ball.x, ball.y, 8, 7)
        px.text(400, 1, self.texte, 15)

    def NewBall(self):
        x = 0
        y = 0
        while x == 0:
            if self.plcount != 0:
                x = randint(-3, 3)
            else:
                x = randint(-5, 5)
        while y == 0:
            if self.plcount != 0:
                y = randint(-3, 3)
            else:
                y = randint(-5, 5)
        self.Balls.append(self.Ball(400, 200, (x, y)))

    def MoveBall(self):
        for ball in self.Balls:
            ball.move(self.player.y, self.bot.y)
            if ball.x > 800 or ball.x < 0:
                if ball.x < 0:
                    self.bot.score += 1
                elif ball.x > 800:
                    self.player.score += 1
                self.texte = (str(self.player.score) + " | " +
                              str(self.bot.score))
                if len(self.Balls) == 1:
                    self.NewBall()
                self.Balls.remove(ball)


Game(0)
