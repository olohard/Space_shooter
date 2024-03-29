import pygame
from bullet import Bullet
from enemy import Enemy


class VolleyOfBullets(list):
    def __init__(self, screen, rocketx, rockety, radius, color):
        super().__init__()
        self.screen = screen
        self.rocketx = rocketx
        self.rockety = rockety
        self.radius = radius
        self.color = color
        self.max_hitpoints = 10

    def set_rocket_pos(self, vector):
        self.rocketx, self.rockety = vector

    def update(self):
        for bullet in self:
            bullet.update_pos()
            if bullet.get_pos() < 0:
                self.pop(0)

    def shoot_bullet(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            if len(self) == 0:
                self.append(Bullet(self.screen, self.rocketx, self.rockety, 4, (255, 255, 255)))

    def draw(self):
        for bullet in self:
            bullet.draw_bullet()
    @staticmethod
    def if_collide(enemy, bullet):
        del enemy
        del bullet
