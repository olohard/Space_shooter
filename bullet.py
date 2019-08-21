import pygame
from pygame.math import Vector2


class Bullet:
    def __init__(self, screen, x, y, radius, color):
        self.screen = screen
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = 1

    def get_pos(self):
        return self.y

    def update_pos(self):
        self.y -= self.speed


    def collision(self):
        pass

    def draw_bullet(self):
        pygame.draw.circle(self.screen, (255, 255, 255), (int(self.x), int(self.y)), 3, 3)
