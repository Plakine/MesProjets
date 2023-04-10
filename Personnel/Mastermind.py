"""
Jeu du MasterMind.
Jeudi 9 Juin 2022 à 10:26:38
"""

from pygame import *
from pygame import event as ev
from random import randint


def start():
    global info, screen_width, screen_height, game, window, csr, x, y,cl,col,col1,col2,col3,col4,colist,coldict,chosenlist,trynum,a,b,c,d

    #réinitialisation de variables
    cl = 1
    # Définition des couleurs à deviner de gauche à droite
    col1 = randint(1, 8)
    col2 = randint(1, 8)
    col3 = randint(1, 8)
    col4 = randint(1, 8)
    colist = [col1,col2,col3,col4]
    # dictionnaire des couleurs
    coldict = {
            1:"white", 
            2:"red", 
            3:"pink", 
            4:"yellow", 
            5:"orange", 
            6:(192, 192, 192), 
            7:"blue", 
            8:"purple"
            }
    #Couleurs préselectionnées 
    col = "red"
    a="None"
    b="None"
    c="None"
    d="None"
    chosenlist = [a,b,c,d]
    trynum = 1
    #on initialise les modules
    display.init()
    font.init()

    #on récupère la taille de l'écran
    info = display.Info() 
    screen_width, screen_height = info.current_w, info.current_h
    #on crée la fenetre
    window = display.set_mode((screen_width, screen_height), display = 0)
    display.set_caption("MasterMind")

    #on crée la surface de jeu
    game = Surface((window.get_width(), window.get_height()))
    x, y = window.get_size()
    draw.rect(game, (0, 0, 0), (0, 0, x, y), width = 0)

    # On actualise l'écran
    window.blit(game, (0, 0))
    display.flip()

    csr = 1 # variable qui sauvegarde sur quel écran est le joueur (1 = écran d'acceuil)


def screen(menu):
    global info, window, screen_width, screen_height, game, pos2

    #création de l'écran d'accueil
    if menu == 1: 

        #Ecriture MasterMind
        mmfont = font.SysFont(None, 150)
        text = mmfont.render("Master MIND", True, (255, 0, 0))
        game.blit(text, ((screen_width/2)-308, (screen_height/4)-52))
        display.flip()
       
        #Bouton Play
        Options_font = font.SysFont(None, 75)
        draw.rect(game, "white", (screen_width/2-70, screen_height/4*3, 140, 55))
        text = Options_font.render("Play", True, (0, 255, 0))
        game.blit(text, ((screen_width/2)-58, (screen_height/4)*3))
        window.blit(game, (0, 0))
        display.flip()
        pos2 = text.get_rect()


