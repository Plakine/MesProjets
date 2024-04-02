"""
Ce programme permet d'ajouter des couleurs aléatoires associé à une détection de contour
à une image en noir et blanc
"""


from PIL import Image
from random import randint


def coloration_glouton():
    # Ouvrir l'image en noir et blanc
    img = Image.open("test.jpg").convert("1")
    # Créer une image vierge en couleur
    nimg = Image.new("RGB", img.size)
    w, h = img.size
    Queue = set()
    color = (randint(0, 255), randint(0, 255), randint(0, 255))
    # Parcourir chaque pixel de l'image
    for y in range(h):
        for x in range(w):
            if img.getpixel((x, y)) != 0 and\
                  nimg.getpixel((x, y)) == (0, 0, 0):
                Queue.add((x, y))
                while len(Queue) > 0:
                    pixel = Queue.pop()
                    nimg.putpixel(pixel, color)
                    if pixel[0] < w-1:
                        if (img.getpixel((pixel[0]+1, pixel[1])) != 0 and nimg.getpixel((pixel[0]+1, pixel[1])) == (0, 0, 0)):
                            Queue.add((pixel[0]+1, pixel[1]))
                    if pixel[0] > 0:
                        if(img.getpixel((pixel[0]-1, pixel[1])) != 0 and nimg.getpixel((pixel[0]-1, pixel[1])) == (0, 0, 0)):
                            Queue.add((pixel[0]-1, pixel[1]))
                    if pixel[1] > 0:
                        if (img.getpixel((pixel[0], pixel[1]-1)) != 0 and nimg.getpixel((pixel[0], pixel[1]-1)) == (0, 0, 0)):
                            Queue.add((pixel[0], pixel[1]-1))
                    if pixel[1] < h-1:
                        if img.getpixel((pixel[0], pixel[1]+1)) != 0 and nimg.getpixel((pixel[0], pixel[1]+1)) == (0, 0, 0):
                            Queue.add((pixel[0], pixel[1]+1))
                color = (randint(0, 255), randint(0, 255), randint(0, 255))
    # Afficher l'image colorée
    nimg.show()
    nimg.save("image_coloriee.png")


coloration_glouton()
