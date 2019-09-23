import pygame
import sys
from rocket import Rocket
from bullet import Bullet
from enemy import Enemy
from volley import VolleyOfBullets


def collision(enemy, bullet):
    if enemy.hitbox[1] + enemy.hitbox[2] > bullet.y > enemy.hitbox[2]:
        if enemy.hitbox[0] + enemy.hitbox[3] > bullet.x > enemy.hitbox[3]:
            validation = enemy.hit()
            return validation
    return True


class Game(object):
    def loop(self):
        # Config part of code
        pygame.init()
        pygame.time.delay(100)
        pygame.display.set_caption('Space Battle')
        screen = pygame.display.set_mode((980, 720))
        fps = 0.0

        # Game objects
        player = Rocket(screen)
        pos = player.get_position()
        volley = VolleyOfBullets(screen, pos[0], pos[1], radius=4, color=(255, 255, 255))
        enemy = Enemy(screen, hitbox=(475, 100, 50, 50))

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
            if enemy:
                if len(volley) >= 1:
                    collide = collision(enemy, volley[0])
                    if not collide:
                        self.del_enemy(enemy,volley)
                        enemy = None

            while fps > 100.0:
                fps -= 100.0

            screen.fill((0, 0, 0))
            self.draw(player, volley, enemy,)
            pygame.display.flip()
            self.go(player)

    @staticmethod
    def del_enemy(enemy, volley):
        del enemy
        volley.pop(0)

    # Moving an object
    @staticmethod
    def go(player):
        player.move()

    # Drawing an object
    @staticmethod
    def draw(player, volley, enemy):
        player.draw()
        if enemy:
            enemy.draw_enemy()
        if len(volley):
            volley.draw()

if __name__ == "__main__":
    g = Game()
    g.loop()
