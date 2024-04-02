# Nuit du c0de 2023
"""
Hector Leo Julien
"""
import pyxel as px
from player import Player as p
from mob import Mob as m
from nourriture import nourriture as b
from Salle import Room as s


class Game:
    def __init__(self):
        self.pl = p()
        px.init(128, 128, title="NDC 2023")
        px.load("5.pyxres")
        # Liste des ennemis présents
        self.mobs = []
        # Carte du jeu
        self.carte = [
            [s(0, 0, [0, 0, 0, 1], 2),
             s(0, 1, [px.rndi(0, 2) for i in range(4)], mob=px.rndi(0, 2)),
             s(0, 1, [px.rndi(0, 2) for i in range(4)], mob=px.rndi(0, 2))
             ],
            [s(1, 0, [1, 2, 1, 0], nourr=b(25, 35, 35, 45, 6)),
                s(1, 1, [1, 0, 1, 0], mob=3),
                s(1, 1, [1, 0, 1, 0], mob=3)],
        ]
        # Fonction pause
        self.paused = False
        # Game over
        self.fin = False
        px.run(self.update, self.draw)

    def draw(self):
        px.cls(0)
        # Game Over : lose
        if self.pl.vies <= 0:
            px.text(50, 50, "You Lose", 7)
            return 1
        # Mur du Hauut
        px.blt(2, 15, 0, 10, 10, 8, 8)
        for i in range(1, 16):
            px.blt(2+8*i, 15, 0, 10, 10, 8, 8)
        px.blt(0, 15, 0, 0, 16, 2, 8)
        for i in range(1, 15):
            px.blt(0, 10+8*i, 0, 0, 16, 2, 8)
        px.blt(2, 119, 0, 10, 10, 8, 8)
        for i in range(1, 16):
            px.blt(2+8*i, 119, 0, 10, 10, 8, 8)
        px.blt(126, 15, 0, 0, 16, 2, 8)
        for i in range(1, 15):
            px.blt(126, 10+8*i, 0, 0, 16, 2, 8)
        # * Portes
        # Dessin de la salle1
        if self.room.portes[0] == 1:
            px.rect(125, 60, 3, 10, 0)
        elif self.room.portes[0] == 2:
            # TODO Afficher correctement la porte
            px.blt(125, 60, 0, 71, 13, 8, 6)
        if self.room.portes[1] == 1:
            px.rect(60, 17, 8, 8, 0)
        elif self.room.portes[1] == 2:
            px.blt(60, 17, 0, 71, 13, 8, 6)
        if self.room.portes[2] == 1:
            px.rect(0, 60, 3, 10, 0)
        elif self.room.portes[2] == 2:
            px.blt(0, 60, 0, 71, 13, 8, 6)
        if self.room.portes[3] == 1:
            px.rect(60, 119, 8, 8, 0)
        elif self.room.portes[3] == 2:
            px.blt(60, 119, 0, 71, 19, 9, -7, 5)
        if self.room.nourriture is not None:
            px.blt(self.room.nourriture.coos[0],
                   self.room.nourriture.coos[2],
                   0, 131, 40, 7, 10, 5)
        if self.room.coffre == 2:
            px.blt(60, 60, 0, 31, 102, 8, 8, 5)
        elif self.room.coffre == 1:
            px.blt(60, 61, 0, 41, 103, 8, 7, 5)

        # Affichage du joueur
        px.blt(self.pl.x, self.pl.y, 0,
               self.pl.sprite[0], self.pl.sprite[1],
               self.pl.sprite[2], self.pl.sprite[3], 5)
        # * UHD
        # Vies
        if self.pl.vies >= 2:
            px.blt(0, 3, 0, 140, 11, 10, 9, 5)
            if self.pl.vies >= 4:
                px.blt(11, 3, 0, 140, 11, 10, 9, 5)
                if self.pl.vies == 6:
                    px.blt(22, 3, 0, 140, 11, 10, 9, 5)
                elif self.pl.vies == 5:
                    px.blt(22, 3, 0, 150, 11, 10, 9, 5)
            elif self.pl.vies == 3:
                px.blt(11, 3, 0, 150, 11, 10, 9, 5)
        elif self.pl.vies == 1:
            px.blt(0, 3, 0, 150, 11, 10, 9, 5)
        # Energie
        if self.pl.endurance >= 2:
            px.blt(50, 2, 0, 141, 20, 10, 10, 5)
            if self.pl.endurance >= 4:
                px.blt(60, 2, 0, 141, 20, 10, 10, 5)
                if self.pl.endurance == 6:
                    px.blt(70, 2, 0, 141, 20, 10, 10, 5)
                elif self.pl.endurance == 5:
                    px.blt(70, 2, 0, 151, 20, 10, 10, 5)
            elif self.pl.endurance == 3:
                px.blt(60, 2, 0, 151, 20, 10, 10, 5)
        elif self.pl.endurance == 1:
            px.blt(50, 2, 0, 151, 20, 10, 10, 5)

        # Bouffe
        if self.pl.nourriture >= 2:
            px.blt(99, 3, 0, 141, 31, 8, 8, 5)
            if self.pl.nourriture >= 4:
                px.blt(107, 3, 0, 141, 31, 8, 8, 5)
                if self.pl.nourriture == 6:
                    px.blt(115, 3, 0, 141, 31, 8, 8, 5)
                elif self.pl.nourriture == 5:
                    px.blt(115, 3, 0, 151, 31, 8, 8, 5)
            elif self.pl.nourriture == 3:
                px.blt(107, 3, 0, 151, 31, 8, 8, 5)
        elif self.pl.nourriture == 1:
            px.blt(99, 3, 0, 151, 31, 8, 8, 5)

        # Affichage projectiles
        for proj in self.pl.projectiles:
            px.blt(proj[0], proj[1], 0, 82, 107, 6, 3, 5)
        # Affichages mob
        if self.room.mob > 0 and len(self.mobs) != 0:
            for thismob in self.mobs:
                px.blt(thismob.x, thismob.y, 0, thismob.sprite[0],
                       thismob.sprite[1], thismob.sprite[2],
                       thismob.sprite[3], 5)
        # Game over : win
        if self.fin:
            px.rect(0, 0, 128, 128, 0)
            px.text(50, 50, "You win", 7)
        # Key got gotten
        if self.paused:
            # * Cadre
            px.rect(10, 10, 108, 108, 0)
            px.rectb(9, 9, 109, 109, 7)
            px.text(45, 15, "Inventaire", 7)
            px.tri(62, 110, 66, 110, 64, 113, 7)
            px.trib(61, 109, 67, 109, 64, 114, 9)
            # * Item : clé
            px.blt(20, 25, 0, 63, 103, 3, 6, 5)
            px.text(28, 25, "Cles : " + str(self.pl.sac["key"]), 7)
            # * item : Arme de lancer
            px.blt(19, 35, 0, 82, 107, 6, 3, 5)
            px.text(28, 34, "Batarang :" + str(self.pl.sac["proj"]), 7)

    def update(self):
        self.room = self.carte[self.pl.tableaui][self.pl.tableauj]
        if px.btnp(px.KEY_I):
            self.paused = not self.paused
        if self.paused:
            return 0

        # Récuperer la clé
        if self.room.mob > 0 and len(self.mobs) == 0:
            if self.room.coffre == -1:
                self.room.coffre = 0
            elif self.room.bf == 1:
                self.room.portes = self.room.save
            self.pl.sac["key"] += 1
            self.room.mob = 0
        # Mouvements joueur + projectiles
        self.pl.move()
        # Régeneration de vie
        if px.frame_count % 600 == 0:
            self.pl.regen()
        # Lancement de projectiles
        self.pl.attack()
        if self.pl.cooldown > 0:
            self.pl.cooldown -= 1
        # Mouvements des mobs
        for enn in self.mobs:
            enn.move(self.pl, self.mobs, px.frame_count)
            if enn.x <= self.pl.x and enn.x+8 >= self.pl.x and\
                    enn.y <= self.pl.y and enn.y+8 >= self.pl.y:
                if self.pl.cooldown == 0:
                    self.pl.cooldown = 15
                    self.pl.vies -= enn.deg
            for tir in self.pl.projectiles:
                if tir[0] <= enn.x and tir[0]+8 >= enn.x and\
                     tir[1] <= enn.y and tir[1]+8 >= enn.y:
                    self.pl.projectiles.remove(tir)
                    self.mobs.remove(enn)
                    self.pl.sac["proj"] += 15
        # Check des nourritures

        if self.room.nourriture is not None:
            if self.pl.x >= self.room.nourriture.coos[0] and\
               self.pl.x <= self.room.nourriture.coos[1] and\
               self.pl.y >= self.room.nourriture.coos[2] and\
               self.pl.y <= self.room.nourriture.coos[3] and\
               self.pl.nourriture < 6:
                if self.pl.nourriture + self.room.nourriture.regen <= 6:
                    self.pl.nourriture += self.room.nourriture.regen
                else:
                    self.pl.nourriture = 6
                self.room.nourriture = None
        '''
        mouvements d'une salle à l'autre
        '''
        # ! 1
        # Mouvement vers la gauche
        if self.pl.y >= 55 and self.pl.y <= 65 and\
            self.pl.x >= 0 and self.pl.x <= 5 and\
                self.room.portes[2] == 1:
            self.pl.tableauj -= 1
            # Génération automatique des salles
            if self.pl.tableauj < 0:
                self.pl.tableauj = 0
                for i in range(len(self.carte)):
                    doors = []  # droite
                    doors.append(self.carte[i][0].portes[2])
                    if i > 0:  # haut
                        doors.append(self.carte[i-1]
                                     [0].portes[3])
                    else:
                        doors.append(px.rndi(0, 2))
                    doors.append(px.rndi(0, 2))  # gauche
                    doors.append(px.rndi(0, 2))  # bas
                    self.carte[i] = [s(i,
                                     self.pl.tableauj, doors)] + \
                        self.carte[i]
            self.room = self.carte[self.pl.tableaui][self.pl.tableauj]
            self.pl.x = 100
            self.pl.y = 60
            # Reset des mobs
            self.mobs = []
            # Spawn des monstres
            for i in range(self.room.mob):
                self.mobs.append(m(px.rndi(1, 2), self.pl.x, self.pl.y))
        # ! 2
        # Mouvement vers la droite
        if self.pl.x <= 128 and self.pl.x >= 120 and\
            self.pl.y >= 55 and self.pl.y <= 65 and\
                self.room.portes[0] == 1:
            self.pl.tableauj += 1
            if self.pl.tableauj == len(self.carte[self.pl.tableaui]):
                # Génération automatique des portes
                for i in range(len(self.carte)):
                    doors = [px.rndi(0, 2)]  # droite
                    if i > 0:  # haut
                        doors.append(self.carte[i-1]
                                     [self.pl.tableauj].portes[3])
                    else:
                        doors.append(px.rndi(0, 2))
                    doors.append(self.carte[i][self.pl.tableauj-1].portes[0])
                    doors.append(px.rndi(0, 2))  # bas
                    self.carte[i] = self.carte[i] +\
                        [s(i, self.pl.tableauj+1,
                            doors, mob=px.rndi(0, 2))]
            self.room = self.carte[self.pl.tableaui][self.pl.tableauj]
            self.pl.x = 30
            self.mobs = []
            # Spawn des monstres
            for i in range(self.room.mob):
                self.mobs.append(m(px.rndi(1, 2), self.pl.x, self.pl.y))
        # ! 3
        # Mouvement vers le haut
        if self.pl.x <= 65 and self.pl.x >= 55 and\
            self.pl.y <= 30 and\
                self.room.portes[1] == 1:
            self.pl.tableaui -= 1
            if self.pl.tableaui < 0:
                self.pl.tableaui = 0
                for j in range(len(self.carte[0])):
                    doors = []
                    # droite
                    if j == 0:
                        doors.append(px.rndi(0, 2))
                    else:
                        doors.append(self.carte[0][j-1].portes[0])
                    # Haut
                    doors.append(px.rndi(0, 2))
                    # Gauche
                    doors.append(px.rndi(0, 2))
                    # Bas
                    if j == 0:
                        doors.append(self.carte[0][j].portes[3])
                    else:
                        doors.append(self.carte[1][j].portes[3])
                    if j == 0:
                        self.carte = [[]] + self.carte
                    self.carte[0].append(s(0, j, doors, mob=px.rndi(0, 2)))
            self.room = self.carte[self.pl.tableaui][self.pl.tableauj]
            self.pl.y = 100
            for i in range(self.room.mob):
                self.mobs.append(m(px.rndi(1, 2), self.pl.x, self.pl.y))
        # ! 4
        # Mouvement vers le bas
        if self.pl.x <= 65 and self.pl.x >= 55 and\
                self.pl.y >= 105 and self.room.portes[3] == 1:
            self.pl.tableaui += 1
            if self.pl.tableaui == len(self.carte):
                for j in range(len(self.carte[self.pl.tableaui-1])):
                    doors = [px.rndi(0, 2)]
                    doors.append(self.carte[self.pl.tableaui-1][j].portes[3])
                    if j > 0:
                        doors.append(self.carte[self.pl.tableaui][j-1].portes[0])
                    else:
                        doors.append(px.rndi(0, 2))
                    doors.append(px.rndi(0, 2))
                    if j == 0:
                        self.carte = self.carte + [[]]
                    r = s(self.pl.tableaui, j, doors, mob=px.rndi(0, 2))
                    self.carte[self.pl.tableaui].append(r)
            self.room = self.carte[self.pl.tableaui][self.pl.tableauj]
            self.pl.y = 35
            self.mobs = []
            for i in range(self.room.mob):
                self.mobs.append(m(px.rndi(1, 2), self.pl.x, self.pl.y))
        '''
        Ouverture de portes fermées à clés
        '''
        # Mouvement vers la gauche
        if self.pl.y >= 55 and self.pl.y <= 65 and\
            self.pl.x >= 0 and self.pl.x <= 5 and\
                self.room.portes[2] == 2 and\
                px.btn(px.KEY_E) and self.pl.sac['key'] > 0:
            self.room.portes[2] = 1
            if self.pl.tableauj > 0:
                self.carte[self.pl.tableaui][self.pl.tableauj-1].portes[0] = 1
            self.pl.sac['key'] -= 1
        # Mouvement vers la droite
        if self.pl.x <= 128 and self.pl.x >= 120 and\
            self.pl.y >= 55 and self.pl.y <= 65 and\
                self.room.portes[0] == 2 and\
                px.btn(px.KEY_E) and self.pl.sac['key'] > 0:
            self.room.portes[0] = 1
            if self.pl.tableauj < len(self.carte[self.pl.tableaui])-1:
                self.carte[self.pl.tableaui][self.pl.tableauj+1].portes[2] = 1
            self.pl.sac['key'] -= 1
        # Mouvement vers le haut
        if self.pl.x <= 75 and self.pl.x >= 35 and\
            self.pl.y >= 0 and self.pl.y <= 35 and\
                self.room.portes[1] == 2 and\
                px.btn(px.KEY_E) and self.pl.sac['key'] > 0:
            self.room.portes[1] = 1
            if self.pl.tableaui > 0:
                self.carte[self.pl.tableaui-1][self.pl.tableauj].portes[3] = 1
            self.pl.sac['key'] -= 1
        # Mouvement vers le bas
        if self.pl.x <= 65 and self.pl.x >= 55 and\
                self.pl.y >= 105 and self.room.portes[3] == 2 and\
                px.btn(px.KEY_E) and self.pl.sac['key'] > 0:
            self.room.portes[3] = 1
            if self.pl.tableaui+1 < len(self.carte[self.pl.tableaui]):
                self.carte[self.pl.tableaui+1][self.pl.tableauj].portes[1] = 1
            self.pl.sac['key'] -= 1

        """
        Interaction objets
        """
        # Utilisation coffre
        if px.btnp(px.KEY_E) and self.pl.x >= 50 and\
            self.pl.x <= 65 and self.pl.y <= 65 and\
                self.pl.y >= 55 and self.room.coffre == 1:
            if self.room.ccont[0] == "fin":
                self.fin = True
            else:
                self.pl.sac[self.room.ccont[0]] += self.room.ccont[1]
        # Ouverture coffre
        if px.btn(px.KEY_E) and self.pl.x >= 50 and\
            self.pl.x <= 65 and self.pl.y <= 65 and\
                self.pl.y >= 55 and self.room.coffre == 2 and\
                self.pl.sac['key'] >= 1:
            self.pl.sac['key'] -= 1
            self.room.coffre = 1


Game()
