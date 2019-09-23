import pygame


class Enemy(object):
    def __init__(self, screen, hitbox):
        self.screen = screen
        self.hitbox = hitbox
        self.hitpoints = 2

    def hit(self):
        self.hitpoints -= 1
        if self.hitpoints <= 0:
            return False
        else:
            return True

    def draw_enemy(self):
        pygame.draw.rect(self.screen, (170, 0, 0), self.hitbox)

