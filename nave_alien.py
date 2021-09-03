import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, tela):
        super(Alien, self).__init__()
        self.tela = tela
        self.nome_imagem = 'imagens/nave_alien1.png'
        self.imagem = pygame.image.load(self.nome_imagem)
        self.rect = self.imagem.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.y = float(self.rect.x)

    def desenha(self):
        self.tela.blit(self.imagem, self.rect)

    def atualiza(self):
        self.y += 5
        self.rect.y = self.y
