from aobject import AObject
import pygame as pg


class Player(AObject):
    def __init__(self, location: pg.math.Vector2, rotation: pg.math.Vector2,
                 scale: pg.math.Vector2, group: pg.sprite.Group,
                 player_info: dict):
        super(Player, self).__init__(location=location, rotation=rotation,
                                     scale=scale, group=group)
        # Player info
        self.first_name = player_info['first_name']
        self.last_name = player_info['last_name']
        self.title = player_info['title']
        self.

    def input(self):
        pass

    def move(self):
        pass

    def update(self):
        self.input()
        self.move()