"""
Dessine la fractale du flocon de Koch"""

import turtle as trt
from math import sqrt
trt.speed(0)
trt.delay(0)
# On désactive la mise à jour de l'écran pour plus de vitesse
wind = trt.Screen()
wind.tracer(0)


def segment_koch(dist, n):
    if n == 1:
        trt.forward(dist)
    else:
        segment_koch(dist//3, n-1)
        trt.left(60)
        segment_koch(dist/3, n-1)
        trt.right(120)
        segment_koch(dist/3, n-1)
        trt.left(60)
        segment_koch(dist/3, n-1)


def triangle_koch(distance, n):
    trt.penup()
    trt.back(distance/2)
    trt.left(90)
    trt.forward((sqrt(3)*distance)/6)
    trt.right(90)
    trt.pendown()
    trt.begin_fill()
    segment_koch(distance, n)
    trt.right(120)
    segment_koch(distance, n)
    trt.right(120)
    segment_koch(distance, n)
    trt.right(120)
    trt.end_fill()


triangle_koch(750, 7)
# On affiche les changements
wind.update()
trt.exitonclick()
