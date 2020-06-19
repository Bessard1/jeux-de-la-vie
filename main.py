from gui import Gui
import random, pygame, time
from cell import Cell

LARGUEUR = 20
LONGUEUR = 20

done = False
interface = Gui()

list_cells = {}
# initialisation des cellules
cell = Cell(LARGUEUR, LONGUEUR, list_cells)
# mise à zero
cell.demarrage()
cell.random_cell()

interface.start()
interface.updateCell(10, 10, 0)
interface.updateCell(10, 11, 1)
interface.updateCell(10, 12, 2)
interface.updateCell(10, 13, 3)

while not done:  # main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("je print a")
        time.sleep(0.25)
        print(cell.get_cellules())
        print(" ")
        cell.nouveau_cycle()
        print("nouv")
        print(cell.get_cellules())

