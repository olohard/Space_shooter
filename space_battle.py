import pygame
import sys
from rocket import Rocket
from bullet import Bullet


class Game(object):
    def loop(self):
        # Config part of code
        pygame.init()
        pygame.time.delay(20)
        pygame.display.set_caption('Space Battle')
        screen = pygame.display.set_mode((980, 720))
        fps = 0.0
        player = Rocket(screen)
        gun = Bullet(x=490, y=576, radius=4, color=(255,255,255))

        # Main loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit()

            while fps > 16.0:
                fps -= 16.0

            screen.fill((0, 0, 0))
            self.draw(player)
            pygame.display.flip()
            self.go(player)


    # Moving an object
    @staticmethod
    def go(player):
        player.move()

    # Drawing an object
    @staticmethod
    def draw(player):
        player.draw()


if __name__ == "__main__":
    g = Game()
    g.loop()
