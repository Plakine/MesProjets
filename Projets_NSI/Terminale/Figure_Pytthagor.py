"""
dessine la fractale de Pytaghore
"""


import turtle as trt
import math
from random import randint


win = trt.Screen()
win.colormode(255)
# On désactive la mise à jour de l'écran pour plus de vitesse
win.tracer(0)
trt.speed(0)
trt.delay(0)


def triangle(dist):
    trt.forward(dist)
    trt.left(150)
    trt.forward(math.cos(math.pi/6)*dist)
    trt.left(90)
    trt.forward(math.cos(math.pi/3)*dist)


def carre(dist):
    trt.fillcolor((randint(0, 255), randint(0, 255), randint(0, 255)))
    trt.begin_fill()
    for i in range(4):
        trt.forward(dist)
        trt.left(90)
    trt.end_fill()


def figure_pythagore(dist, n):
    if n == 0:
        carre(dist)
        trt.left(90)
        trt.forward(dist)
        trt.right(90)
        triangle(dist)
        trt.left(180)
        carre(math.cos(math.pi/3)*dist)
        trt.right(60)
        trt.forward(dist)
        trt.left(150)
        trt.forward(dist*math.cos(math.pi/6))
        trt.left(180)
        carre(dist*math.cos(math.pi/6))
        trt.forward(dist*math.cos(math.pi/6))
        trt.right(150)
        trt.forward(dist)
        trt.left(90)
        trt.forward(dist)
        trt.left(90)

    else:
        carre(dist)
        trt.left(90)
        trt.forward(dist)
        trt.right(90)
        triangle(dist)
        trt.left(180)
        figure_pythagore(math.cos(math.pi/3)*dist, n-1)
        trt.right(60)
        trt.forward(dist)
        trt.left(150)
        trt.forward(dist*math.cos(math.pi/6))
        trt.left(180)
        figure_pythagore(dist*math.cos(math.pi/6), n-1)
        trt.forward(dist*math.cos(math.pi/6))
        trt.right(150)
        trt.forward(dist)
        trt.left(90)
        trt.forward(dist)
        trt.left(90)


# On descends la position de départ
trt.penup()
trt.right(90)
trt.forward(300)
trt.left(90)
trt.pendown()


figure_pythagore(150, 9)
# On affiche les changements
win.update()
trt.exitonclick()
