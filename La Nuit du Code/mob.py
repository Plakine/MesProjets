from pyxel import rndi


class Mob:
    def __init__(self, tipe, plx, ply):
        """
        Tipe 1 -> spider
        tipe 2 -> snake
        """
        self.tipe = tipe
        if tipe == 2:
            self.vies = 4
            self.sprite = [130, 65, 7, 7]
            self.deg = 2
            self.has_seen = False
            self.e = 0
            self.dirx = 0
            self.diry = 0
        elif tipe == 1:
            self.vies = 2
            self.sprite = [120, 64, 8, 8]
            self.deg = 1
        # Coordonées de l'ennedi
        if ply != 100 and ply != 35:
            self.x = abs(120-plx)
            self.y = rndi(35, 90)
        else:
            self.x = rndi(35, 90)
            self.y = abs(120-ply)

    def move(self, player, mobs, fm_count):
        # Mouvement de l'ennemi

        # Mouvement Araignée
        if self.tipe == 1:
            mov = rndi(0, 1)
            if mov == 0:
                if self.x < player.x:
                    for mob in mobs:
                        if mob != self and not (
                            mob.x+1 <= self.x and mob.x+9 >= self.x and
                                mob.y <= self.y and mob.y+8 >= self.y):
                            self.x += 1
                    if len(mobs) == 1:
                        self.x += 1
                elif self.x > player.x:
                    for mob in mobs:
                        if mob != self and not (
                            mob.x-1 <= self.x and mob.x+7 >= self.x and
                                mob.y <= self.y and mob.y+8 >= self.y):
                            self.x -= 1
                    if len(mobs) == 1:
                        self.x -= 1
            elif mov == 1:
                if self.y < player.y:
                    for mob in mobs:
                        if mob != self and not (
                            mob.x <= self.x and mob.x+8 >= self.x and
                                mob.y+1 <= self.y and mob.y+9 >= self.y):
                            self.y += 1
                    if len(mobs) == 1:
                        self.y += 1
                elif self.y > player.y:
                    for mob in mobs:
                        if mob != self and not (
                            mob.x <= self.x and mob.x+8 >= self.x and
                                mob.y-1 <= self.y and mob.y+7 >= self.y):
                            self.y -= 1
                    if len(mobs) == 1:
                        self.y -= 1
        elif self.tipe == 2:
            if ((self.x < player.x+8) and (self.x > player.x-8)) or\
                  ((self.y < player.y+8) and (self.y > player.y-8)):
                self.has_seen = True

            if self.has_seen is False:
                if self.x != player.x and self.y != player.y:
                    if fm_count % 200 == 0:
                        self.e = rndi(0, 1)
                    if self.e == 0:
                        if self.dirx == 0:
                            self.x += 2
                        elif self.dirx == 1:
                            self.x -= 2
                        if self.x+2 >= 120 and self.dirx == 0:
                            self.dirx = 1
                        elif self.x-2 <= 2 and self.dirx == 1:
                            self.dirx = 0
                    else:
                        if self.diry == 0:
                            self.y += 2
                        elif self.diry == 1:
                            self.y -= 2
                        if self.y + 2 < 111 and self.diry == 0:
                            self.diry = (self.diry+1) % 2
                        elif self.y - 2 > 23 and self.diry == 1:
                            self.diry = (self.diry+1) % 2
            else:
                if abs(self.x-player.x) > abs(self.y - player.y):
                    if self.x < player.x:
                        self.x += 3
                    elif self.x > player.x:
                        self.x -= 3
                else:
                    if self.y < player.y:
                        self.y += 3
                    elif self.y > player.y:
                        self.y -= 3
