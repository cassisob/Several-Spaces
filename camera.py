
import pygame

class Camera():

    def __init__(self):
        self.width = 1280
        self.height = 720
        self.camera = pygame.Rect(0, 0, self.width, self.height)
        self.screenHeight = 1280
        self.screenWidth = 720
        self.x = 0
        self.y = 0

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        if target.rect.centerx >= 370 and target.rect.x <= 4500:
            self.x = -target.rect.centerx + int(self.screenWidth / 2)
        if target.rect.y <= 250 and self.y <= 150:
            self.y += 5
        if target.rect.y >= 250 and self.y >= 5:
            self.y -= 5
        self.camera = pygame.Rect(self.x, self.y, self.width, self.height)

    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)


