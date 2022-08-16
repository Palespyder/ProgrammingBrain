import pygame as pg
import sys
from settings import *
from world import World


class Atlys:
    def __init__(self):
        # Pygame Functionality
        pg.init()
        pg.font.init()
        pg.display.set_caption("Atlys - A Pirate Survival Adventure")
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pg.RESIZABLE)
        self.clock = pg.time.Clock()

        # World Variables
        self.world = World()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            dt = self.clock.tick() / 1000
            self.world.run(dt)
            pg.display.update()


if __name__ == '__main__':
    atlys = Atlys()
    atlys.run()