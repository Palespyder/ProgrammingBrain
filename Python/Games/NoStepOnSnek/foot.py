import pygame
import random


class Foot(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load('assets/images/footprint.png')
        self.rect = self.image.get_rect(center=pos)
        self.position = pos
        self.group = group

    def move(self, dt):
        self.rect.center = (random.randint(100, 1080), random.randint(100, 620))
        images = ['assets/images/footprint.png', 'assets/images/footprint2.png', 'assets/images/footprint3.png', 'assets/images/footprint4.png']
        self.image = pygame.image.load(images[random.randint(0, len(images) - 1)])

    def update(self, dt):
        self.move(dt)

