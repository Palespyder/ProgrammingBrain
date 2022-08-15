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


class Insect(Food):
    def __init__(self, pos, group):
        super(Insect, self).__init__(pos, group)

    def move(self, dt):
        pass

    def update(self, dt):
        pass


class Mouse(Food):
    def __init__(self, pos, group):
        super(Mouse, self).__init__(pos, group)
        self.speed = 50
        self.image = pygame.Surface((10, 10))
        self.image.fill('blue')
        self.rect = self.image.get_rect(center=pos)

    def move(self, dt):
        pass

    def update(self, dt):
        pass


class Rat(Food):
    def __init__(self, pos, group, snake_rect):
        super(Rat, self).__init__(pos, group, snake_rect)
        self.speed = 100
        self.image = pygame.Surface((32, 32))
        self.image.fill('red')
        self.rect = self.image.get_rect(center=pos)

        self.destination = None

        self.tick_count = 0

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
        return x, y

    def move(self, dt):
        if self.destination is None:
            self.destination = self.random_navigable_point()
            print(f"{self.destination}:{self.rect.center}")
            if self.destination[0] < self.rect.x:
                self.direction.x = -1
                self.direction.y = 0
            if self.destination[0] > self.rect.x:
                self.direction.x = 1
                self.direction.y = 0
            if self.destination[1] < self.rect.y:
                self.direction.x = 0
                self.direction.y = -1
            if self.destination[1] > self.rect.y:
                self.direction.x = 0
                self.direction.y = 1
        self.position += self.direction * self.speed * dt
        self.rect.center = self.position
        if self.rect.center == self.destination:
            self.destination = None



    def evade(self):
        dist_x = WINDOW_X - self.rect.x
        dist_y = WINDOW_Y - self.rect.y

        # Find greatest distance direction from current.
        greatest = 0
        greatest_name = None
        if dist_x - self.rect.x > greatest:
            greatest = dist_x
            greatest_name = "Right"

        if dist_y - self.rect.y > greatest:
            greatest = dist_y
            greatest_name = "Down"

        if self.rect.x + self.rect.x > greatest:
            greatest = self.rect.x
            greatest_name = "Left"

        if self.rect.y + self.rect.y > greatest:
            greatest = self.rect.y
            greatest_name = "Up"

        print(self.random_navigable_point())


    def update(self, dt):
        if not self.is_evading:
            self.move(dt)
            if self.check_snake_distance() <= 200:
                self.is_evading= True
                self.evade()
        elif self.is_evading and self.check_snake_distance() >= 200:
            self.is_evading = False
            self.move(dt)


class Rabbit(Food):
    def __init__(self, pos, group, snake_rect):
        super(Rabbit, self).__init__(pos, group, snake_rect)
        self.speed = 200
        self.image = pygame.Surface((30, 30))
        self.image.fill('white')
        self.rect = self.image.get_rect(center=pos)
        self.tick_count = 0

    def move(self, dt):
        if self.tick_count >= random.randint(120, 241):
            rnd_num = random.randint(0, 10)
            if rnd_num == 0:
                self.direction.y = 0
                self.direction.x = -1
            elif rnd_num == 2:
                self.direction.x = 0
                self.direction.y = -1
            elif rnd_num == 4:
                self.direction.y = 0
                self.direction.x = 1
            elif rnd_num == 4:
                self.direction.x = 0
                self.direction.y = 1
            self.tick_count = 0

        if self.position[0] <= 0 + self.rect.width // 2:
            self.direction.y = 0
            self.direction.x = 1
            self.position += self.direction * self.speed * dt
        elif self.position[0] >= WINDOW_X - self.rect.width // 2:
            self.direction.y = 0
            self.direction.x = -1
            self.position += self.direction * self.speed * dt
        elif self.position[1] <= 0 + self.rect.height // 2:
            self.direction.x = 0
            self.direction.y = 1
            self.position += self.direction * self.speed * dt
        elif self.position[1] >= WINDOW_Y - self.rect.height // 2:
            self.direction.x = 0
            self.direction.y = -1
            self.position += self.direction * self.speed * dt
        else:
            self.position += self.direction * self.speed * dt
            self.rect.center = self.position
        self.tick_count += 1

    def update(self, dt):
        self.move(dt)


