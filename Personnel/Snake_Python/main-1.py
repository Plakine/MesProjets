from pygame import display
from pygame import *
import pygame
from time import time
from random import randint

class snake:
    long = 1
    haut = 1
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    dir = 0
    dir2 = 0
    arr = [[0,0,0,0]]
    nxt= [0,0]


def init():
    global v,window, isrunning, midx, midy, WHITE, game,x,y,serpent, clock,a,b,seconds,gr,gr2,fruit,points,f2,R,G,B,R1,G1,B1
    R1 =255
    G1 =255
    B1=255
    R=255
    G=0
    B=0
    pygame.font.init()
    f2 = []
    points = 0
    fruit = 0
    gr2 =1
    gr=0
    v=[0,0]
    serpent = snake()
    serpent.long=1
    serpent.haut = 1
    serpent.x1 = 0
    serpent.y1 = 0
    serpent.x2 = 0
    serpent.y2 = 0
    serpent.dir = 0
    serpent.arr = [[0,0,0,0]]
    serpent.nxt= [0,0]
    seconds =  0
    display.init()
    window = pygame.display.set_mode((1000,1000),display=0)
    game = pygame.Surface((window.get_width(),window.get_height()))
    display.set_caption("Snaaaaaaaaaaaaaaake")
    x,y= window.get_size()
    #print(x,y)
    isrunning = 1
    serpent.x1 = 495
    serpent.y1 = 495
    serpent.dir = 0
    serpent.dir2 = 0
    midx = serpent.x1
    midy = serpent.y1
    a = midx
    b = midy
  #  print(midx,midy)
    WHITE = pygame.color.Color('white')
    window.blit(game, (50, 50))
def start():
    pygame.draw.rect(game, "black", (0,0,x,y), width=0)
    window.blit(game, (0, 0))
    pygame.display.flip()
    serpent.dir = 1
    pix(midx,midy)
    serpent.dir = "left"
    grow(a,b)
    serpent.dir=0
    window.blit(game, (0, 0))


def keycheck():
    global a,b,gr
    while 1:
        window.blit(game, (50, 50))
        pix(a,b)
        frut()
        window.blit(game,(0,0))
        display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP or event.key == pygame.K_z or event.key == pygame.K_w) and serpent.dir!="down":
                    up()
                if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and serpent.dir!="up":
                    down()
                if (event.key == pygame.K_LEFT or event.key == pygame.K_q) and serpent.dir!="right":
                    left()
                if (event.key == pygame.K_RIGHT or event.key == pygame.K_d or event.key == pygame.K_a) and serpent.dir!="left":
                    right()
                if event.key == pygame.K_ESCAPE:
                    serpent.dir = 0
                if event.key == pygame.K_RETURN:
                    init()
                    start()
                if event.key == pygame.K_g and serpent.dir != 0:
                    gr = 1
                    grow(a,b)
            if event.type == pygame.QUIT:
                display.quit()
                pygame.quit()
def pix(x,y):
    global seconds,a,b,v,gr,gr2,points,fruit,R,G,B,R1,G1,B1
    if time() == seconds+0.1 or time() > seconds+0.1 and serpent.dir != 0 and gr != 1:
        seconds = time()
        if serpent.dir == "up":
            v = [0,-15]
        if serpent.dir == "down" :
            v = [0,15]
        if serpent.dir == "left" :
            v = [-15,0]
        if serpent.dir == "right" :
            v = [15,0]
        seconds = time()

        if gr2 == 1:
            for i in serpent.arr:
                if [x+v[0],y+v[1],serpent.long,serpent.haut] ==i or x+v[0]>1000 or x+v[0]<0 or y+v[1]>1000 or y+v[1]<0:
                    print("lost")
                    print(serpent.arr,x+v[0],y+v[0])
                    gr2 = 0
                    display.quit()
                    pygame.quit()
                    
        else:
            gr2=1
        if f2 == [x+v[0],y+v[1],serpent.long,serpent.haut]:
            fruit = 0 
            points = points +1
            grow(a,b)
            R1 = R
            G1 = G
            B1 = B
            for i in serpent.arr:
                    pygame.draw.rect(game,(R1,G1,B1),(i[0],i[1],15,15))
        pygame.draw.rect(game,"black",(serpent.arr[0][0],serpent.arr[0][1],15,15), width=0)
        serpent.arr.pop(0)
        pygame.draw.rect(game, (R1,G1,B1), (x+v[0],y+v[1],15*serpent.long,15*serpent.haut), width=0)
        seconds=time()
        a = x+v[0]
        b = y+v[1]
        if f2 == [x+v[0],y+v[1],serpent.long,serpent.haut]:
            fruit = 0 
            points = points +1
            grow(a,b)
            displaynum(points)
        serpent.arr.append([x+v[0],y+v[1],serpent.long,serpent.haut])
        window.blit(game,(0,0))
        display.flip()
        seconds = time()
def up():
    serpent.dir = "up"
def down():
    serpent.dir = "down"
def left():
    serpent.dir = "left"
def right():
    serpent.dir = "right"

def displaynum(num):
    global window
    number_font  = pygame.font.SysFont('Comic_sans_ms',16)                # Default font, Size 16
    number_image = number_font.render( str(num), True,(255,255,255))  # Number 8
    rect = number_image.get_rect()
    window.blit(number_image, rect)
    display.flip()
    
def grow(x,y):
        global gr,gr2,R1,G1,B1
        gr2=0
        if serpent.dir == "up":
            v = [0,-15]
        if serpent.dir == "down":
            v = [0,15]
        if serpent.dir == "left":
            v = [-15,0]
        if serpent.dir == "right":
            v = [15,0]
        if serpent.dir == 0:
            v = [0,0]
        pygame.draw.rect(game, (R1,G1,B1), (x+v[0],y+v[1],15*serpent.long,15*serpent.haut), width=0)
        serpent.arr.insert(0,[x+v[0],y+v[1],serpent.long,serpent.haut])
        seconds=time()
        a = x+v[0]
        b = y+v[1]
        gr=0
        
def frut():
    global fruit, f2,R,G,B
    if fruit != 1:
        x1 = randint(0,65)*15
        y1 = randint(0,65)*15
        R= randint(10,255)
        G=randint(10,255)
        B=randint(10,255)
        pygame.draw.rect(game,(R,G,B),(x1,y1,15,15))
        fruit = 1
        f2 = [x1,y1,serpent.long,serpent.haut]
        
        
        
init()
start()
keycheck()




