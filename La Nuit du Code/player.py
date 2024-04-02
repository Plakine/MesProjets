import pyxel


class Player:
    def __init__(self):
        # Les coordonées
        self.x = 25
        self.y = 64
        # Les valeurs de l'uhd
        self.vies = 6
        self.nourriture = 6
        self.endurance = 6
        # Dupliquée des variables salles 1,2,3
        self.tableaui = 1
        self.tableauj = 0
        self.sac = {"key": 0, "proj": 30}
        # Les tirs du personnages
        self.projectiles = []
        # Les coordonées des images
        # Normal
        self.sprite1 = [122, 12, 6, 8]
        # Inversé
        self.sprite2 = [132, 12, -6, 8]
        # Sprite utilisé actuellement
        self.sprite = self.sprite1
        self.cooldown = 15

    def move(self):
        # Reste du mode deux joueurs
        # Vitesse de base
        move = 2.5
        # Sprint
        if pyxel.btn(pyxel.KEY_SHIFT) and self.endurance > 0.5 and (
            pyxel.btn(pyxel.KEY_Z)
            or pyxel.btn(pyxel.KEY_S)
            or pyxel.btn(pyxel.KEY_Q)
            or pyxel.btn(pyxel.KEY_D)
                ):
            move = 5
            if pyxel.frame_count % 10 == 0:
                self.endurance -= 1
        # Récupération du sprint
        elif not pyxel.btn(pyxel.KEY_SHIFT) and self.endurance < 6 and\
                pyxel.frame_count % 120 == 0 and self.nourriture > 0:
            self.endurance += 1
            self.nourriture -= 1
        # Mouvements
        moved = False
        while move > 0 and moved is False:
            if pyxel.btn(pyxel.KEY_Z) and self.y-move >= 23:
                self.y -= move
                moved = True
            elif pyxel.btn(pyxel.KEY_S) and self.y+move <= 111:
                self.y += move
                moved = True
            if pyxel.btn(pyxel.KEY_Q) and self.x-move >= 2:
                self.x -= move
                self.sprite = self.sprite2
                moved = True
            elif pyxel.btn(pyxel.KEY_D) and self.x+move <= 120:
                self.x += move
                self.sprite = self.sprite1
                moved = True
            move -= 1
        # Mouvement des tirs
        for proj in self.projectiles:
            proj[0] += proj[2]
            if proj[0] > 128 or proj[0] < 0:
                self.projectiles.remove(proj)

    def regen(self):
        """
        Régenération des pv
        """
        if self.vies < 6 and self.nourriture > 1 and self.vies > 0:
            self.nourriture -= 2
            self.vies += 1

    def attack(self):
        """
        Lancement des tirs
        """
        if pyxel.btnp(pyxel.KEY_SPACE) and len(self.projectiles) < 4 and\
                self.sac["proj"] > 0:
            # Direction du tir
            self.sac["proj"] -= 1
            if self.sprite == self.sprite2:
                self.projectiles.append([self.x, self.y, -15])
            elif self.sprite == self.sprite1:
                self.projectiles.append([self.x, self.y, 15])
