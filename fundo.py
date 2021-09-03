import pygame


class Forest():

    def __init__(self, tela):
        self.tela = tela
        self.nome_imagem = 'imagens/fundo_floresta.png'
        self.imagem = pygame.image.load(self.nome_imagem)
        self.retangulo = self.imagem.get_rect()
        self.retangulo_tela = tela.get_rect()
        self.retangulo.centerx = self.retangulo_tela.centerx
        self.retangulo.bottom = self.retangulo_tela.bottom
        self.nome_imagem1 = 'imagens/nave.png'
        tamanho = 3
        self.imagem1 = pygame.transform.scale(pygame.image.load(self.nome_imagem1), (32 * tamanho, 32 * tamanho))
        self.rect = self.imagem1.get_rect()
        self.rect.y = 528
        self.rect.x = 5280

    def desenha(self):
        self.tela.blit(self.imagem, self.retangulo)

    def desenha1(self, cam):
        self.tela.blit(self.imagem1, cam.apply_rect(self.rect))