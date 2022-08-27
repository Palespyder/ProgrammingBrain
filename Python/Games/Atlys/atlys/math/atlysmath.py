import pygame.math as pm
import math


def get_distance(start: pm.Vector2, end: pm.Vector2):
    """
    Calculate the distance from statrt to end.
    :return: The distance from the start (x, y) to the end (x, y)
    """
    x = end.x - start.x
    y = end.y - start.y
    return math.sqrt((x ** 2 + y ** 2))


