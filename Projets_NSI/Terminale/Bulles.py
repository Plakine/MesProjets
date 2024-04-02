# -*- coding: utf-8 -*-
"""
Projet de NSI
réalisé en une seule heure lors d'un cours
Jeu style 'agar.io'
Vous jouez la boule blanche
Votre but est d'occuper tout l'espace
vous grandissez en mangeant d'autre boules mais attention
vous serez aussi plus lent
"""

import pyxel as px
from math import pi


class Game:
    class Joueur:
        """
        Définit les méthodes et variables pour les joueurs
        """
        def __init__(self, num):
            """
            Num définit s'il s'agit du joueur 1 ou du joueur 2
            """
            self.num = num
            if num == 1:
                # Coordonées d'apparitions joueur 1
                self.xc = 100
                self.yc = 100
                # Couleur j1 (Blanc)
                self.couleur = 7
                # Taile
                self.rayon = 10
                # Vitesse
                self.dirx = 10
                self.diry = 10
            elif num == 2:
                # Coordonées d'apparitions joueur 1
                self.xc = 900
                self.yc = 900
                # Couleur j1 (Gris)
                self.couleur = 13
                # Taile
                self.rayon = 10
                # Vitesse
                self.dirx = 10
                self.diry = 10

        def min(self, p2):
            """
            Renvoie le rayon minimum entre self et p2
            """
            return self if self.rayon > p2.rayon else p2

        def bouger(self):
            """
            Mouvements des joueurs
            Flèches directionelles -> Joueur 1
            Z/Q/S/D -> Joueur 2
            """
            # J1
            if self.num == 1:
                if px.btn(px.KEY_LEFT):
                    self.xc -= self.dirx
                elif px.btn(px.KEY_RIGHT):
                    self.xc += self.dirx
                if px.btn(px.KEY_UP):
                    self.yc -= self.diry
                elif px.btn(px.KEY_DOWN):
                    self.yc += self.diry
            # J2
            elif self.num == 2:
                if px.btn(px.KEY_Q):
                    self.xc -= self.dirx
                elif px.btn(px.KEY_D):
                    self.xc += self.dirx
                if px.btn(px.KEY_Z):
                    self.yc -= self.diry
                elif px.btn(px.KEY_S):
                    self.yc += self.diry
            if self.xc > 1000:
                self.xc = 0
            # Coté gauche
            elif self.xc < 0:
                self.xc = 1000
            # Bas
            if self.yc > 1000:
                self.yc = 0
            # Haut
            elif self.yc < 0:
                self.yc = 1000

    class Bulle:
        """
        Définit les méthodes des ennemis
        """
        def __init__(self, joueur):
            # Coordonées d'apparition
            self.xc = px.rndi(15, 1000)
            self.yc = px.rndi(15, 1000)
            # On vérifie que la bulle n'apparait pas sur le joueur
            if type(joueur) is int:
                while self.xc > (joueur.xc-joueur.rayon) and\
                    self.xc < (joueur.xc+joueur.rayon) and \
                        self.yc > (joueur.yc-joueur.rayon) and\
                        self.yc < (joueur.yc+joueur.rayon):
                    self.xc = px.rndi(15, 1000)
                    self.yc = px.rndi(15, 1000)
                self.rayon = px.rndi(0, int(joueur.rayon*2))
            else:
                self.rayon = px.rndi(0, 10)
            # Vitesse
            self.dirx = float(px.rndi(-5, 5))
            self.diry = float(px.rndi(-5, 5))
            # Couleur (toutes sauf aqua, blanc gris (fond, j1, j2))
            self.couleur = [1, 2, 3, 4, 5, 0, 8, 9, 10, 11, 12, 14, 15][
                px.rndi(0, 12)]

        def bouge(self):
            """
            Méthodes de mouvement"""
            # Mouvements aléatoires
            mov2 = px.rndi(0, 15)  # décide entre mouvement avant ou arrière
            if mov2 == 0 and (px.frame_count//30) % 5 == 0:  # 5 secondes
                self.dirx = -1*self.dirx
            self.xc += self.dirx
            if mov2 == 5 and (px.frame_count//30) % 5 == 0:
                self.diry = -1*self.diry
            self.yc += self.diry
            # Si la bulle passe sur les côtés
            # coté droit
            if self.xc > 1000:
                self.xc = 0
            # Coté gauche
            elif self.xc < 0:
                self.xc = 1000
            # Bas
            if self.yc > 1000:
                self.yc = 0
            # Haut
            elif self.yc < 0:
                self.yc = 1000

    def __init__(self):
        """
        initialisation du jeu
        """
        px.init(1000, 1000)
        # Conditions de Défaite
        self.pl1haslost = False
        self.pl2haslost = False
        self.haslost = False
        self.pl1 = self.Joueur(1)
        self.pl2 = self.Joueur(2)
        # Crée les bulles
        self.Mousse = [self.Bulle(self.pl1.min(self.pl2)) for i in range(40)]
        px.run(self.update, self.draw)

    def update(self):
        # Mouvements joueur 1 et 2
        self.pl1.bouger()
        self.pl2.bouger()
        # Mouvements bullesq
        for j in range(len(self.Mousse)):
            if self.Mousse[j] is not None:
                self.Mousse[j].bouge()
        for i in range(len(self.Mousse)):
            # Collisions autre bulles
            for j in range(i, len(self.Mousse)):
                if i is not None and j is not None:
                    if self.BullesEnContact(self.Mousse[i], self.Mousse[j]):
                        if self.Mousse[i].rayon <= self.Mousse[j].rayon:
                            self.collision(i, j)
                        else:
                            self.collision(j, i)
                        self.PlaceBulle(self.Bulle(self.pl1.min(self.pl2)))
            # Collision joueur 2
            if self.BullesEnContact(self.Mousse[i], self.pl1) and\
                    not self.pl1haslost:
                if self.Mousse[i].rayon <= self.pl1.rayon:
                    surfp = pi*self.Mousse[i].rayon**2
                    surfg = pi*self.pl1.rayon**2
                    surfpost = surfp + surfg
                    rayonpost = px.sqrt(surfpost/pi)
                    self.pl1.rayon = rayonpost
                    self.pl1.dirx = self.pl1.dirx/2
                    self.pl1.diry = self.pl1.diry/2
                    self.Mousse[i] = None
                    self.PlaceBulle(self.Bulle(self.pl1.min(self.pl2)))
                else:
                    surfg = pi*self.Mousse[i].rayon**2
                    surfp = pi*self.pl1.rayon**2
                    surfpost = surfp + surfg
                    rayonpost = px.sqrt(surfpost/pi)
                    self.Mousse[i].rayon = rayonpost
                    self.Mousse[i].dirx = self.Mousse[i].dirx/2
                    self.Mousse[i].diry = self.Mousse[i].diry/2
                    self.pl1haslost = True
                    self.PlaceBulle(self.Bulle(self.pl1.min(self.pl2)))
            # Collision joueur 2
            if self.BullesEnContact(self.Mousse[i], self.pl2) and\
                    not self.pl2haslost:
                if self.Mousse[i].rayon <= self.pl2.rayon:
                    surfp = pi*self.Mousse[i].rayon**2
                    surfg = pi*self.pl2.rayon**2
                    surfpost = surfp + surfg
                    rayonpost = px.sqrt(surfpost/pi)
                    self.pl2.rayon = rayonpost
                    self.pl2.dirx = self.pl2.dirx/2
                    self.pl2.diry = self.pl2.diry/2
                    self.Mousse[i] = None
                    self.PlaceBulle(self.Bulle(self.pl1.min(self.pl2)))
                else:
                    surfg = pi*self.Mousse[i].rayon**2
                    surfp = pi*self.pl2.rayon**2
                    surfpost = surfp + surfg
                    rayonpost = px.sqrt(surfpost/pi)
                    self.Mousse[i].rayon = rayonpost
                    self.Mousse[i].dirx = self.Mousse[i].dirx/2
                    self.Mousse[i].diry = self.Mousse[i].diry/2
                    self.pl2haslost = True
                    self.PlaceBulle(self.Bulle(self.pl1.min(self.pl2)))

            # Défait si une bulle occupe tout l'écran
            if self.Mousse[i].rayon > 505:
                self.haslost = True
        # Quitte l'application
        if px.btnp(px.KEY_ESCAPE):
            px.quit()

    def draw(self):
        px.cls(6)

        if self.haslost is False:
            # On dessine toutes les boules
            for b in self.Mousse:
                if b is not None:
                    px.circ(b.xc, b.yc, b.rayon, b.couleur)
            # On dessine les joueurs
            if not self.pl1haslost:
                px.circ(self.pl1.xc, self.pl1.yc,
                        self.pl1.rayon, self.pl1.couleur)
            if not self.pl2haslost:
                px.circ(self.pl2.xc, self.pl2.yc,
                        self.pl2.rayon, self.pl2.couleur)
        else:
            px.text(50, 500, "GAME OVER", 8)

    def BullesEnContact(self, B1, B2):
        """
        Test de distance entre B1 et B2
        renvoie vrai si elles se touche
        faux sinon
        """
        if B1 is None or B2 is None:
            return
        disx = abs(B1.xc - B2.xc)
        disy = abs(B1.yc - B2.yc)
        dis = px.sqrt(disx**2 + disy**2)
        if dis < (B1.rayon + B2.rayon):
            return True
        else:
            return False

    def collision(self, ind1, ind2):
        """
        Gère la collision entre deux boules
        augmente la taille de la plus grande, et diminue sa vitesse
        supprime la plus petite
        ind1 -> petite, ind2 -> grande"""
        surfp = pi*self.Mousse[ind1].rayon**2
        surfg = pi*self.Mousse[ind2].rayon**2
        surfpost = surfp + surfg
        rayonpost = px.sqrt(surfpost/pi)
        self.Mousse[ind2].rayon = rayonpost
        self.Mousse[ind2].dirx = self.Mousse[ind2].dirx/2
        self.Mousse[ind2].diry = self.Mousse[ind2].diry/2
        self.Mousse[ind1] = None

    def PlaceBulle(self, B):
        """
        rajoute une bulle dans le jeu
        """
        i = self.donnePremierIndiceLibre()
        if i < len(self.Mousse):
            self.Mousse[i] = B

    def donnePremierIndiceLibre(self):
        "parcours les bulles pour une place libre"
        i = 0
        while i < len(self.Mousse) and self.Mousse[i] is not None:
            i += 1
        return i


Game()