def launch():
    global x, y, coldict, Rects,csr,destin,a,b,c,d, polyrect
    Rects = []
    #On efface l'écran
    draw.rect(game, (0, 0, 0), (0, 0, x, y), width = 0)
    
    #carré du menu des couleurs
    draw.rect(game, "white", (screen_width/8*6, screen_height/4*3.7, screen_height, screen_width), width = 1)
    
    #création des cercles de couleurs
    for e in range(1, 9):
        draw.circle(game, coldict.get(e), (screen_width/8*6+55*e, screen_height/4*3.8), 20)
        #définit une liste hitbox pour les cercles (utilisée plus bas)
        Rects.append((screen_width/8*6-20+55*e, screen_height/4*3.8-20,40,40))  
    #Boitier de sélection
    draw.rect(game, "white", (screen_width/6, screen_height/10*8.7, 500, 100), width = 1)
    draw.circle(game,"white",(screen_width/6+500/5,screen_height/10*8.7+50),30,width=1)
    draw.circle(game,"white",(screen_width/6+500/5*2,screen_height/10*8.7+50),30,width=1)
    draw.circle(game,"white",(screen_width/6+500/5*3,screen_height/10*8.7+50),30,width=1)
    draw.circle(game,"white",(screen_width/6+500/5*4,screen_height/10*8.7+50),30,width=1)

    #Hitbox du boitier d'essai
    destin = [
              (screen_width/6+500/5-30,screen_height/10*8.7+20,60,60),
              (screen_width/6+500/5*2-30,screen_height/10*8.7+20,60,60),
              (screen_width/6+500/5*3-30,screen_height/10*8.7+20,60,60),
              (screen_width/6+500/5*4-30,screen_height/10*8.7+20,60,60),
              ]
    
    #Bouton Entrée

        #Création de la flèche
    draw.polygon(game, 'white',[
                (screen_width/6*2.6,screen_height/10*8.7+50),
                (screen_width/6*2.6+50,screen_height/10*8.7+50),
                (screen_width/6*2.6+50,screen_height/10*8.7+30),
                (screen_width/6*2.6+75,screen_height/10*8.7+60),
                (screen_width/6*2.6+50,screen_height/10*8.7+90),
                (screen_width/6*2.6+50,screen_height/10*8.7+70),
                (screen_width/6*2.6,screen_height/10*8.7+70)
                ])

    polyrect = (screen_width/6*2.6,screen_height/10*8.7,75,90)

        #Texte "Entrée"
    Spl = font.SysFont(None,30)
    etr = Spl.render("Entrée", True, "black")
    game.blit(etr,(screen_width/6*2.6+5,screen_height/10*9.1+5))

    #Affichage des essais
    for i in range(10):
        #Police
        Number = font.SysFont(None,25)
        Num = Number.render(str(i),True,"White")

        #Rangée 1
        if i <=5 and i!=0:
            draw.rect(game, "white", (screen_width/6-100, screen_height/10*8.7-i*190, 500, 100), width = 1)
            draw.circle(game,"white",(screen_width/6-100+500/5,screen_height/10*8.7+50-i*190),30,width=1)
            draw.circle(game,"white",(screen_width/6-100+500/5*2,screen_height/10*8.7+50-i*190),30,width=1)
            draw.circle(game,"white",(screen_width/6-100+500/5*3,screen_height/10*8.7+50-i*190),30,width=1)
            draw.circle(game,"white",(screen_width/6-100+500/5*4,screen_height/10*8.7+50-i*190),30,width=1)
            game.blit(Num,(screen_width/6-80,screen_height/10*8.7-i*190+10))

        #Rangée 2   
        if i >5:
            draw.rect(game, "white", (screen_width/6*4.5-100, screen_height/10*8.7-(i-4)*190, 500, 100), width = 1)
            draw.circle(game,"white",(screen_width/6*4.5-100+500/5,screen_height/10*8.7+50-(i-4)*190),30,width=1)
            draw.circle(game,"white",(screen_width/6*4.5-100+500/5*2,screen_height/10*8.7+50-(i-4)*190),30,width=1)
            draw.circle(game,"white",(screen_width/6*4.5-100+500/5*3,screen_height/10*8.7+50-(i-4)*190),30,width=1)
            draw.circle(game,"white",(screen_width/6*4.5-100+500/5*4,screen_height/10*8.7+50-(i-4)*190),30,width=1)
            game.blit(Num,(screen_width/6*4.25,screen_height/10*8.7-(i-4)*190+10))
   #affichage du menu
    window.blit(game,(0,0))
    display.flip()
    csr=2


# Reset the Color selector
def clearout():
    global chosenlist
    #Turns it black
    draw.circle(game,"black",(screen_width/6+500/5,screen_height/10*8.7+50),30,width=0)
    draw.circle(game,"black",(screen_width/6+500/5*2,screen_height/10*8.7+50),30,width=0)
    draw.circle(game,"black",(screen_width/6+500/5*3,screen_height/10*8.7+50),30,width=0)
    draw.circle(game,"black",(screen_width/6+500/5*4,screen_height/10*8.7+50),30,width=0)   
    #Outlines the circle again
    draw.circle(game,"white",(screen_width/6+500/5,screen_height/10*8.7+50),30,width=1)
    draw.circle(game,"white",(screen_width/6+500/5*2,screen_height/10*8.7+50),30,width=1)
    draw.circle(game,"white",(screen_width/6+500/5*3,screen_height/10*8.7+50),30,width=1)
    draw.circle(game,"white",(screen_width/6+500/5*4,screen_height/10*8.7+50),30,width=1)
    chosenlist = ["None","None","None","None"]


