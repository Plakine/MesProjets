"""
Pong

"""
import pyxel as px
from random import randint
# Redéfini la couleur numéro 3
px.colors[3] = 0x4169e1


class Game():
    """
    Le squelette du jeu
    """
    class Bot():
        """
        Les robots
        """
        def __init__(self, number) -> None:
            """
            number -> int (1||2):
                - joueur 1 ou 2
            """
            if number == 2:  # Droite de l'écran
                # Coin haut gauche du dessin
                self.x = 760
                # Position de la raquette utilisé pour calculer la trajectoire
                self.maxx = 760
            elif number == 1:  # Gauche de l'écran
                # Coin haut gauche du dessin
                self.x = 20
                # Position de la raquette utilisé pour calculer la trajectoire
                self.maxx = 40
            self.y = 200
            self.score = 0
            self.num = number
            self.width = 20
            self.height = 60

        def move(self, balls):
            """
            Fais bouger le robot
            balls : list de toutes Ball à l'écran
            """
            closestBall, closestdistance = self.get_closestball(balls)
            closestBall = balls[closestBall]
            # Cas 1 : Aucune balle ne va vers le robot
            # -> Le robot se replace au milieu
            if closestBall.speed[0] < 0 and self.num == 2\
                    or closestBall.speed[0] > 0 and self.num == 1:
                if self.y < 160:
                    self.y += 10
                elif self.y > 170:
                    self.y -= 10
                return 0
            # Calcule la coordonée y de la balle à son arrivée au robot
            curr_y = self.get_bally(closestBall, closestdistance)

            # Si le robot ne peut pas l'avoir il refait les calculs
            # avec la balle suivante
            while abs((curr_y-(self.y+30))//10) > closestdistance:
                balls = [i for i in balls if i != closestBall]
                # Si aucune n'est accessible il se replace au milieu
                if len(balls) == 0:
                    if self.y < 160:
                        self.y += 10
                    elif self.y > 170:
                        self.y -= 10
                    return 0
                closestBall, closestdistance = self.get_closestball(balls)
                closestBall = balls[closestBall]
                curr_y = self.get_bally(closestBall, closestdistance)

            # le robot décide dans quel sens bouger
            # Vers le bas
            if curr_y > self.y+30\
                    and curr_y - self.y+30 > 19:
                # Empeche le robot d'osciller autour de sa position initiale
                if self.y+60 + 5 < 400:
                    # Verifie que le robot ne sorte pas de l'écran
                    self.y += 10
            # Vers le haut
            elif curr_y < self.y+30 and self.y+30\
                    - curr_y > 19:
                if self.y + 5 > 0:
                    self.y -= 10

        def get_closestball(self, balls: list):
            """
            Cherche la balle dans balls la plus proche du robot
            """
            # Cherche la balle qui arrive le plus tôt (en quantité d'image)
            closestBall = 0
            closestdistance = 900
            for i in range(len(balls)):
                # Calcule la durée en images pour que la balle arrive
                # Distance de la raquette (pixel) / vitesse (pixel/frame)
                distance = ((self.maxx-balls[i].x)/balls[i].speed[0])
                if distance < closestdistance\
                   and distance > 0:
                    # Changer cette condition par distance < x
                    # permet de limiter la vue des robots
                    # aux balles arrivants dans moins de x images
                    closestdistance = distance
                    closestBall = i
            return closestBall, closestdistance

        def get_bally(self, closestBall, closestdistance: int) -> int:
            """
            Calcul la coordonée y ou le robot devra se placer
            closestBall : Ball -> la balle la plus proche
            closestdistance : int -> sa distance avec le joueur (en images)
            """
            curr_y = closestBall.y  # Coordonée y de la balle
            changed = 0  # La balle a-t-elle rebondi sur le mur
            # (0 -> vitesse y initiale, 1 -> vitesse y inversée)
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
            return curr_y

    class Player():

        def __init__(self, playernum):
            if playernum == 1:
                self.x = 20  # Position du joueur sur l'écran en x
            elif playernum == 2:
                self.x = 780
            self.num = playernum
            self.y = 200
            self.score = 0
            self.width = 20
            self.height = 60

        def move(self):
            """
            Change la coordonée y du joueur en fonction du bouton appuyé
            """
            # Si le joueur est le 1
            if self.num == 1:
                if px.btn(px.KEY_Z) and self.y > 0:
                    self.y -= 10
                elif px.btn(px.KEY_S) and (self.y+self.height) < 400:
                    self.y += 10
            # Si le joueur est le 2
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
            """
            Mouvements et colisions de la balle (sauf entre balles)
            """
            # Colision avecle mur
            if self.y + self.speed[1] > 400\
                    or self.y + self.speed[1] < 0:
                self.Bounce(0)
                while self.y + self.speed[1] > 400\
                        or self.y + self.speed[1] < 0:
                    self.x += self.speed[0]*2
                    self.y += self.speed[1]*2

            # Colision avec la raquette gauche
            if (self.x <= 41 and self.x >= 20):
                if self.y-player_y <= 60 and self.y-player_y >= 0:
                    self.Bounce(1)
                    while (self.x <= 40) or (self.x >= 760):
                        self.x += self.speed[0]*2
                        self.y += self.speed[1]*2
            # Colision avec la raquette droite
            if self.y <= 800 and (self.x >= 760):
                if self.y-bot_y <= 60 and self.y-bot_y >= 0:
                    self.Bounce(1)
                    while (self.x <= 40) or (self.x >= 760):
                        self.x += self.speed[0]*2
                        self.y += self.speed[1]*2
            # Mouvement classique
            self.x += self.speed[0]*2
            self.y += self.speed[1]*2

        def Bounce(self, entity):
            """
            Inverse la vitesse d'une balle en fonction du type de colision
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
        # Selection du nombre de joueurs
        if playercount == 0:
            self.bot = self.Bot(2)
            self.player = self.Bot(1)
        elif playercount == 1:
            self.bot = self.Bot(2)
            self.player = self.Player(1)
        elif playercount == 2:
            self.bot = self.Player(2)
            self.player = self.Player(1)

        # Crée un balle
        self.Balls = []
        self.NewBall()

        self.texte = str(self.player.score) + " | " + str(self.bot.score)
        px.init(self.screen_width, self.screen_height, title="Pong", fps=60)
        px.load("Pong.pyxres")
        px.run(self.update, self.draw)

    def update(self):
        """
        Calcule les changements
        """
        # * Mouvement des raquettes
        # Passe en argument la liste de balles si l'objet est un robot
        if self.plcount != 0:
            self.player.move()
        else:
            self.player.move(self.Balls)

        if self.plcount != 2:
            self.bot.move(self.Balls)
        else:
            self.bot.move()

        # * Mouvement des balles
        self.MoveBall()

        # Nouvelle balle toutes les 10s (à 60 ips)
        if px.frame_count % 600 == 0 and px.frame_count != 0:
            self.NewBall()

        # * reset du jeu
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
        """
        Dessine les changements
        """
        px.cls(0)
        px.rectb(0, 0, 800, 400, 7)  # Bordure du terrain

        # * Affichage des raquettes

        # A gauche
        if type(self.player) == self.Player:  # Cas 1 : joueur
            px.blt(self.player.x, self.player.y,
                   1, 30, 0, 21, 60)
        else:  # Cas 2 robot
            px.blt(self.player.x, self.player.y,
                   0, 30, 0, 21, 60)
        # A droite
        if type(self.bot) == self.Player:  # Cas joueur
            px.blt(self.bot.x, self.bot.y,
                   1, 0, 0, 20, 60)
        else:  # Cas robot
            px.blt(self.bot.x, self.bot.y,
                   0, 0, 0, 20, 60)

        for ball in self.Balls:
            px.circ(ball.x, ball.y, 8, 7)
        px.text(400, 1, self.texte, 15)

    def NewBall(self):
        """
        Crée une nouvelle balle
        """
        x = 0
        y = 0
        while x == 0:
            if self.plcount != 0:
                x = randint(-3, 3)  # Au moins 1 joueur
            else:
                x = randint(-5, 5)  # 0 joueurs (balles peuvent etre + rapide)
        while y == 0:
            if self.plcount != 0:
                y = randint(-3, 3)  # Au moins 1 joueur
            else:
                y = randint(-5, 5)  # 0 joueurs (balles peuvent etre + rapide)
        self.Balls.append(self.Ball(400, 200, (x, y)))

    def MoveBall(self):
        """
        Effectue les mouvement pour les balles
        """
        # Colision interballe
        for ball in self.Balls:
            ballcoos = [(ball.x, ball.y) for ball in self.Balls]
            for val in ballcoos:
                if (ball.x-4 <= val[0]+4 and val[0]-4 <= ball.x+4)\
                    and (ball.y-4 <= val[1]+4 and val[1]-4 <= ball.y+4)\
                        and (ball.x != val[0] or ball.y != val[1]):
                    # Colision
                    if (ball.x-4 <= val[0]+4 and val[0]-4 <= ball.x+4)\
                            and (ball.y-4 <= val[1]+4 and
                                 val[1]-4 <= ball.y+4):
                        ball.speed = [-ball.speed[0], -ball.speed[1]]
                    elif (ball.x-4 <= val[0]+4 and val[0]-4 <= ball.x+4):
                        ball.speed = [-ball.speed[0], ball.speed[1]]
                    elif (ball.y-4 <= val[1]+4 and val[1]-4 <= ball.y+4):
                        ball.speed = [ball.speed[0], -ball.speed[1]]
                elif (ball.x+4 <= val[0]-4 and val[0]+4 <= ball.x-4)\
                        and (ball.y+4 <= val[1]-4 and val[1]+4 <= ball.y-4)\
                        and (ball.x != val[0] or ball.y != val[1]):
                    # Colision
                    if (ball.x+4 <= val[0]-4 and val[0]+4 <= ball.x-4)\
                            and (ball.y+4 <= val[1]-4 and
                                 val[1]+4 <= ball.y-4):
                        ball.speed = [-ball.speed[0], -ball.speed[1]]
                    elif (ball.x+4 <= val[0]-4 and val[0]+4 <= ball.x-4):
                        ball.speed = [-ball.speed[0], ball.speed[1]]
                    elif (ball.y+4 <= val[1]-4 and val[1]+4 <= ball.y-4):
                        ball.speed = [ball.speed[0], -ball.speed[1]]
            # Mouvements "classiques"
            ball.move(self.player.y, self.bot.y)

            # Colision balle - But
            if ball.x > 800 or ball.x < 0:
                if ball.x < 0:
                    self.bot.score += 1
                elif ball.x > 800:
                    self.player.score += 1
                self.texte = (str(self.player.score) + " | " +
                              str(self.bot.score))  # Change le score affiché
                if len(self.Balls) == 1:
                    self.NewBall()  # Maintient au moins une balle
                self.Balls.remove(ball)


Game(0)
