import pygame as pg
from settings import  *

class HUD:
    def __init__(self, surface):
        self.display_surface = surface
        self.hud_sprites = pg.sprite.Group()

    def setup(self):
        pass

    def update(self, dt):
        self.hud_sprites.draw(self.display_surface)
        self.hud_sprites.update(dt)