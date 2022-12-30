import view
import pygame
from view import Button
from view import PokerTable
from model import Player

# Classe représentant l'application principale
class MainApplication:
    buttons: list[Button]
    players: list[Player]

    def __init__(self, table: PokerTable):
        self.buttons = []
        self.table = table
        self.clock = pygame.time.Clock()

        mainButton = Button(30, 30, 400, 100, 'Button One (onePress)', myFunction)
        self.buttons.append(mainButton)



    def run(self):
        x = 0
        y = 0
        running = True

        while running:
            for button in self.buttons:
                button.process()
                self.table.screen.blit(button.buttonSurface, button.buttonRect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_LEFT]:
                x -= 1
            elif pressed[pygame.K_RIGHT]:
                x += 1
            elif pressed[pygame.K_DOWN]:
                y += 1
            elif pressed[pygame.K_UP]:
                y -= 1

            # self.screen.get_screen().fill((0, 0, 0))
            # self.screen.get_screen().blit(image, (x, y))
            pygame.display.flip()
            self.clock.tick(120)

        pygame.quit()

def myFunction(source):
    print('Button Pressed')
    print(source)


