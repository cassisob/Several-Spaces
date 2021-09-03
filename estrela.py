import pygame
from random import randint
from pygame.sprite import Sprite


class Star(Sprite):

    def __init__(self, config, tela):
        super(Star, self).__init__()
        self.config = config
        self.tela = tela
        self.nome_imagem = 'imagens/estrela1.png'
        tamanho = 3
        self.imagem = pygame.transform.scale(pygame.image.load(self.nome_imagem), (32*tamanho, 32*tamanho))
        self.retangulo = self.imagem.get_rect()
        self.retangulo.x = randint(0, 1200)
        self.retangulo.y = randint(0, 800)
        self.x = randint(0, 1200)
        self.y = randint(-810, -10)

    def desenha(self):
        self.tela.blit(self.imagem, self.retangulo)

    def atualiza(self):
        self.y += 1
        self.retangulo.y = self.y