def checking():
    global trynum
    p = 0
    n = 0
    v = 0
    #Convertis la selection en int 
    for b in chosenlist:
        rep = list(coldict.keys())[list(coldict.values()).index(b)]
        chosenlist[chosenlist.index(b)] = rep

    colist2 = colist
    chosenlist2 = chosenlist
    #Vérifie les parfaits
    for i in range(4):
        if chosenlist[i-v] == colist[i-v]:
            p += 1 
            chosenlist2.pop(i-v)
            colist2.pop(i-v)
            v+=1
    #vérifie les couleurs malplacés
    for i in range(len(chosenlist2)):
        if chosenlist2[i] in colist2:
            n += 1 
            colist2.pop(colist2.index(chosenlist2[i]))

    #Affichage des indices colonnede droite
    score = font.SysFont(None,25)
    if trynum-1 <=5:
        num = score.render("Misplaced",True,"White")
        game.blit(num,(screen_width/6-120-500/6,screen_height/10*8.7-(trynum-1)*190))
        num = score.render(str(n),True,"White")
        game.blit(num,(screen_width/6-80-500/6,screen_height/10*8.7+20-(trynum-1)*190))
        num = score.render("Perfects",True,"White")
        game.blit(num,(screen_width/6+420,screen_height/10*8.7-(trynum-1)*190))
        num = score.render(str(p),True,"White")
        game.blit(num,(screen_width/6+440,screen_height/10*8.7+20-(trynum-1)*190))

    #Affichage des indices colonne de gauche
    elif trynum-1 >5 :
        num = score.render("Misplaced",True,"White")
        game.blit(num,(screen_width/6*4.5-300+500/5,screen_height/10*8.7-(trynum-5)*190))
        num = score.render(str(n),True,"White")
        game.blit(num,(screen_width/6*4.5-280+500/5,screen_height/10*8.7+20-(trynum-5)*190))
        num = score.render("Perfects",True,"White")
        game.blit(num,(screen_width/6*4.5+405,screen_height/10*8.7-(trynum-5)*190))
        num = score.render(str(p),True,"White")
        game.blit(num,(screen_width/6*4.5+405,screen_height/10*8.7+20-(trynum-5)*190))


    # Victoire
    if p == 4 :
        draw.rect(game, (0, 0, 0), (0, 0, x, y), width = 0)
        winfont = font.SysFont(None, 150)
        text = winfont.render("Victoire", True, (255, 0, 0))
        game.blit(text, ((screen_width/2)-200, (screen_height/2)-50))
        display.flip()
        return 0
    else:
        return 1


start()
screen(1)  # 1 - > afficher le menu de titre

