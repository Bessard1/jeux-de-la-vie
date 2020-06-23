from gui import Gui
import random
import time
import pygame

# definition de contantes

RIEN = 0
VIVANT = 1
NAISSANCE = 2
MORT = 3


# class
class Cell:
    def __init__(self, x, y, gui):
        self.cellules = {} #stocké les valeurs des cellules
        self.x = x
        self.y = y
        self.gui = gui
        self.gui.start()
        self.save_vector = {}

    def get_interface(self):
        return self.gui
    """
    @explication : fonction pour l'initialisation d'une case précise pour le jeu
    @return : None
    @param : 
        self -> lui-même (normal en python)
        interface -> cela permet de mettre à jour la partie graphique
    """
    def set_cellule(self, x, y, value, interface):
        self.cellules[x,y] = value
        interface.updateCell(x, y, value)


    """
    @explication : fonction pour l'initialisation du jeu aucune vie
    @return : un dictionnaire avec les valeurs initialiser à 0
    @param : 
        self -> lui-même (normal en python)
    """
    def demarrage(self):
        for largeur in range (self.x):
            for longueur in range (self.y):
                self.cellules[largeur,longueur] = RIEN
                self.gui.updateCell(largeur, longueur, RIEN)
                self.save_vector[largeur,longueur] = RIEN

    """
    @explication : fonction pour l'initialisation du jeu avec des valeurs aléatoires
    @param : 
        self -> lui-même (normal en python)
    """
    def random_cell(self):
        for item in self.cellules:
            value_rand = random.randint(RIEN,VIVANT)
            self.cellules[item] = value_rand #item = coordonné de la cellule
            self.gui.updateCell(item[0], item[1], value_rand)
            self.save_vector[item] = value_rand


    


    """
    @explication : detection de cellules voisines 
    @return : le nombre de cellules voisisnes
    @param : 
        self        -> lui-même (normal en python)
        numero_cell -> cellule ciblée
    """
    def get_voisines(self, numero_cell):
        cell_voisine = 0
        for y in range (-1,2):
            for x in range (-1,2):
                # numero_cell[0] et numero_cell[1] coordonnée de la cellule passé en parametre de la fonction
                verif_cell = (numero_cell[0]+x,numero_cell[1]+y) #le 0 correspond au x dans les coordonnée et le 1 au y des coordonnée

                # verification si nous ne sommes pas en dehors
                if verif_cell[0] < self.x  and verif_cell[0] >= 0 :
                    if verif_cell[1] < self.y and verif_cell[1] >= 0:

                        # incremetation du compteur de voisine
                        if self.cellules[verif_cell] == 1:

                            if x == 0 and y == 0 : # faut pas qu'elle se compte elle même
                                cell_voisine += 0 #cellule_voisine = cellule_voisine+0
                            else :
                                cell_voisine += 1

        return cell_voisine
    

    """
    @explication : incrementation de l'age des cellules
    @param : 
        self        -> lui-même (normal en python)
    """
    def nouveau_cycle(self):
        nouv_tab = {} #tableau temporaire
        for item in self.cellules:

            # recupereation des voisins de la cellules en questions
            voisine = self.get_voisines(item)

            # check de l'etat de la cellule en question qui est en vie
            if self.cellules[item] == 1 :
                if voisine < 2 : # sous population
                    nouv_tab[item] = RIEN
                    self.save_vector[item] = MORT
                    self.gui.updateCell(item[0], item[1], MORT)
                    
                elif voisine > 3 : # sur population
                    nouv_tab[item] = RIEN
                    self.save_vector[item] = MORT
                    self.gui.updateCell(item[0], item[1], MORT)

                else : # on garde la cellule en vie
                    nouv_tab[item] = VIVANT
                    self.save_vector[item] = VIVANT
                    self.gui.updateCell(item[0], item[1], VIVANT)



            # dans le cas ou la cellule visée ne contient aucune vie
            elif self.cellules[item] == 0:
                if voisine == 3 : # reproduction des cellules
                    nouv_tab[item] = VIVANT
                    self.save_vector[item] = NAISSANCE
                    self.gui.updateCell(item[0], item[1], NAISSANCE)
                else:
                    nouv_tab[item] = RIEN
                    self.save_vector[item] = RIEN
                    self.gui.updateCell(item[0], item[1], RIEN)

        #affectation du nouveau tableau qui a mis à jour les valeurs
        self.cellules = nouv_tab




    """
    @explication : permet de calculer les cellules voisines mais suivants une règle précise
    @param : 
        self        -> lui-même (normal en python)
        numero_cell -> une cellule cible
    """
    def rules_voisines_250(self, numero_cell):
            cell_voisine = 0
            for y in range (-1,2):
                x = -1
                verif_cell = (numero_cell[0]+x,numero_cell[1]+y)
                # verification si nous ne sommes pas en dehors
                if verif_cell[0] < self.x  and verif_cell[0] >= 0 :
                    if verif_cell[1] < self.y and verif_cell[1] >= 0:
                        # incremetation du compteur de voisine
                        # si une cellule voisine à ddroite ou à gauche est en vie alors celle du desssous sera en vie
                        if y != 0 and self.cellules[verif_cell] == 1: #!= différent de
                            cell_voisine += 1

            return cell_voisine
    
    """
    @explication : permet de calculer les cellules voisines mais suivants une règle précise
    @param : 
        self        -> lui-même (normal en python)
        numero_cell -> une cellule cible
    """
    def rules_voisines_126(self, numero_cell):
            cell_voisine = 0
            for y in range (-1,2):
                x = -1
                verif_cell = (numero_cell[0]+x,numero_cell[1]+y)
                # verification si nous ne sommes pas en dehors
                if verif_cell[0] < self.x  and verif_cell[0] >= 0 :
                    if verif_cell[1] < self.y and verif_cell[1] >= 0:
                        # incremetation du compteur de voisine
                        #on compte juste la
                        if self.cellules[verif_cell] == 1:
                            cell_voisine += 1


            return cell_voisine


    """
    @explication : permet de mettre à jour la partie graphique et noyau pourune règle spéciphique
    @param : 
        self        -> lui-même (normal en python)
    """
    def rules_250(self):
            nouv_tab = {}
            for item in self.cellules:

                # recupereation des voisins de la cellules en questions
                voisine = self.rules_voisines_250(item)

                if voisine == 0:
                    nouv_tab[item] = RIEN
                    self.save_vector[item] = RIEN
                    self.gui.updateCell(item[0], item[1], RIEN)
                else: 
                    nouv_tab[item] = VIVANT
                    self.save_vector[item] = VIVANT
                    self.gui.updateCell(item[0], item[1], VIVANT)
                
            #affectation du nouveau tableau qui a mis à jour les valeurs
            self.cellules = nouv_tab


    """
    @explication : permet de mettre à jour la partie graphique et noyau pourune règle spéciphique
    @param : 
        self        -> lui-même (normal en python)
    """
    def rules_126(self):
            nouv_tab = {}
            for item in self.cellules:

                # recupereation des voisins de la cellules en questions
                voisine = self.rules_voisines_126(item)

                if voisine == 0 or voisine == 3: 
                    nouv_tab[item] = RIEN
                    self.save_vector[item] = RIEN
                    self.gui.updateCell(item[0], item[1], RIEN)
                else: 
                    nouv_tab[item] = VIVANT
                    self.save_vector[item] = VIVANT
                    self.gui.updateCell(item[0], item[1], VIVANT)
                
            #affectation du nouveau tableau qui a mis à jour les valeurs
            self.cellules = nouv_tab

    """
    @explication : permet de mettre à jour la partie graphique et noyau pourune règle spéciphique
    @param : 
        self        -> lui-même (normal en python)
        rule_number -> numéro ou None afin de faire un choix dans la fonction appelée
    """
    def call_rules(self, rule_number, choice):
        if  rule_number == 250:
            self.set_cellule(0,20,1, self.gui)
            self.rules_250()
        elif rule_number == 126:
            self.set_cellule(0,20,1, self.gui)
            self.rules_126()
        elif rule_number == 0:
            if choice == True :
                self.random_cell()
            self.nouveau_cycle()
        else :
            return None

    def save_party(self):
        with open("save.txt", "w") as mon_fichier:
            for item in self.cellules:
                mon_fichier.write(str(self.save_vector[item]))
            print("save")
            mon_fichier.close()

    def restore_party(self):
        with open("save.txt", "r") as mon_fichier:
            # le nombre de case present dans la grille puis qui regarde case par case associé à un caractére
            for largeur in range (self.x):
                for longueur in range (self.y):
                    # read(1) lire carctere par caractere
                    char = mon_fichier.read(1)
                    if not char :
                        #quitter les boucles en forcan
                        break
                    else:
                        etat_cell = int(char)
                        if etat_cell != 0 and etat_cell <= 2:
                            self.cellules[largeur,longueur] = VIVANT
                            self.save_vector[largeur,longueur] = VIVANT
                        else:
                            self.cellules[largeur,longueur] = RIEN
                            self.save_vector[largeur,longueur] = RIEN
                    
                        #remise à jour la partie graphique
                        self.gui.updateCell(largeur, longueur, etat_cell)

            print("recover")
            mon_fichier.close()
"""
@explication : fonction principal qui permet de boucler sur les mises à jour du noyaux et de la GUI
"""
def launch():
    
    LARGUEUR  = 20
    LONGUEUR = 40

    
    interface = Gui()

    done = False

    #initialisation des cellules
    cell = Cell(LARGUEUR,LONGUEUR, interface)
    #mise à zero
    cell.demarrage()

    number = None
    choice = False
    while not done:
        time.sleep(0.2)

        # tu met None pour faire celui de base
        # tu met 250,126 pour choisir les règles voulues
        cell.call_rules(number, choice)
        choice = False

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                    pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (20 + 5)
                row = pos[1] // (20 + 5)
                # Set that location to one
                cell.set_cellule(row, column, 1, cell.get_interface())
                print("Click ", pos, "Grid coordinates: ", row, column)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    choice = True
                    number = 0
                elif event.key == pygame.K_d:
                    number = 250
                elif event.key == pygame.K_r:
                    number = 126
                elif event.key == pygame.K_s:
                    cell.save_party()
                elif event.key == pygame.K_o:
                    cell.restore_party()
                    number = None
                elif event.key == pygame.K_n:
                    cell.demarrage()
