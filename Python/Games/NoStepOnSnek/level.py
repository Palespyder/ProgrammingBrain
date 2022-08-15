import pygame
from snake import Snake
from foot import Foot
from food import Rat, Rabbit

class Level:
    def __init__(self):

        self.display_surface = pygame.display.get_surface()
        self.all_sprites = pygame.sprite.Group()
        self.setup()

    def setup(self):
        self.snake = Snake((640, 360), self.all_sprites)
        self.rat = Rat((640, 350), self.all_sprites)
        self.rabbit = Rabbit((300, 100), self.all_sprites)


    def run(self, dt):
        self.display_surface.fill((249, 237, 140))
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)