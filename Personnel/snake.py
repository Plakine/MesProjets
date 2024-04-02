from pygame import display
from pygame import *
import pygame
from time import time
from random import randint

# Variables Globales
R1 =255
G1 =255
B1=255
R=255
G=0
B=0
WHITE = pygame.color.Color('white')

class snake:
    long = 1
    haut = 1
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    dir = 0
    dir2 = 0
    arr = [[0, 0, 0, 0]]
    nxt = [0, 0]

class Game:
    def __init__(self):
        """
        Défini les variables du jeu
        """
        pygame.font.init()
        self.coordonneés_fruit = []
        self.points = 0
        self.nb_fruit_écran = 0
        self.frame_invulnerabilite = 1
        self.vitesse = [0, 0]
        self.snake = snake()
        self.seconds = 0
        display.init()
        self.windows = pygame.display.set_mode((1000, 1000),display=0)
        self.surface_jeu = pygame.Surface((self.windows.get_width(), self.windows.get_height()))
        display.set_caption("Snaaaaaaaaaaaaaaake")
        self.window_width, self.window_height = self.windows.get_size()
        self.jeu_en_cours = 1
        self.snake.x1 = 495
        self.snake.y1 = 495
        self.snake.dir = 0
        self.snake.dir2 = 0
        self.centre_x = self.snake.x1
        self.centre_y = self.snake.y1
        self.tete_serpent_x = self.centre_x
        self.tete_serpent_y = self.centre_y
        self.windows.blit(self.surface_jeu, (50, 50))

        # On commence le jeu
        self.start()
        self.keycheck()

    def start(self):
        """
        Défini l'état initial d'une partie"""
        # Dessine le fond noir
        pygame.draw.rect(self.surface_jeu, "black", (0,0,self.window_width, self.window_height), width=0)
        self.windows.blit(self.surface_jeu, (0, 0))
        pygame.display.flip()
        # Donne une première direction au serpent
        self.snake.dir = 1
        # Dessine le serpent
        self.pix(self.centre_x, self.centre_y)
        self.snake.dir = "left"
        # Ajoute une case au serpent
        self.grow(self.tete_serpent_x,self.tete_serpent_y)
        self.snake.dir = 0
        self.windows.blit(self.surface_jeu, (0, 0))

    def keycheck(self):
        """
        Fonction qui traduit les entrées clavier en action
        Fonction principale du jeu
        """
        while 1:
            self.windows.blit(self.surface_jeu, (50, 50))
            self.pix(self.tete_serpent_x, self.tete_serpent_y)
            self.frut()
            self.windows.blit(self.surface_jeu, (0, 0))
            display.flip()
            for event in pygame.event.get():
                # Permet au joueur de redéfinir la direction de son serpent sans pouvoir se retourner
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_UP or event.key == pygame.K_z or event.key == pygame.K_w) and self.snake.dir != "down":
                        self.up()
                    if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and self.snake.dir != "up":
                        self.down()
                    if (event.key == pygame.K_LEFT or event.key == pygame.K_q) and self.snake.dir != "right":
                        self.left()
                    if (event.key == pygame.K_RIGHT or event.key == pygame.K_d or event.key == pygame.K_a) and self.snake.dir != "left":
                        self.right()
                    # Mets en pause le jeu
                    if event.key == pygame.K_ESCAPE:
                        self.snake.dir = 0
                    # Redémarre la partie
                    if event.key == pygame.K_RETURN:
                        pygame.font.init()
                        self.coordonneés_fruit = []
                        self.points = 0
                        self.nb_fruit_écran = 0
                        self.frame_invulnerabilite = 1
                        self.vitesse = [0, 0]
                        self.snake = snake()
                        self.seconds = 0
                        display.init()
                        self.windows = pygame.display.set_mode((1000, 1000),display=0)
                        self.surface_jeu = pygame.Surface((self.windows.get_width(), self.windows.get_height()))
                        display.set_caption("Snaaaaaaaaaaaaaaake")
                        self.window_width, self.window_height = self.windows.get_size()
                        self.jeu_en_cours = 1
                        self.snake.x1 = 495
                        self.snake.y1 = 495
                        self.snake.dir = 0
                        self.snake.dir2 = 0
                        self.centre_x = self.snake.x1
                        self.centre_y = self.snake.y1
                        self.tete_serpent_x = self.centre_x
                        self.tete_serpent_y = self.centre_y
                        self.windows.blit(self.surface_jeu, (50, 50))
                        self.start()
                # Permet de quitter le jeu
                if event.type == pygame.QUIT:
                    print("e")
                    display.quit()
                    pygame.quit()

    def pix(self, x,y):
        """
        Mets à jour le jeu
        """
        # permet d'instaurer une vitesse de jeu
        if time() == self.seconds+0.1 or time() > self.seconds+0.1 and self.snake.dir != 0:
            self.seconds = time()
            # Change la direction
            if self.snake.dir == "up":
                self.vitesse = [0,-15]
            if self.snake.dir == "down" :
                self.vitesse = [0,15]
            if self.snake.dir == "left" :
                self.vitesse = [-15,0]
            if self.snake.dir == "right" :
                self.vitesse = [15,0]
            self.seconds = time()
            # Vérifie que le joueur n'est pas en colision avec les bords ou lui même
            if self.frame_invulnerabilite == 1:
                for i in self.snake.arr:
                    if ([x+self.vitesse[0],y+self.vitesse[1],self.snake.long,self.snake.haut] ==i or x+self.vitesse[0]>1000 or x+self.vitesse[0]<0 or y+self.vitesse[1]>1000 or y+self.vitesse[1]<0):
                        self.frame_invulnerabilite = 0
                        display.quit()
                        pygame.quit()
                        exit()
            else:
                self.frame_invulnerabilite = 1
            # Vérifie la colision entre le joueur et le fruit
            if self.coordonneés_fruit == [x+self.vitesse[0],y+self.vitesse[1],self.snake.long,self.snake.haut]:
                self.nb_fruit_écran = 0
                self.points = self.points + 1
                self.grow(self.tete_serpent_x, self.tete_serpent_y)
                for i in self.snake.arr:
                        pygame.draw.rect(self.surface_jeu,(R1,G1,B1),(i[0],i[1],15,15))
            
            pygame.draw.rect(self.surface_jeu,"black",(self.snake.arr[0][0],self.snake.arr[0][1],15,15), width=0)
            self.snake.arr.pop(0)
            pygame.draw.rect(self.surface_jeu, (R1,G1,B1), (x+self.vitesse[0],y+self.vitesse[1],15*self.snake.long,15*self.snake.haut), width=0)
            self.seconds=time()
            self.tete_serpent_x = x+self.vitesse[0]
            self.tete_serpent_y = y+self.vitesse[1]
            if self.coordonneés_fruit == [x+self.vitesse[0],y+self.vitesse[1],self.snake.long,self.snake.haut]:
                self.nb_fruit_écran = 0 
                self.points = self.points +1
                self.grow(self.tete_serpent_x,self.tete_serpent_y)
            self.snake.arr.append([x+self.vitesse[0],y+self.vitesse[1],self.snake.long,self.snake.haut])
            self.windows.blit(self.surface_jeu, (0, 0))
            display.flip()
            self.seconds = time()

    # Changent la direction du serpent
    def up(self):
        self.snake.dir = "up"
    def down(self):
        self.snake.dir = "down"
    def left(self):
        self.snake.dir = "left"
    def right(self):
        self.snake.dir = "right"
        
    def grow(self, x,y):
            """
            agrandi le serpent
            """
            self.frame_invulnerabilite=0
            if self.snake.dir == "up":
                self.vitesse = [0,-15]
            if self.snake.dir == "down":
                self.vitesse = [0,15]
            if self.snake.dir == "left":
                self.vitesse = [-15,0]
            if self.snake.dir == "right":
                self.vitesse = [15,0]
            if self.snake.dir == 0:
                self.vitesse = [0,0]
            pygame.draw.rect(self.surface_jeu, (R1,G1,B1), (x+self.vitesse[0],y+self.vitesse[1],15*self.snake.long,15*self.snake.haut), width=0)
            self.snake.arr.insert(0,[x+self.vitesse[0],y+self.vitesse[1],self.snake.long,self.snake.haut])
            self.seconds=time()
            self.tete_serpent_x = x+self.vitesse[0]
            self.tete_serpent_y = y+self.vitesse[1]
            
    def frut(self):
        """
        génère un nouveau fruit
        """
        if self.nb_fruit_écran != 1:
            x1 = randint(0,65)*15
            y1 = randint(0,65)*15
            R= randint(10,255)
            G=randint(10,255)
            B=randint(10,255)
            pygame.draw.rect(self.surface_jeu,(R,G,B),(x1,y1,15,15))
            self.nb_fruit_écran = 1
            self.coordonneés_fruit = [x1,y1,self.snake.long,self.snake.haut]


Game()
