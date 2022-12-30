from controller.MainController import *
from view import *
from const import *

# Programme principal

# Initialisation de l'écran principal
table = PokerTable(CONST_SCREEN_WIDTH, CONST_SCREEN_HEIGHT)
table.initialize()

mainApp = MainApplication(table)
mainApp.run()



# imageBaseDir = 'images/'
# image = pygame.image.load(imageBaseDir + '6_clubs.png').convert()
