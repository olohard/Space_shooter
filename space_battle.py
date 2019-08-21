import pygame
import sys
from rocket import Rocket
from bullet import Bullet
from enemies import Enemy
from volley import VolleyOfBullets


class Game(object):
    def loop(self):
        # Config part of code
        pygame.init()
        pygame.time.delay(20)
        pygame.display.set_caption('Space Battle')
        screen = pygame.display.set_mode((980, 720))
        fps = 0.0

        # Game objects
        player = Rocket(screen)
        pos = player.get_position()
        volley = VolleyOfBullets(screen, pos[0], pos[1], radius=4, color=(255, 255, 255))
        enemy = Enemy(screen)

        # Main loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    pygame.quit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit()
                    pygame.quit()

            pos = player.get_position()
            volley.set_rocket_pos(pos)

            volley.shoot_bullet()
            volley.update()


            while fps > 60.0:
                fps -= 60.0

            screen.fill((0, 0, 0))
            self.draw(player, enemy, volley)
            pygame.display.flip()
            self.go(player)

    # Moving an object
    @staticmethod
    def go(player):
        player.move()

    # Drawing an object
    @staticmethod
    def draw(player, enemy, volley):
        player.draw()
        enemy.draw_enemy()
        volley.draw()

    @staticmethod
    def shoot():
        pass

    @staticmethod
    def spawn():
        pass

if __name__ == "__main__":
    g = Game()
    g.loop()
