import pygame


class Planeta():

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
        self.nome_imagem1 = 'imagens/degrade.png'
        self.imagem1 = pygame.image.load(self.nome_imagem1)
        self.retangulo1 = self.imagem.get_rect()
        self.retangulo1.y = -1440

    def desenha(self):
        self.tela.blit(self.imagem, self.retangulo)

    def atualiza(self):
        if self.retangulo.y == 0:
            pygame.mixer.Sound("sons/vitoria.wav").play()
        if self.retangulo.y <= 280:
            self.retangulo.y += 1
        else:
            white = (205,205,205)
            self.font = pygame.font.Font("fonte/jogo.ttf", 120)
            self.texto = self.font.render('MISSÃO CUMPRIDA', True, white)
            self.tela.blit(self.texto, [115, 150])
            self.font1 = pygame.font.Font("fonte/jogo.ttf", 40)
            self.texto1 = self.font1.render('Aperte R para recomeçar', True, white)
            self.tela.blit(self.texto1, [370, 600])
            pygame.display.flip()

    def comeca(self):
        if self.retangulo1.y <= 2160:
            self.retangulo1.y += 5
            self.tela.blit(self.imagem1, self.retangulo1)

    def desenha1(self):
        white = (205,205,205)
        self.font2 = pygame.font.Font("fonte/jogo.ttf", 150)
        self.texto2 = self.font2.render('GAME OVER', True, white)
        self.tela.blit(self.texto2, [230, 150])
        self.font3 = pygame.font.Font("fonte/jogo.ttf", 40)
        self.texto3 = self.font3.render('Aperte R para recomeçar', True, white)
        self.tela.blit(self.texto3, [370, 300])
        pygame.display.flip()