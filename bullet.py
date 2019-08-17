<<<<<<< HEAD
import pygame


class Bullet(object):
        def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = 5

    @staticmethod
    def shoot_bullet():
        bullets = []
        while True:
            for bullet in bullets:
                if bullet.y < 0:
                    bullet.y += bullet.speed
                else:
                    bullets.pop(bullets.index(bullet))

        if key[pygame.K_SPACE]:
            if len(bullets) > 10:
                bullets.append(Bullet(490, 576, 4, (255, 255, 255)))

    def draw_bullet(self):
        pygame.draw.circle(self.screen, (255, 255, 255), (490, 576), self.radius, 3)
=======
import pygame


class Bullet(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = 5

        bullets = []
        while True:
            for bullet in bullets:
                if bullet.y < 0:
                    bullet.y += bullet.speed
                else:
                    bullets.pop(bullets.index(bullet))

    @staticmethod
    def shoot_bullet():
        while True:
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                if len(bullets) > 0:
                    bullets.append(Bullet(490, 576, 4, (255, 255, 255)))

    def draw_bullet(self):
        pygame.draw.circle(self.screen, (255, 255, 255), (490, 576), self.radius, 3)
>>>>>>> 8edfd7be70b98c0f6ce38765db4e77f88933fe37
