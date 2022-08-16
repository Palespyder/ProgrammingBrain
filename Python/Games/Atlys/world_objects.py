import pygame as pg
from atlysmath import get_distance
from settings import *


class AEntity(pg.sprite.Sprite):
    def __init__(self, location: pg.math.Vector2, rotation: pg.math.Vector2,
                 scale: pg.math.Vector2, group: pg.sprite.Group):
        super().__init__(group)
        # World Space Variables
        self.world_group = group
        self.world_location = location
        self.world_rotation = rotation
        self.world_scale = scale
        self.distance_to_world_origin = get_distance(WORLD_ORIGIN, self.world_location)
