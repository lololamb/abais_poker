import pygame
from const import *
from .PygameButton import *

# Cette classe représente la vue de la table de poker
class PokerTable:
    screen: pygame.Surface
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = None

    def initialize(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        image = pygame.image.load(CONST_IMAGE_BASE_DIR + 'table_poker.jpg').convert()
        image = pygame.transform.scale(image, (self.width, self.height))

        self.screen.blit(image, (0, 0))
        pygame.display.flip()
        running = True

    def get_screen(self):
        return self.screen

    def __str__(self):
        return '(Screen: width' + str(self.width) + ', height: ' + str(self.height) + ')'
