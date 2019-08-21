import pygame
from bullet import Bullet


class VolleyOfBullets(list):
    def __init__(self,screen, x, y, radius, color):
        super().__init__()
        self.screen = screen
        self.rocketx = x
        self.rockety = y
        self.radius = radius
        self.color = color
        self.flag = False

    def set_rocket_pos(self, vector):
        self.rocketx, self.rockety = vector
        self.flag = False

    def update(self):
        for bullet in self:
            bullet.update_pos()
            if bullet.get_pos() < 0:
                self.pop(0)

    def shoot_bullet(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE]:
            if len(self) < 100000 and not self.flag:
                self.append(Bullet(self.screen, self.rocketx, self.rockety, 4, (255, 255, 255)))
                self.flag = True
                print(len(self))
        key = pygame.key.get_pressed()


    def draw(self):
        for bullet in self:
            bullet.draw_bullet()