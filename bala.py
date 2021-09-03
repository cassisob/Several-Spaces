import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, tela, nave):
        super(Bullet, self).__init__()
        self.tela = tela
        self.retangulo = pygame.Rect(0, 0, 9, 20)
        self.retangulo.centerx = nave.retangulo.centerx
        self.retangulo.top = nave.retangulo.top
        self.y = float(self.retangulo.y)
        self.cor = (255, 255, 255)
        self.velocidade = 20


    def atualiza(self):
        self.y -= self.velocidade
        self.retangulo.y = self.y


    def desenha(self):
        pygame.draw.rect(self.tela, self.cor, self.retangulo)

