from random import randint
import turtle as trt
from math import pi


class Alphabet():

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
        trt.forward(L*(5/6))
        trt.down()
        trt.circle(0.5*H,-180)
        trt.left(180)
        trt.circle(-0.5*H,-180)
        trt.up()
        trt.left(180)
        trt.forward(L/6)

    def D(H,L,x):
        trt.left(90)
        trt.forward(H)
        trt.right(90)
        trt.circle(-0.5*H,180)
        trt.up()
        trt.right(180)
        trt.forward(L)
        
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
        trt.back(L/6)
        trt.left(90)
        trt.down()
        trt.forward(H/3)
        trt.left(90)
        trt.forward(L/3)
        trt.up()
        trt.back(L/3)
        trt.right(90)
        trt.back(H/3)
        trt.right(90)
        trt.forward(L/6)

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

    def J(H,L,x):
        trt.setheading(90)
        trt.up()
        trt.forward(H)
        trt.down()
        trt.setheading(0+x)
        trt.forward(L)
        trt.right(90)
        trt.forward(H*1.5/2)
        trt.circle(-0.3*H,180)
        trt.up()
        trt.setheading(270)
        trt.forward(H/4.1)
        trt.setheading(0)
        trt.forward(L)

    def K(H,L,x):
        trt.left(90)
        trt.forward(H)
        trt.back(H/2)
        trt.right(50.19)
        trt.forward(H*0.78)
        trt.back(H*0.78)
        trt.right(79.61)
        trt.forward(0.78*H)
        trt.left(39.81)

    def L(H,L,x):
        trt.setheading(90+x)
        trt.forward(H)
        trt.back(H)
        trt.right(90)
        trt.forward(L)

    def M(H,L,x):
        L*=2
        trt.left(75.96)
        trt.forward(1.03*H)
        trt.right(151.93)
        trt.forward(1.03*H)
        trt.left(151.93)
        trt.forward(1.03*H)
        trt.right(151.93)
        trt.forward(1.03*H)
        
    def N(H,L,x):
        trt.left(90)
        trt.forward(H)
        trt.right(149.04)
        trt.forward(1.17*H)
        trt.left(149.04)
        trt.forward(H)
        trt.back(H)
        trt.right(149.04)

    def O(H,L,x):
        trt.up()
        trt.forward(0.5*L)
        trt.down()
        trt.circle(0.5*H)
        trt.up()
        trt.forward(0.5*H)

    def P(H,L,x):
        trt.left(90)
        trt.forward(H*0.6)
        trt.right(90)
        trt.forward(L*2/3)
        trt.circle(0.2*H,180)
        trt.forward(L*2/3)
        trt.left(90)
        trt.forward(H)
        trt.left(90)
        trt.up()
        trt.forward(L)

    def Q(H,L,x):
        trt.up()
        trt.forward(0.5*L)
        trt.down()
        trt.circle(0.5*H)
        trt.up()
        trt.forward(1/2*L)
        trt.right(52.22)
        trt.down()
        trt.forward(0.1*L) #0.06*H
        trt.back(0.33*H)
        trt.forward(0.27*H)
        trt.left(52.22)
        trt.up()
        trt.forward(1/3*L)        

    def R(H,L,x):
        trt.left(90)
        trt.forward(H*0.6)
        trt.right(90)
        trt.forward(L*2/3)
        trt.circle(0.2*H,180)
        trt.forward(L*2/3)
        trt.left(90)
        trt.forward(H*0.4)
        trt.left(45)
        trt.forward(0.85*H)
        trt.left(45)
        trt.up()
        
    def S(H,L,x):
        trt.forward(0.5*L)
        trt.circle(0.25*H,180)
        trt.circle(-0.25*H,180)
        trt.forward(0.5*L)
        trt.back(0.5*L)
        trt.left(180)
        trt.circle(0.25*H,180)
        trt.circle(-0.25*H,180)
        trt.left(180)
        trt.up()
        trt.forward(0.5*L)
    
    def T(H,L,x):
        trt.up()
        trt.forward(L*0.5)
        trt.down()
        trt.left(90)
        trt.forward(H)
        trt.left(270)
        trt.forward(L/2)
        trt.back(L)
        trt.right(90)
        trt.up()
        trt.forward(H)
        trt.left(90)
        trt.forward(L)

    def U(H,L,x):
        trt.up()
        trt.left(90)
        trt.forward(H)
        trt.down()
        trt.back(H*0.7)
        trt.left(180)
        trt.circle(0.3*H,180)
        trt.forward(H*0.7)
        trt.up()
        trt.back(H)
        trt.right(90)

    def V(H,L,x):
        trt.up()
        trt.forward(L/2)
        trt.down()
        trt.left(106.7)
        trt.forward(1.04*H)
        trt.back(1.04*H)
        trt.right(33.4)
        trt.forward(1.04*H)
        trt.back(1.04*H)
        trt.right(73.3)
        trt.up()
        trt.forward(L/2)

    def W(H,L,x):
        trt.left(90)
        trt.forward(H)
        trt.back(H)
        trt.right(30.96)
        trt.forward(0.58*H)
        trt.right(118.07)
        trt.forward(H*0.58)
        trt.left(149.04)
        trt.forward(H)
        trt.back(H)
        trt.right(90)

    def X(H,L,x):
        trt.left(59.04)
        trt.forward(1.17*H)
        trt.back((1.17/2)*H)
        trt.left(61.93)
        trt.forward((1.17/2)*H)
        trt.back(1.17*H)
        trt.right(120.96)

    def Y(H,L,x):
        trt.up()
        trt.setheading(0)
        trt.forward(L/2)
        trt.down()
        trt.left(90)
        trt.forward(0.5*H)
        trt.left(30.96)
        trt.forward(0.58*H)
        trt.back(0.58*H)
        trt.right(61.92)
        trt.forward(0.58*H)
        trt.backward(0.58*H)
        trt.left(30.96)
        trt.up()
        trt.backward(0.5*H)
        trt.right(90)
        trt.forward(L/2)

    def Z(H,L,x):
        trt.up()
        trt.setheading(90+x)
        trt.forward(H)
        trt.down()
        trt.setheading(0+x)
        trt.forward(L)
        trt.right(120.96)
        trt.forward(1.17*H)
        trt.left(120.96)
        trt.forward(L)

    def Apostrophe(H,L,x):
        trt.up()
        trt.left(90)
        trt.forward(H)
        trt.forward(-5)
        trt.down()
        trt.left(30)
        trt.forward(L/5)
        trt.up()
        trt.back(L/5)
        trt.right(30)
        trt.back(H-5)
        trt.right(90)
        trt.forward(L-5)


