

class Room:
    def __init__(self, i, j, portes,
                 coffre=0, contenu=None, mob=0, bossfight=False, nourr=None):
        """
        i,j -> coordonées de la pièce
        coffre -> présence d'un coffre
            -1 => Post mob
            0 => non
            1 => oui
            2 => verrouillée
        mob -> nombre d'ennemis
        portes -> [droite, haut, gauche, bas]
            0 => non
            1 => oui
            2 => verrouillée
        """
        self.nourriture = nourr
        self.emplacement = [i, j]
        self.coffre = coffre
        self.ccont = contenu
        self.mob = mob
        self.portes = portes
        self.bf = bossfight
        if bossfight:
            self.save = self.portes
            self.portes = [0, 0, 0, 0]
