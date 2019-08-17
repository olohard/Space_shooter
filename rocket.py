import pygame
import pygame.math
from bullet import Bullet


class Rocket(object):
    def __init__(self, screen):
        self.screen = screen
        size = screen.get_size()
        self.pos = pygame.Vector2(size[0]/2, size[1] * 0.9)     # Rocket position
        self.vel = pygame.Vector2(0, 0)                         # Rocket velocity
        self.acc = pygame.Vector2(0, 0)                         # Rocket acceleration

    def add_acc(self, force):
        self.acc += force

    def move(self):
        bullets = []
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.pos.x > 15:
            self.add_acc(pygame.Vector2(-1, 0))
        if key[pygame.K_RIGHT] and self.pos.x < 965:
            self.add_acc(pygame.Vector2(1, 0))

        self.vel *= 0.1
        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

    def draw(self):
        points = [pygame.Vector2(0, -15), pygame.Vector2(7.5, 7.5), pygame.Vector2(-7.5, 7.5)]
        points = [self.pos + p * 2 for p in points]
        pygame.draw.polygon(self.screen, (0, 100, 255), points)
