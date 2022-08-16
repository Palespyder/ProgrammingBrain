import pygame as pg
from settings import *
from atlys_inc.atlysmath import *


class AObject:
    """
    Any Item in the physical world. This is our WorldObject.
    """
    def __init__(self, location: pg.math.Vector2, rotation: pg.math.Vector2,
                 scale: pg.math.Vector2, group: pg.sprite.Group):

        # World Space Variables
        self.world_group = group
        self.world_location = location
        self.world_rotation = rotation
        self.world_scale = scale
        self.distance_to_world_origin = get_distance(WORLD_ORIGIN, self.world_location)

        # Local(Screen) Space Variables






