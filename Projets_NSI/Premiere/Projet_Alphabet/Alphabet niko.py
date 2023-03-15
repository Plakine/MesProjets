from sys import exit
import turtle as trt
from math import pi


class Alphabet():
# =============================================================================
#     def a():
#       print('a')
#     def b():
# 
#     def c():
# 
#     def d():
# 
#     def e():
# 
#     def f():
# 
#     def g():
# 
#     def h():
# 
#     def i():
# 
#     def j():
# 
#     def k():
# 
#     def l():
# 
#     def m():
# 
#     def n():
# 
#     def o():
# 
#     def p():
# 
#     def q():
# 
#     def r():
# 
#     def s():
#         
#     def t():
# 
#     def u():
# 
#     def v():
# 
#     def w():
# 
#     def x():
# 
#     def y():
# 
#     def z():
# 
    def A(H,L,x):
        trt.setheading(90+x)
        trt.left(343.3)
        trt.forward(1.04*H)
        trt.left(213.4)
        trt.forward(1.04*H)
        trt.back(0.507*H)
        trt.left(253.3)
        trt.forward(0.5*L)
        trt.back(0.5*L)
        trt.right(253.3)
        trt.forward(0.507*H)

    def B(H,L,x):
        trt.setheading(90+x)
        trt.forward(H*0.7)
        for i in range(180):
            trt.forward(((0.4*pi)*H)/220)
            trt.right(96/70)
        dir = trt.heading()
        trt.setheading(180)
        trt.forward(L*0.2)
        trt.back(L*0.2)
        trt.setheading(dir)
        trt.left(130)
        for i in range(180):
            trt.forward(((0.61*pi)*H)/320)
            trt.right(96/80)
        trt.up()
        trt.setheading(270)
        trt.forward(5)
        trt.setheading(0)
        trt.forward(L)

    def C(H,L,x):
        trt.up()
        trt.forward(L*(2/3))
        trt.setheading(180-x)
        trt.down()
        for i in range(180):
            trt.forward(0.4)
            trt.right(1)
        trt.up()
        trt.setheading(270-x)
        trt.forward(H-(0.09*H))

    def D(H,L,x):
        trt.setheading(90+x)
        trt.forward(H)
        trt.setheading(0)
        for i in range(145):
            trt.forward((pi*H)/280)
            trt.right(1.25)
        trt.up()
        trt.setheading(180)
        trt.forward(1.5)
        trt.back(20)
   
    def E(H,L,x):
        trt.setheading(90+x)

        for i in range(2):
            trt.left(270)
            trt.forward(L)
            trt.back(L)
            trt.right(270)
            trt.forward(H/2)
        trt.left(270)
        trt.forward(L)
        trt.up()
        trt.setheading(270)
        trt.forward(H)

    def F(H,L,x):
        trt.setheading(90+x)
        trt.forward(H/4)
        for i in range(2):
            trt.forward(H*1.5/4)
            trt.left(270)
            trt.forward(L)
            trt.back(L)
            trt.right(270)
        trt.left(270)
        trt.up()
        trt.forward(L)
        trt.left(270)
        trt.forward(H)

    def G(H,L,x):
        getattr(Alphabet,"C")(H,L,x)
        trt.setheading(90+x)
        trt.down()
        trt.forward(H/3)
        trt.left(90)
        trt.forward(L/3)
        trt.up()
        trt.back(L/3)
        trt.right(90)
        trt.back(H/3)
        trt.right(90)

    def H(H,L,x):
        trt.setheading(90+x)
        trt.forward(H)
        trt.back(H/2)
        trt.left(270)
        trt.forward(L)
        trt.right(270)
        trt.forward(H/2)
        trt.back(H)

    def I(H,L,x):
        trt.up()
        trt.forward(L)
        trt.setheading(180+x)
        trt.down()
        trt.forward(L)
        trt.back(L/2)
        trt.left(270)
        trt.forward(H)
        trt.left(270)
        trt.forward(L/2)
        trt.back(L)
        trt.up()
        trt.setheading(270)
        trt.forward(H)
        trt.setheading(0)
        trt.forward(L)

#! J NE FONCTIONNE PAS EN ITALIQUE
    def J(H,L,x):
        trt.setheading(90)
        trt.up()
        trt.forward(H)
        trt.down()
        trt.setheading(0-x)
        trt.forward(L)
        trt.right(90)
        trt.forward(H*1.5/2)
        for i in range(180):
            trt.forward(0.008*L)
            trt.right(1)
        trt.up()
        trt.setheading(270)
        trt.forward(H/4.1)
        trt.setheading(0)
        trt.forward(L)

    def K(H,L,x):
        trt.setheading(90+x)
        trt.forward(H/2)
        trt.left(210.96)
        trt.forward(H*0.6)
        trt.back(H*0.58)
        trt.right(241.93)
        trt.forward(0.58*H)
        trt.back(H*0.58)
        trt.right(329.04)
        trt.forward(H/1.8)
        trt.left(270)
        trt.up()
        trt.forward(L*0.5)
        trt.left(270)
        trt.forward(H)

    def L(H,L,x):
        trt.setheading(90+x)
        trt.forward(H)
        trt.back(H)
        trt.right(90)
        trt.forward(L)

    def M(H,L,x):
        L*=2
        trt.setheading(90+x)
        trt.left(343.3)
        trt.forward(1.04*H)
        trt.left(213.4)
        trt.forward(1.04*H)
        trt.left(146.6)
        trt.forward(1.04*H)
        trt.left(213.4)
        trt.forward(1.04*H)
