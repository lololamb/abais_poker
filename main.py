import pygame
from MainController import *
from view import *
from const import *

# Programme principal

# Initialisation de l'écran principal
mainScreen = PokerTable(CONST_SCREEN_WIDTH, CONST_SCREEN_HEIGHT)
mainScreen.initialize()

mainApp = MainApplication(mainScreen)
mainApp.run()


# imageBaseDir = 'images/'
# image = pygame.image.load(imageBaseDir + '6_clubs.png').convert()
