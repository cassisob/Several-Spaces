import pygame

class Parede(pygame.sprite.Sprite):

    def __init__(self, walls, x, y, w, h):
        super().__init__()
        walls.add(self)
        self.x = (x / 128) * 48
        self.y = (y / 128) * 48
        self.w = (w / 128) * 48
        self.h = (h / 128) * 48
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
