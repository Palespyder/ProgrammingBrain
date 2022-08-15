import pygame


class Food(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super.__init__(group)