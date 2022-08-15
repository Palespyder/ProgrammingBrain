# Simple snake game

import pygame
import sys
from level import Level
from settings import *

pygame.init()
pygame.font.init()


class SnekGame:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
        pygame.display.set_caption("No Step on Snek")
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dt = self.clock.tick() / 1000
            self.level.run(dt)
            pygame.display.update()


if __name__ == '__main__':
    snek = SnekGame()
    snek.run()














