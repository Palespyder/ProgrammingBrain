import pygame as pg
from settings import *
from world_objects import AEntity
from atlysmath import *


class Player(AEntity):
    def __init__(self, location: pg.math.Vector2, rotation: pg.math.Vector2,
                 scale: pg.math.Vector2, group: pg.sprite.Group):
        super().__init__(location, rotation, scale, group)

        # Player Variables
        self.speed = 200

        #self.image = pg.Surface((self.world_scale.x, self.world_scale.y))
        self.image = pg.image.load('assets/images/character/male/character.png')
        #self.image.fill('white')
        self.rect = self.image.get_rect(center=(self.world_location.x, self.world_location.y))

    def input(self):
        keys = pg.key.get_pressed()

        # Vertical Directions
        if keys[pg.K_w]:
            self.world_rotation.y = -1
        elif keys[pg.K_s]:
            self.world_rotation.y = 1
        else:
            self.world_rotation.y = 0

        # Horizontal Directions
        if keys[pg.K_d]:
            self.world_rotation.x = 1
        elif keys[pg.K_a]:
            self.world_rotation.x = -1
        else:
            self.world_rotation.x = 0

        if keys[pg.K_BACKSPACE]:
            pg.quit()
            exit()

    def move(self, dt):
        self.world_location += self.world_rotation * self.speed * dt
        self.rect.center = (self.world_location.x, self.world_location.y)

    def update(self, dt):
        self.input()
        self.move(dt)