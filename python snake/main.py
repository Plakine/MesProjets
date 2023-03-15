from random import randint
from turtle import width
from pygame import display
from pygame import *
import pygame
from threading import *
# defining snake class
class snake:
    long = 1
    haut = 1
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    dir = 0
    arr = [0,0,0,0]
    nxt= [15,0]


def init():
    #globalizing the vars
    global window, isrunning, midx, midy, WHITE, game,x,y,serpent, clock,a,b,fruit


    display.init()
    window = pygame.display.set_mode((1000,1000),display=0)
    game = pygame.Surface((window.get_width(),window.get_height()))
    display.set_caption("Snaaaaaaaaaaaaaaake")
    x,y= window.get_size()

    #setting variables
    isrunning = 1
    fruit = 0
    serpent = snake()
    serpent.x1 = int(x/2)
    serpent.y1 = int(y/2)
    midx = serpent.x1
    midy = serpent.y1
    a = midx
    b = midy

#le début du jeu
def start():
    #on mets un fond noir
    pygame.draw.rect(game, "black", (0,0,x,y), width=0)
    #on l'affiche
    window.blit(game, (0, 0))
    pygame.display.flip()
    #on fait apparaitre le serpent
    pix(midx,midy)
    #on fait apparaitre un fruit
    nfruit()
    #on l'affiche
    window.blit(game, (0, 0))

#boucles
def keycheck():
    while 1:
        #on affiche tout ce qui est arrivé
        window.blit(game,(0,0))
        display.flip()
        #boucle à chaque fois que quelque chose se passe
        for event in pygame.event.get():
            #boucle si une touche a été écrit
            if event.type == pygame.KEYDOWN:
                #haut
                if event.key == pygame.K_UP or event.key == pygame.K_z or event.key == pygame.K_w:
                    up()
                    pix(a,b)
                #bas
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    down()
                    pix(a,b)
                #left
                if event.key == pygame.K_LEFT or event.key == pygame.K_d:
                    left()
                    pix(a,b)
                #Right
                if event.key == pygame.K_RIGHT or event.key == pygame.K_q or event.key == pygame.K_a:
                    right()
                    pix(a,b)
                #debug pour gros serpent
                if event.key == pygame.K_p:
                    bigsnake(a,b)
            #si altf4 ou la croix rouge
            if event.type == pygame.QUIT:
                #on éteint tout
                display.quit()
                pygame.quit()
                exit()   

#nouveau fruit
def nfruit():
    #vérifie si un fruit existe déjà (ne fonctionne pas )
    if fruit ==0:
        #trouve un emplacement aléatoire pour le fruit
        h = randint(0,49)*20
        l = randint(0,49)*20
        #l'affiche
        pygame.draw.rect(game,"red",(h,l,15,15),width=0)
#mouvement du serpent
def pix(x,y):
    #supprimme l'ancien
    pygame.draw.rect(game,"black",(serpent.arr[0],serpent.arr[1],20,20), width=0)
    #ajoute le nouveau
    pygame.draw.rect(game, "white", (x+serpent.nxt[0],y+serpent.nxt[1],20,20), width=0)
    #modifie les anciennes variables
    a = x+serpent.nxt[0]
    b = x+serpent.nxt[1]
   ## serpent.arr = [x+serpent.nxt[0],y+serpent.nxt[1],20,20]
    #les affiches
    window.blit(game,(0,0))
    display.flip()

#ne fonctionne pas 
def bigsnake(x,y):
    if serpent.dir =="up":
      serpent.nxt = [serpent.nxt[0]+0,serpent.nxt[1]-20]
    if serpent.dir =="down":
      serpent.nxt = [serpent.nxt[0]+0,serpent.nxt[1]+20]
    if serpent.dir =="left":
        serpent.nxt = [serpent.nxt[0]-20,serpent.nxt[1]+0]
    if serpent.dir =="right":
      serpent.nxt = [serpent.nxt[0]+20,serpent.nxt[1]+0]
    pygame.draw.rect(game, "white", (x+serpent.nxt[0],y+serpent.nxt[1],20,20), width=0)

    a = x+serpent.nxt[0]
    b = y+serpent.nxt[1]


#set of instruction to define the way 
def up():
    serpent.dir = "up"
    serpent.nxt = [serpent.nxt[0]+0,serpent.nxt[1]-20]
def down():
    serpent.dir = "down"
    serpent.nxt = [serpent.nxt[0]+0,serpent.nxt[1]+20]
def left():
    serpent.dir = "left"
    serpent.nxt = [serpent.nxt[0]-20,serpent.nxt[1]+0]
def right():
    serpent.dir = "right"
    serpent.nxt = [serpent.nxt[0]+20,serpent.nxt[1]+0]


#starting the program
init()
start()
keycheck()