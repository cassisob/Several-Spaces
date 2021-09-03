import pygame
from pygame.sprite import Sprite


class Bullet1(Sprite):

    def __init__(self, tela, orion):
        super(Bullet1, self).__init__()
        self.tela = tela
        self.rect = pygame.Rect(0, 0, 10, 5)
        self.rect.centerx = orion.rect.right
        self.rect.centery = orion.rect.centery
        self.cor = (255, 255, 255)
        self.velocidade = 20
        self.acum = 0
        self.dir = orion.direction

    def atualiza(self, balas):
        if self.dir == 'right':
            self.rect.x += self.velocidade
        if self.dir == 'left':
            self.rect.x -= self.velocidade
        if self.acum == 20:
            balas.remove(self)
        self.acum += 1

    def desenha(self, cam):
        pygame.draw.rect(self.tela, self.cor, cam.apply_rect(self.rect))