# action à effectuer tout le temps
while 1:

    # Event listener (detecte lorsque qu'on clique sur quelque chose
    # (clavier, souris...))
    for event in ev.get():

            # si un touche à été pressé
            if event.type == KEYDOWN :
                # si c'est escape on quitte le jeu
                if (event.key == K_ESCAPE):
                    display.quit()
                    quit()
                # On choisis la couleur à l'aide du clavier
                if event.key == K_1:
                    col = coldict.get(1)
                elif event.key == K_2:
                    col = coldict.get(2)
                elif event.key == K_3:
                    col = coldict.get(3)                    
                elif event.key == K_4:
                    col = coldict.get(4)
                elif event.key == K_5:
                    col = coldict.get(5)
                elif event.key == K_6:
                    col = coldict.get(6)
                elif event.key == K_7:
                    col = coldict.get(7)
                elif event.key == K_8:
                    col = coldict.get(8)
                #On redémmare le jeu, si l'écran de defaite est affiché et la touche entrée est pressé
                if csr == 3 and event.key == K_RETURN:
                    start()
                    screen(1)

            #Si la souris à été préssé
            if event.type == MOUSEBUTTONDOWN:
                #on récupére la position de la souris
                pos = mouse.get_pos()

                #Si on se trouve sur le menu titre
                if csr == 1:
                    #Les donnes Rect du boutton "Play" (défini dans screen(1))
                    pos2 = (screen_width/2-70, screen_height/4*3, 140, 55)
                    #détecter si la souris est sur le bouton
                    for f in range(int(pos2[0]), int(pos2[0]+pos2[2])): #Pos2[0] - > Position horizontale du haut gauche du bouton, pos2[0]+pos2[2] - > même mais haut à droite; int() pour régler une erreur de Type
                        for g in range(int(pos2[1]), int(pos2[1]+pos2[3])): #Pos2[1] - >  Position verticale du haut droit du bouton, pos2[1]+pos2[3] - > même mais bas à gauche.
                            if pos == (f, g):
                                csr = 2 #on passe au deuxième menu
                                launch() #Affichage de l'interface de jeu
                if csr == 2: 
                    #Selecteur de couleur (même fonctionnement qu'au dessus ! )
                    lazy = 1
                    for pos2 in Rects:
                        for f in range(int(pos2[0]), int(pos2[0]+pos2[2])): #Pos2[0] - > Position horizontale du haut gauche du bouton, pos2[0]+pos2[2] - > même mais haut à droite; int() pour régler une erreur de Type
                            for g in range(int(pos2[1]), int(pos2[1]+pos2[3])): #Pos2[1] - >  Position verticale du haut droit du bouton, pos2[1]+pos2[3] - > même mais bas à gauche.
                                if pos == (f, g):
                                    col = coldict.get(lazy)
                        lazy+=1        
                    
                    #*Appliquer la couleur (même fonctionnement qu'au dessus ! )
                    lazy2=0
                    for pos2 in destin:
                        for f in range(int(pos2[0]), int(pos2[0]+pos2[2])): #Pos2[0] - > Position horizontale du haut gauche du bouton, pos2[0]+pos2[2] - > même mais haut à droite; int() pour régler une erreur de Type
                            for g in range(int(pos2[1]), int(pos2[1]+pos2[3])): #Pos2[1] - >  Position verticale du haut droit du bouton, pos2[1]+pos2[3] - > même mais bas à gauche.
                                if pos == (f, g):
                                    #On affiche la couleur sélectionné sur le rond sélectionné

                                    for i in range(4):
                                        draw.circle(game,col,(destin[lazy2][0]+30,destin[lazy2][1]+30),i*10)
                                        window.blit(game,(0,0))
                                        display.flip()
                                        if lazy2 == 0:
                                            a = col
                                        elif lazy2 ==1:
                                            b = col
                                        elif lazy2 == 2:
                                            c = col
                                        else : 
                                            d = col
                                        chosenlist = [a,b,c,d]
                        
                        for f in range(int(polyrect[0]), int(polyrect[0]+polyrect[2])): #Pos2[0] - > Position horizontale du haut gauche du bouton, pos2[0]+pos2[2] - > même mais haut à droite; int() pour régler une erreur de Type
                            for g in range(int(polyrect[1]), int(polyrect[1]+polyrect[3])): #Pos2[1] - >  Position verticale du haut droit du bouton, pos2[1]+pos2[3] - > même mais bas à gauche.
                                if pos == (f, g):
                                    
                                    if "None" in chosenlist: #On vérifie que chaque rond a une couleur
                                        break
                                    else: 
                                    #*Affichage des essais précédents 

                                        #Rangée 1
                                        if trynum <=5:
                                            draw.circle(game,a,(screen_width/6-100+500/5,screen_height/10*8.7+50-trynum*190),30,width=0)
                                            draw.circle(game,b,(screen_width/6-100+500/5*2,screen_height/10*8.7+50-trynum*190),30)
                                            draw.circle(game,c,(screen_width/6-100+500/5*3,screen_height/10*8.7+50-trynum*190),30)
                                            draw.circle(game,d,(screen_width/6-100+500/5*4,screen_height/10*8.7+50-trynum*190),30)
                                            


                                        #Rangée 2   
                                        if trynum >5:
                                            draw.circle(game,a,(screen_width/6*4.5-100+500/5,screen_height/10*8.7+50-(trynum-4)*190),30)
                                            draw.circle(game,b,(screen_width/6*4.5-100+500/5*2,screen_height/10*8.7+50-(trynum-4)*190),30)
                                            draw.circle(game,c,(screen_width/6*4.5-100+500/5*3,screen_height/10*8.7+50-(trynum-4)*190),30)
                                            draw.circle(game,d,(screen_width/6*4.5-100+500/5*4,screen_height/10*8.7+50-(trynum-4)*190),30)
                                            if trynum == 10:
                                                draw.rect(game, (0, 0, 0), (0, 0, x, y), width = 0)
                                                losefont = font.SysFont(None, 150)
                                                text = losefont.render("Defaite", True, (255, 0, 0))
                                                game.blit(text, ((screen_width/2)-200, (screen_height/2)-50))
                                                display.flip()
                                                #flag to stop the clearout from happening
                                                cl = 0

                                        trynum+=1
                                        colist = [col1,col2,col3,col4]

                                        
                                        if checking() == 1 and cl == 1:
                                            clearout()
                                        else:
                                            csr= 3
                                            chosenlist = ["None","None","None","None"]
  
                                        
                                        #Actualisation de l'écran
                                        window.blit(game,(0,0))
                                        display.flip()
                        lazy2+=1

