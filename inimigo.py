import pygame
from pygame.sprite import Sprite


class Macaco(Sprite):

    def __init__(self, tela, x, y):
        super(Macaco, self).__init__()
        self.tela = tela
        self.nome_imagem = 'imagens/macaco3.png'
        self.imagem = pygame.image.load(self.nome_imagem)
        self.rect = self.imagem.get_rect()
        self.rect.x = ((x / 128) * 48)
        self.rect.y = ((y / 128) * 48) + 10
        self.acum = 1
        self.direction = 'right'

    def desenha(self, cam):
        self.tela.blit(self.imagem, cam.apply_rect(self.rect))

    def vira(self):
        if self.direction == "left":
            self.imagem = pygame.transform.flip(self.imagem, True, False)
        elif self.direction == "right":
            self.imagem = pygame.transform.flip(self.imagem, True, False)

    def direcao(self, direction):
        if not self.direction == direction:
            self.direction = direction
            self.vira()

    def atualiza(self):
        if self.acum <= 15:
            self.rect.x -= 5
            self.acum += 1
            self.direcao('left')
        elif self.acum <= 30:
            self.rect.x += 5
            self.acum += 1
            self.direcao('right')
        else:
            self.acum = 1



