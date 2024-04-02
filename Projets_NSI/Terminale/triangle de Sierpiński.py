"""
programme qui dessine la fractale du triangle de sierpinski
"""
from math import sqrt
import turtle as trt

trt.delay(0)
trt.speed(0)
trt.fillcolor("yellow")
trt.penup()
# On désactive la mise à jour de l'écran pour plus de vitesse
wind = trt.Screen()
wind.tracer(0)


def triangle(dist, n):
    """
    dessine un triangle avec une profondeur de n et une taille de dist
    """
    if n == 0:
        trt.begin_fill()
        trt.forward(dist)
        trt.left(120)
        trt.forward(dist)
        trt.left(120)
        trt.forward(dist)
        trt.left(120)
        trt.forward(dist)
        trt.end_fill()
    else:
        triangle(dist/2, n-1)
        triangle(dist/2, n-1)
        trt.back(dist/2)
        trt.left(120)
        trt.forward(dist/2)
        trt.right(120)
        triangle(dist/2, n-1)
        trt.right(60)
        trt.forward(dist/2)
        trt.left(60)


def fulltriangle(dist, n):
    """
    dessine un triangle avec une profondeur de n et une taille de dist
    """
    trt.penup()
    trt.back(dist/2)
    trt.right(90)
    trt.forward((1/4)*(sqrt(3))*dist)
    trt.left(90)
    trt.pendown()
    triangle(dist, n)


fulltriangle(1000, 8)
# On affiche les changements
wind.update()
trt.exitonclick()
