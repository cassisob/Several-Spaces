import pygame

class Iniciar():

    def __init__(self, tela):
        self.tela = tela
        self.nome_imagem = 'imagens/menu.png'
        self.imagem = pygame.image.load(self.nome_imagem)
        self.retangulo = self.imagem.get_rect()
        self.retangulo_tela = tela.get_rect()
        self.white = (255, 255, 255)
        black = (0, 0, 0)
        self.font = pygame.font.Font("fonte/jogo.ttf", 45)
        self.font1 = pygame.font.Font("fonte/jogo.ttf", 90)
        self.texto = self.font.render('ESPAÇO para jogar', True, self.white)
        self.texto1 = self.font1.render('Several Spaces', True, black)

    def desenha(self):
        self.tela.blit(self.imagem, self.retangulo)
        self.tela.blit(self.texto, [420, 613])
        self.tela.blit(self.texto1, [255, 135])

    def controles(self):
        self.nome_imagem1 = 'imagens/controles.png'
        self.imagem1 = pygame.image.load(self.nome_imagem1)
        self.retangulo1 = self.imagem.get_rect()
        self.tela.blit(self.imagem1, self.retangulo1)