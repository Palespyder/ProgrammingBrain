import pygame


class Timer:
    def __init__(self, duration, funct = None):
        self.duration = duration
        self.func = funct
        self.time = 0
        self.active = False

    def activate(self):
        pass

    def deactivate(self):
        pass

    def update(self):
        pass