#*Fonction Principale


def writer(
mot: str,
gras: int = 0,
souligne: int = 0,
startcenter: int = 0,
taillex: int = 1920,
tailley: int = 1080,
Taillepolice: int = 50, 
Policeheight: int = 50, 
PoliceLarge: int = 30,
couleur: str = "black",
randomcol: int = 0,
backgroundcol: str = "white" ):


    mot = mot.upper()
    #Change la couleur
    try:
        trt.color(couleur)
        if randomcol==1:
            trt.colormode(255)
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
    trt.ht()

    #Crée la surface avec les dimensions choises
    trt.screensize(taillex/1.1,tailley/1.1)
    #Plein écran
    trt.Screen().setup(1.0,1.0)
    #Couleur de l'arrière plan
    trt.bgcolor(backgroundcol)
    #Va à la première ligne
    trt.up()
    trt.goto((0-taillex/2),(0+tailley/2)-15-Taillepolice)
    #se mets en position pour écrire
    trt.setheading(90)
    trt.down()

    #Différents modes d'écritures

    #Mode Gras
    x=0
    if gras == 1:
        trt.width(5)


    #Mode Centré et souligné
    a = 0 
    Seize=[0] #On initialise la liste la ou se trouvera la première lettre
    line = 1 #On considère que il y a au moins 1 lignes
    for letter in mot:
        if letter != "M" and letter != "O"  and letter !=" " and letter !="Q": #Taille d'une lettre normale
            Seize[a] += PoliceLarge+20
        elif letter == " ": #Un espace fait 40 de large
            Seize[a] += 40
        elif letter == "O" or letter == "Q": #O et Q sont plus grand 
            Seize[a] += PoliceLarge*(4/3)+20
        elif letter =="M": # M est encore plus grand
            Seize[a] += PoliceLarge*(5/3)+20



        if Seize[a] >= trt.screensize()[0]-50: #Pour trouver s'il y a besoin d'un retour à la ligne
            line +=1 #Le programme considère une ligne de plus
            Seize.append(0) #On considère qu'on est allé à la ligne
            a+=1 
    a=1
    trt.up()
    if startcenter == 1: 
        trt.goto(-(Seize[0]/2),Policeheight+20 + Policeheight*line/2) #Zone de départ du turtle en cas de centrage
    
    #Boucles principales
    for letter in mot: #On écrit lettre par lettre
        if randomcol == 1:
                trt.color(randint(0,255),randint(0,255),randint(0,255)) #Pour mettre une couleur aléatoire
        try: #Pour éviter des crashs 

            #Récupère la fonction du nom de la lettre
            fonction  = getattr(Alphabet,letter) #Afin de récuperer la fonction nécessaire à la lettre
            trt.setheading(0) #Pour se mettre en place

            #Vérifies qu'on n'est pas à la fin de la ligne
            if ((trt.pos()[0]*2+PoliceLarge+20)) >= (taillex)-50:
                #Si on est pas centré
                if startcenter!=1:
                    trt.up()
                    if souligne == 1:
                        trt.right(90) # Se mets en position pour souligner
                        trt.forward(20)
                        trt.left(90)
                        trt.down()
                        trt.forward(-Seize[a-1]) #Avance de la longueur d'une ligne
                        a+=1 #Passe à la ligne d'après
                    trt.up()
                    trt.goto(0-taillex/2+PoliceLarge/5,trt.pos()[1]-Policeheight*2-20) #Pour se mettre en place pour la prochaine ligne

                #Si on est centré
                elif a < len(Seize): 
                    trt.up()
                    if souligne == 1:
                        trt.right(90)
                        trt.forward(20)
                        trt.left(90)
                        trt.down()
                        trt.forward(-Seize[a-1])
                    trt.up()
                    trt.goto(0-(abs(Seize[a])/2),trt.pos()[1] -Policeheight*2+20)
                    a+=1
            

            #Remets le stylo en marche au cas ou
            trt.down()
            
            #Vérifies qu'on a pas atteint la fin de l'écran
            if (trt.pos()[1]-Policeheight*2)<=-(trt.screensize()[1]/2):
                #Rajoute de la place y
                trt.screensize(taillex,trt.screensize()[1]+Policeheight)
            
            #Appelle la fonction pour dessinger la lettre
            fonction(Policeheight,PoliceLarge,x)
            
            #Se remets en place pour la prochaine lettre
            trt.setheading(0)
            trt.up()
            trt.forward(20)
        except:
            #On arrive ici si on essaye d'utiliser un caractère qui n'existe pas donc Cas Spéciaux
            #Espaces
            if letter == " ":
                trt.up()
                trt.right(-(trt.heading()))
                trt.forward(40)
            if letter == "'":
                trt.forward(-5)
                Alphabet.Apostrophe(Policeheight,PoliceLarge,x)

    #Souligne la dernière ligne
    if souligne == 1:
        trt.right(90)
        trt.forward(20)
        trt.left(90)
        trt.down()
        trt.forward(-Seize[a-1])
    #Permet de fermer la fenêtre de turtle à la fin du programme    
    trt.exitonclick()     
    
   
#! Exemple d'utilisation
#* writer("Vos mots, je crois qu'on appelle ca une phrase d'ailleurs",gras=1,souligne=1,startcenter=1,Taillepolice=60)

Alphabet.__doc__ = "Une classe qui contient toutes nos fonctions"  
    
writer.__doc__ = "Mot = Mot à écrire (sensible à la casse) ; gras : 0=non 1=oui ; souligné: 0 -> non, 1 -> oui ; startcenter : 0 -> non 1 -> oui ; taillex : largeur de la fenêtre ; tailley = longueur de la fenêtre ; Taille Police -> Définit la largeur et hauteur de la police ; les prochains arguments ne sont  pris en compte que si TaillePolice = 0: Policeheight = Hauteur de la police; PoliceLarge : largeur de la police, couleur -> string or Tuple, definit la couleur des lettres ; randomcol : utilise une couleur différente pour chaque lettre (0 -> non, 1 -> oui) ; backgroundcolor : définit la couleur de l'arrière plan"
