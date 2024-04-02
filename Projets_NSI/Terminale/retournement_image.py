"""
Julien Antognelli
T°NSI
Projet de NSI :
Effectuer une rotation de 90° sur une image en programmation récursive
"""
from PIL import Image as im

# On charge l'image
image = im.open("lien de votre image ici")
image.load()


def retournement(image):
    """
    Fonction récursive qui rends l'image retournée
    de 90° dans le sens trigonométrique"""
    if image.size == (2, 2):
        # On enregistre les couleurs des différents pixels
        temp1 = image.getpixel((0, 0))
        temp3 = image.getpixel((0, 1))
        temp2 = image.getpixel((1, 0))
        temp4 = image.getpixel((1, 1))
        # On les réarrange
        image.putpixel((0, 1), temp1)
        image.putpixel((1, 1), temp3)
        image.putpixel((0, 0), temp2)
        image.putpixel((1, 0), temp4)
        return image
    else:
        # On récupère la taille de l'image
        x = image.size[0]
        y = image.size[1]
        # On définit les coordonées des différentes zones
        box1 = (0, 0, x//2, y//2)
        box2 = (x//2, 0, x, y//2)
        box3 = (0, y//2, x//2, y)
        box4 = (x//2, y//2, x, y)
        # On découpe l'image avec les zones
        im1 = retournement(image.crop(box1))
        im2 = retournement(image.crop(box2))
        im3 = retournement(image.crop(box3))
        im4 = retournement(image.crop(box4))
        # On les recolle à des endroits différents
        newimage = im.new('RGB', (x, y))
        newimage.paste(im2, (0, 0))
        newimage.paste(im4, (x//2, 0))
        newimage.paste(im1, (0, y//2))
        newimage.paste(im3, (x//2, y//2))
        return newimage


nimage = retournement(image)
nimage.save("sans_titre.png")
nimage.show()
