import pygame

class Ship():

    def __init__(self, tela):
        self.velocidade = 5
        self.tela = tela
        self.nome_imagem = 'imagens/nave.png'
        tamanho = 3
        self.imagem = pygame.transform.scale(pygame.image.load(self.nome_imagem), (32 * tamanho, 32 * tamanho))
        self.retangulo = self.imagem.get_rect()
        self.retangulo_tela = tela.get_rect()
        self.retangulo.centerx = 1180
        self.retangulo.bottom = self.retangulo_tela.bottom
        self.move_direita = False
        self.move_esquerda = False
        self.move_cima = False
        self.move_baixo = False

    def desenha(self):
        self.tela.blit(self.imagem, self.retangulo)

    def atualiza(self):
        if self.move_direita and self.retangulo.right < 1230:
            self.retangulo.centerx += self.velocidade
        if self.move_esquerda and self.retangulo.left > 50:
            self.retangulo.centerx -= self.velocidade
        if self.move_baixo:
            if self.retangulo.y <= 620:
                self.retangulo.centery += self.velocidade
        if self.move_cima:
            if self.retangulo.y >= 5:
                self.retangulo.centery -= self.velocidade

    def desce(self):
        self.retangulo.y += 5