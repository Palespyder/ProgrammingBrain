import pygame

class Snake:
    def __init__(self, pos, group):
        self.speed = 10
        self.position = pos
        self.group = group
        self.direction = pygame.math.Vector2((0, 0))
        self.section_size = 32
        self.sections = []
        self.num_sections = 1
        self.image = pygame.Surface((32, 64))
        self.image.fill('black')
        self.rect = self.image.get_rect(center=pos)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            print("Up")
            self.direction.y = -1
        elif keys[pygame.K_s]:
            print("down")
            self.direction.y = 1


        elif keys[pygame.K_d]:
            print("right")
            self.direction.x = 1
        elif keys[pygame.K_a]:
            print("left")
            self.direction.x = -1

    def update(self, dt):
        self.input()


