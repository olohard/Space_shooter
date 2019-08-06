# Space_shooter
This game is a classic Space Shooter. I'm glad I can share you my code.
# Introduction 
This is my first bigger project in Python. I'm newbie so it's not really good code, but it works.
# Code
Here is a portion of my code:

    def add_acc(self, force):
        self.acc += force

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.add_acc(pygame.Vector2(-1, 0))
        if key[pygame.K_RIGHT]:
            self.add_acc(pygame.Vector2(1, 0))
        self.vel *= 0.3
        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0
