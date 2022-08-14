# Simple snake game

import pygame
import random
import time

WINDOW_X = 1280
WINDOW_Y = 720

# Initialize the pygame module.
pygame.init()

# Initialize the pygame Window
pygame.display.set_caption("Snek")
screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y))

# FPS Controller
clock = pygame.time.Clock()
# deltatime
dt = clock / 1000

class Snake:
    def __init__(self):
        self.speed = 10
        self.start_position = (WINDOW_X // 2, WINDOW_Y // 2)
        self.image = pygame.surface.Surface()









