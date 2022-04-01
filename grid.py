import random


class Creation:
    def __init__(self):
        # on crée la grille de la map en 11 par 11 et les portes nord , gauche, sud,droite
        self.map = [
            [
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
            ], [
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
            ], [
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
            ], [
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
            ], [
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
            ], [
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
            ], [
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
            ], [
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
            ], [
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
            ], [
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
            ], [
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
            ]
        ]
        self.test = 0

    def see(self):  # affiche la map
        for i in range(11):
            print(self.map[i])

    def expand(self):
        if self.test == 0:
            for i in range(4):  # on choisi aléatoirement si il y auras une porte ou pas
                self.map[5][5][i] = random.randint(
                    0, 1)    # 0 = pas de porte 1 = porte
            if self.map[5][5][0] + self.map[5][5][1] + self.map[5][5][2] + self.map[5][5][3] == 0:
                self.test = 0
                self.expand()   # si il n'y en a pas on recommance

        for x in range(10):  # on par cour la map
            for y in range(10):
                for i in range(3):
                    if self.map[x][y][i] == 1:  # si on trouve un emplacement choisi
                        if i == 0:  # nord
                            if self.map[x][y-1][0] == 1:    # si il ny a pas déjas une porte
                                pass
                            self.map[x][y-1][0] = 1     # on en place une
                        if i == 1:  # gauche
                            if self.map[x-1][y][1] == 1:    # si il ny a pas déjas une porte
                                pass
                            self.map[x-1][y][1] = 1     # on en place une
                        if i == 2:  # sud
                            if self.map[x][y+1][2] == 1:    # si il ny a pas déjas une porte
                                pass
                            self.map[x][y+1][2] = 1     # on en place une
                        if i == 3:  # droite
                            if self.map[x+1][y][3] == 1:    # si il ny a pas déjas une porte
                                pass
                            self.map[x+1][y][3] = 1     # on en place une


creation = Creation()
creation.expand()
creation.see()
