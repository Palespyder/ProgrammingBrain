import math

import pygame
import random
from settings import *


class Food(pygame.sprite.Sprite):
    def __init__(self, pos, group, snake_rect):
        super().__init__(group)
        self.position = pos
        self.group = group
        self.snake_rect = snake_rect

        # Movement
        self.direction = pygame.math.Vector2()
        self.speed = 0

        # AI Variables
        self.is_evading = False

    def check_snake_distance(self):
        """
        Calculate the distance from self to the snake in order to be able to evade.
        :return: The distance from the snake's (x, y) to the rat's (x, y)
        """
        x = self.snake_rect.x - self.rect.x
        y = self.snake_rect.y - self.rect.y
        return math.sqrt((x**2 + y**2))

    def random_navigable_point(self):
        x = random.randint(self.rect.width // 2, WINDOW_X - (self.rect.width // 2))
        y = random.randint(self.rect.height // 2, WINDOW_Y - (self.rect.height // 2))
        return pygame.math.Vector2(x, y)


class Rat(Food):
    def __init__(self, pos, group, snake_rect):
        super(Rat, self).__init__(pos, group, snake_rect)
        self.speed = 100
        self.image = pygame.Surface((32, 32))
        self.image.fill('red')
        self.rect = self.image.get_rect(center=pos)

        self.destination = None

        self.tick_count = 0

    def move(self, dt):
        if self.destination is None:
            self.destination = self.random_navigable_point()
            new_vect = self.destination - self.position
            if self.position[0] <= new_vect.x:
                self.direction.x = 1
            elif self.position[0] >= new_vect.x:
                self.direction.x = -1
            else:
                self.direction.x= 0

            if self.position[1] <= new_vect.y:
                self.direction.y = 1
            elif self.position[1] >= new_vect.y:
                self.direction.y = -1
            else:
                self.direction.y = 0

            self.position += self.direction * self.speed * dt
            self.rect.center = new_vect
            self.destination = None




    def update(self, dt):
        self.move(dt)


