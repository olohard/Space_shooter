import pygame


class Enemy(object):
    def __init__(self, screen):
        self.screen = screen

    def draw_enemy(self):
        pygame.draw.rect(self.screen, (170, 0, 0), (480, 100, 30, 30))

