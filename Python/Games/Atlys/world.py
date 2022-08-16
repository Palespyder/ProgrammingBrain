import pygame as pg

class World:
    def __init__(self):
        self.display_surface = pg.display.get_surface()
        self.all_sprites = pg.sprite.Group()

    def setup(self):
        pass

    def run(self, dt):
        self.display_surface.fill((249, 237, 140))
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)