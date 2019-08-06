import pygame
from pygame.math import Vector2 as V2


class Rocket(object):
    def __init__(self, game):
        self.game = game
        size = self.game.screen.get_size()
        self.pos = V2(size[0]/2, size[1]/2)     # Rocket position
        self.vel = V2(0, 0)                     # Rocket velocity
        self.acc = V2(0, 0)                     # Rocket acceleration

    def add_acc(self, force):
        self.acc += force

    def move(self):
        y, x = 10, 10
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.add_acc(V2(0, -1))
        if key[pygame.K_DOWN]:
            self.add_acc(V2(0, 1))
        if key[pygame.K_LEFT]:
            self.add_acc(V2(-1, 0))
        if key[pygame.K_RIGHT]:
            self.add_acc(V2(1, 0))
        self.vel *= 0.3
        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

    def draw(self):
        points = [V2(0, -10), V2(5, 5), V2(-5, 5)]
        points = [self.pos + p * 2 for p in points]
        pygame.draw.polygon(self.game.screen, (255, 255, 255), points)

