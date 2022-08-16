import pygame
import pygame.math as pm
import math


def get_distance(start: pm.Vector2, end: pm.Vector2):
    """
    Calculate the distance from self to the snake in order to be able to evade.
    :return: The distance from the snake's (x, y) to the rat's (x, y)
    """
    x = end.x - start.x
    y = end.y - start.y
    return math.sqrt((x ** 2 + y ** 2))


