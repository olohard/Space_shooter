import pygame
import sys
from rocket_to_s_b import Rocket


class Game(object):
    def __init__(self):
        # Config part of code
        pygame.init()
        pygame.time.delay(20)
        pygame.display.set_caption('Space Battle')
        self.fps = 100.0
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.delta = 0.0
        self.player = Rocket(self)

        # Main loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit()

            while self.delta > 16.0:
                self.delta -= 16.0

            self.screen.fill((0, 0, 0))
            self.paint()
            pygame.display.flip()
            self.go()

    # Moving an object
    def go(self):
        self.player.move()

    # Drawing an object
    def paint(self):
        self.player.draw()


if __name__ == "__main__":
    Game()
