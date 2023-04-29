"""
Brick Breaker
"""
from random import randint
import pyxel as px
# Redéfinis la couleur n°3
px.colors[3] = 0x4169e1


class Game:

    class Brick:
        def __init__(self, x1, y1, x2, y2):
            # * Coordonées de la brique
            self.x1 = x1
            self.x2 = x2
            self.y1 = y1
            self.y2 = y2

            self.color = 7
            # Défini si la balle peut entrer en colision avec
            # et si c'est visible
            self.visible = True
            self.degat = 0
            # Selection de la couleur
            while self.color == 7 or self.color == 3:
                self.color = randint(1, 15)
            # Brique grise = plus de vie
            if self.color == 13:
                self.vie = 3
            else:
                self.vie = 1

        def Colision(self):
            """
            inflige des dégats à une brique
            """
            self.vie -= 1
            self.degat += 1

    class Ball:
        def __init__(self, x, y, size) -> None:
            # X,Y,size sont choisis en fonction de la taille de l'écran
            self.x = x
            self.y = y
            self.size = size
            if size < 2:  # Eviter une balle trop petite
                self.size = 2
            self.speed = (randint(-size, size), randint(-size, size))
            # Vitesse nulle interdite
            while self.speed[1] == 0 or self.speed[0] == 0:
                self.speed = (randint(-size, size), randint(-size+1, size+1))

        def move(self):
            """
            movement de la balle
            """
            self.x += self.speed[0]
            self.y += self.speed[1]

        def bounce(self, bouncetype):
            """
            Collisions de la balle avec inanimé
            """
            if bouncetype == 1:  # largeur de brique
                self.speed = (self.speed[0], -self.speed[1])
            elif bouncetype == 2:  # longueur de brique
                self.speed = (-self.speed[0], self.speed[1])
            elif bouncetype == 3:  # Wall
                self.speed = (-self.speed[0], self.speed[1])
            elif bouncetype == 4:  # Roof
                self.speed = (self.speed[0], -self.speed[1])

    class Player:
        def __init__(self, x, y, width, screenwid) -> None:
            # * Défini en fonction de la taille de l'écran
            self.x = int(x)
            self.y = int(y)
            self.width = int(width)
            self.height = self.width//6
            self.winwidth = screenwid
            self.mvspeed = width//6

            self.vies = 3
            self.score = 0

        def move(self):
            """
            Mouvement de la raquette
            """
            if px.btn(px.KEY_LEFT) and self.x-self.mvspeed >= 0:
                self.x -= self.mvspeed
            if px.btn(px.KEY_RIGHT)\
               and self.x+self.width+self.mvspeed <= self.winwidth:
                self.x += self.mvspeed

    def __init__(self, width) -> None:
        # * taille de la fenêtre
        self.width = width
        self.height = (width*3)//4
        # Le joueur
        self.player = self.Player(width/2, ((
            self.height*55)/60), self.height/10, width)
        # La balle
        self.balls = [self.Ball((width//2)+10, (
            (self.height*45)//60), self.height//120)]

        # Taille d'une brique
        self.brick_width = self.width//10
        self.brick_height = self.height//20
        # Ecart visible entre les briques
        self.ecart = width//160
        # Création d'une liste de briques
        self.bricks = [
            [self.Brick((i*self.brick_width), (j*self.brick_height),
                        ((i+1)*self.brick_width), ((j+1)*self.brick_height))
                for i in range(0, 10)] for j in range(0, 10)]

        px.init(self.width, self.height, title="Casse Brique")
        px.load("Cassebrique.pyxres")
        px.run(self.update, self.draw)

    def draw(self):
        """
        affiche l'écran
        """
        px.cls(0)
        # Les balles
        for ball in self.balls:
            px.circ(ball.x, ball.y, ball.size, 7)

        # Les briques
        for brickline in self.bricks:
            for brick in brickline:
                if brick.visible is True:
                    # Le rectangle
                    px.rect(brick.x1+self.ecart, brick.y1+self.ecart,
                            (brick.x2-(brick.x1+self.ecart)),
                            (brick.y2-(self.ecart+brick.y1)), brick.color)
                    # L'image de dégat
                    if brick.degat > 0 and brick.degat < 3:
                        px.blt(brick.x1+(brick.x2-brick.x1)//2-7,
                               brick.y1+self.ecart, brick.degat,
                               0, 0, 15, 8, 7)
        # Le joueur
        px.rect(self.player.x, self.player.y, self.player.width,
                self.player.height, 3)
        # Les textes
        txt = "Score : " + str(self.player.score) + " Vies : " \
            + str(self.player.vies)
        px.text(0, (self.height-5), txt, 7)

    def update(self):
        """
        Calcul des changements
        """
        # Mouvements joueurs
        self.player.move()
        # Mpuvements balles
        for ball in self.balls:
            ball.move()
            # * Collisions
            # Murs
            if ball.x >= self.width or ball.x <= 0:
                ball.bounce(3)
                while ball.x >= self.width or ball.x <= 0:
                    ball.move()
            # Briques
            if ball.y < self.height//2 and ball.x > 0 and ball.x < self.width:
                brick = self.bricks[ball.y//self.brick_height][
                    ball.x//self.brick_width]
                if brick.visible is True:
                    brick.Colision()
                    # Brique morte
                    if brick.vie == 0:
                        brick.visible = False
                    self.player.score += 1
                    # Rebond de la balle
                    if ball.x == brick.x1 or ball.x == brick.x2:
                        ball.bounce(2)
                    else:
                        ball.bounce(1)

            # collision avec le joueur
            if ball.y >= self.player.y\
                and ball.y <= self.player.y+self.player.height\
                and ball.x >= self.player.x\
               and ball.x <= self.player.x+self.player.width:
                # Calcul du facteur de changement du x
                # position de la balle par rapport au
                # centre du joueur ramené dans -30 + 30
                # puis on en prend le sinus qui est inclus dans -1/2 + 1/2
                decalage = ((ball.x -
                             (self.player.x+(self.player.width//2)))
                            * 30)//(self.player.width//2)
                decalage = px.sin(decalage)

                if decalage > 0:
                    ball.speed = [abs(ball.speed[0]), ball.speed[1]]
                if decalage < 0:
                    ball.speed = [-abs(ball.speed[0]), ball.speed[1]]

                ball.speed = [ball.speed[0]+px.ceil(ball.speed[1]*decalage),
                              -ball.speed[1]]
                # On sort de la raquette (evite que la balle se bloque)
                while ball.y >= self.player.y\
                        and ball.y <= self.player.y+self.player.height\
                        and ball.x >= self.player.x\
                        and ball.x <= self.player.x+self.player.width:
                    ball.move()
            # Collision avec le bas
            if ball.y > self.height:
                self.newball()
                self.player.vies -= 1
                self.balls.remove(ball)
                # Game over
                if self.player.vies == -1:
                    self.gamerestart()
            # Colision avec le haut de l'écran
            if ball.y < 0:
                ball.bounce(4)

    def newball(self):
        """
        Crée une nouvelle balle
        """
        self.balls.append(self.Ball((self.width//2)+10,
                                    ((self.height*45)//60), self.height//120))

    def gamerestart(self):
        """
        Relance la partie
        """
        # Voir Game.__init__()
        width = self.width
        height = self.height
        self.player = self.Player(width/2, ((height*55)/60), height/10, width)
        self.balls = [self.Ball((width//2)+10, ((height*45)//60), height//120)]
        # Briques
        self.bricks = [[self.Brick((i*self.brick_width), (j*self.brick_height),
                                   ((i+1)*self.brick_width),
                                   ((j+1)*self.brick_height)
                                   ) for i in range(0, 10)]
                       for j in range(0, 10)]


Game(320)
