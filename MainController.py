import view
import pygame


# Classe représentant l'application principale
class MainApplication:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()

    def run(self):
        x = 0
        y = 0
        running = True

        while running:
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
