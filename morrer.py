import pygame

class Game_over():

    def __init__(self, tela):
        self.tela = tela
        self.nome_imagem = 'imagens/planeta.png'
        self.tamanho = 8
        self.imagem = pygame.transform.scale(pygame.image.load(self.nome_imagem), (32 * self.tamanho, 32 * self.tamanho))
        self.retangulo = self.imagem.get_rect()
        self.retangulo_tela = tela.get_rect()
        self.retangulo.centerx = self.retangulo_tela.centerx
        self.retangulo.y = -300
        self.acum = 0
        self.nome_imagem1 = 'imagens/ceu.png'
        self.imagem1 = pygame.image.load(self.nome_imagem1)
        self.retangulo1 = self.imagem.get_rect()

    def desenha(self):
        black = (0, 0, 0)
        self.font = pygame.font.Font("fonte/jogo.ttf", 150)
        self.texto = self.font.render('GAME OVER', True, black)
        self.tela.blit(self.texto, [230, 150])
        self.font1 = pygame.font.Font("fonte/jogo.ttf", 40)
        self.texto1 = self.font1.render('Aperte R para recomeçar', True, black)
        self.tela.blit(self.texto1, [370, 300])
        pygame.display.flip()

