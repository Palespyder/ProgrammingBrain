import pygame
import random
from settings import *


class Food(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.position = pos
        self.group = group

        # Movement
        self.direction = pygame.math.Vector2()
        self.speed = 0


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
        self.speed = 100
        self.image = pygame.Surface((10, 10))
        self.image.fill('blue')
        self.rect = self.image.get_rect(center=pos)

    def move(self, dt):
        pass

    def update(self, dt):
        pass


class Rat(Food):
    def __init__(self, pos, group):
        super(Rat, self).__init__(pos, group)
        self.speed = 200
        self.image = pygame.Surface((20, 20))
        self.image.fill('red')
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


class Rabbit(Food):
    def __init__(self, pos, group):
        super(Rabbit, self).__init__(pos, group)
        self.speed = 295
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


