import pygame as pg
from settings import *
from player import Player


class World:
    def __init__(self):
        self.display_surface = pg.display.get_surface()
        self.all_sprites = pg.sprite.Group()
        self.setup()

    def setup(self):
        self.player = Player(pg.math.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), pg.math.Vector2(0, 0),
                             pg.math.Vector2(32, 32), self.all_sprites)

    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)
