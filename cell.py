#### import

import threading
import random
import pygame


# class
class Cell:
    def __init__(self, x, y, list_cells):
        self.cellules = list_cells
        self.x = x
        self.y = y

    
    """
    @explication : fonction pour l'initialisation du jeu aucune vie
    @return : un dictionnaire avec les valeurs initialiser à 0
    @param : 
        self -> lui-même (normal en python)
    """
    def demarrage(self):
        for largeur in range (self.x):
            for longueur in range (self.y):
                self.cellules[largeur,longueur] = 0
    """
    @explication : fonction pour l'initialisation du jeu avec des valeurs aléatoires
    @param : 
        self -> lui-même (normal en python)
    """
    def random_cell(self):
        for item in self.cellules:
            self.cellules[item] = random.randint(0,1)
    


    """
    @explication : detection de cellules voisines 
    @return : le nombre de cellules voisisnes
    @param : 
        self        -> lui-même (normal en python)
        numero_cell -> cellule ciblée
    """
    def get_voisines(self, numero_cell):
        cell_voisine = 0
        for x in range (-1,2):
            for y in range (-1,2):
                verif_cell = (numero_cell[0]+x,numero_cell[1]+y)

                # verification si nous ne sommes pas en dehors
                if verif_cell[0] < self.x  and verif_cell[0] >= 0 :
                    if verif_cell[1] < self.y and verif_cell[1] >= 0:

                        # incremetation du ciompteur de voisine
                        if self.cellules[verif_cell] == 1:

                            if x == 0 and y == 0 : # faut pas qu'elle se compte elle même
                                cell_voisine += 1

        return cell_voisine
    

    """
    @explication : incrementation de l'age des cellules
    @param : 
        self        -> lui-même (normal en python)
    """
    def nouveau_cycle(self):
        nouv_tab = {}
        for item in self.cellules:
            # recupereation des voisins de la cellules en questions
            voisine = self.get_voisines(item)

            # check de letat de la cellule ne question qui est en vie
            if self.cellules[item] == 1 :
                if voisine < 2 : # sous population
                    nouv_tab[item] = 0
                elif voisine > 3 : # sur population
                    nouv_tab[item] = 0
                else : # on garde la cellule en vie
                    nouv_tab[item] = 1



            # dans le cas ou la cellule visée ne contient aucune vie
            elif self.cellules[item] == 0:
                if voisine == 3 : # reproduction des cellules
                    nouv_tab[item] = 1
                else:
                    nouv_tab[item] = 0

        #affectation du nouveau tableau qui a mis à jour les valeurs
        self.cellules = nouv_tab
        
                    


    def get_cellules(self):
        return self.cellules