#     def N():
# 
#     def O():
# 
#     def P():
# 
#     def Q():
# 
#     def R():
# 
#     def S():
# 
    def T(H,L,x):
        trt.setheading(90+x)
        trt.forward(H)
        trt.left(270)
        trt.forward(L/2)
        trt.back(L)
        trt.right(90)
        trt.up()
        trt.forward(H)
        trt.setheading(0)
        trt.forward(L/2)
#     def U():
# 
#     def V():
# 
#     def W():
# 
#     def X():
# 
#     def Y():
# 
#     def Z():
#   
# 
# =============================================================================

#TODO(Lettres) lettres minuscules : all; Lettres Majuscules : N,O,P,Q,R,S,U,V,W,X,Y,Z; Total -> 26+12 = 38 lettres TODO 
#! Problème J -> Italique ne marche pas 

#TODO(Paramètres) Souligné

#*Fonction Principales   
def writer(mot:str,#* Mot à écrire (Type -> string)
gras:int=0, #* Mode Gras (1 : oui, 0: non, défault(0)) (Type -> int)
italique:int=0, #* Mode Italique (1:oui  0:non, défault(0)) (Type -> int)
startcenter:int = 0, #* Mode Centrée (1:oui 0:non, défault(0)) (Type -> int)
taillex:int=1920, #* Largeur de L'écran (défault(1920)) (Type -> int)
tailley:int=1080, #* Hauteur de L'écran (défault(1080)) (Type -> int)
Taillepolice:int = 50, 
#* Taille générale de la police (défault(50)) (Type -> int)
Policeheight:int=50, 
#* Hauteur de la Police (Défault(50 ou Taillepolice)) (Type -> int)
PoliceLarge:int=30,
#* Largeur de la Police (Défault(30 ou 0.6*Taillepolice)) (Type -> int)
couleur:str = "black" #* Couleur de la police (Défault(Black)) (Type -> str)
):
    
    #Change la couleur
    try:
        trt.color(couleur)
    except:
        #Renvoie une erreur 
        print('not a valid color')

    #Vérifies que tout a été effacé
    trt.clear()

    #définit la taille de la police 
    #Rapport de 0.6 trouvé sur itnernet
    if Taillepolice!=0:
        Policeheight = Taillepolice
        PoliceLarge = Taillepolice*0.6

    #Accélere la tortue
    trt.speed(-1)
    trt.delay(0)

    #Crée la surface avec les dimensions choises
    trt.screensize(taillex,tailley)
    trt.Screen().setup(1.0,1.0)

    #Va à la première ligne
    trt.up()
    trt.goto((0-taillex/2)+20,(0+tailley/2)-15-Taillepolice)
    trt.setheading(90)
    trt.down()

    #Différents modes d'écritures

    #Mode Gras
    x=0
    if gras == 1:
        trt.width(5)

    #Mode Italique
    if italique ==1:
        x = -5
        trt.width((trt.width()/2))

    #Mode Centré
    if startcenter == 1:
        a = 0
        Seize=[a]
        line = 1
        for letter in mot:
            Seize[a] += PoliceLarge+20
            if Seize[a] >= trt.screensize()[0]-50:
                line +=1
                Seize.append((-taillex+50))
                a+=1
        a=0
        trt.up()
        trt.goto(-(Seize[0]/2),Policeheight+20 + Policeheight*line/2)

    #Boucles principales
    for letter in mot:
        try:
            #Récupère la fonction du nom de la lettre
            fonction  = getattr(Alphabet,letter)

            #Vérifies qu'on n'est pas à la fin de la ligne
            if ((trt.pos()[0])+PoliceLarge*2) >= (taillex)/2:

                #Si on est pas centré
                if startcenter!=1:
                    trt.up()
                    trt.goto(0-taillex/2+PoliceLarge/5,trt.pos()[1]-Policeheight*1.8)

                #Si on est centré
                else:
                    a+=1
                    trt.up()
                    trt.goto(trt.goto(-(Seize[a]/2),trt.pos()[1] -Policeheight+20-Policeheight))
        
                #Remets le stylo en marche au cas ou
            trt.down()
            
            #Vérifies qu'on a pas atteint la fin de l'écran
            if (trt.pos()[1]-Policeheight*2)<=-(trt.screensize()[1]/2):
                #Rajoute de la place
                trt.screensize(taillex,trt.screensize()[1]+Policeheight)
            
            #Appelle la fonction pour dessinger la lettre
            fonction(Policeheight,PoliceLarge,x)
            
            #Se remets en place pour la prochaine lettre
            trt.setheading(0)
            trt.up()
            #Mode Italique
            if x != 0 and letter != "C":
                trt.left(3.5)
            trt.forward(20)

        except:
            #On arrive ici si on essaye d'utiliser un caractère qui n'existe pas donc Cas Spéciaux
            
            #Espaces
            if letter == " ":
                trt.up()
                trt.forward(40)
            else:
                exit()

    trt.exitonclick()     
    # Permet de fermer la fenêtre de turtle à la fin du programme
   
 

Alphabet.__doc__ = "Une classe qui contient toutes not fonctions"  
#*Crée une documentation pour la classe Alphabet
    
    
writer.__doc__ = "Mot = Mot à écrire (sensible à la casse), gras : 0=non 1=oui,italique : 0-> non 1 -> oui, taillex : largeur de la fenêtre,tailley = longueur de la fenêtre, Taille Police -> Définit la largeur et hauteur de la police, les prochains arguments ne sont, pris en compte que si TaillePolice = 0; Policeheight = Hauteur de la police, PoliceLarge : largeur de la police, Startcenter -> fais démarrer l'écriture au milieu de l'écran, couleur -> string or Tuple, definit la couleur des lettres"
#*Crée une documentation pour la fonction 



