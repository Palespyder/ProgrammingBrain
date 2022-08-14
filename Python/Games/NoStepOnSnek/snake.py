import pygame


class Snake(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.position = pos
        self.group = group
        self.section_size = 32
        self.sections = []
        self.num_sections = 1
        self.image = pygame.Surface((self.section_size, self.section_size))
        self.image.fill('black')
        self.rect = self.image.get_rect(center=pos)

        # Movement
        self.direction = pygame.math.Vector2()
        self.speed = 300

    def input(self):
        keys = pygame.key.get_pressed()

        # Vertical Directions
        if keys[pygame.K_w]:
            self.direction.x = 0
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.x = 0
            self.direction.y = 1

        # Horizontal Directions
        if keys[pygame.K_d]:
            self.direction.y = 0
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.y = 0
            self.direction.x = -1

    def move(self, dt):
        self.position += self.direction * self.speed * dt
        self.rect.center = self.position

    def update(self, dt):
        self.input()
        self.move(dt)


