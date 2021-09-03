import pygame

class Quant() :

    def __init__(self, tela, acum):
        self.tela = tela
        self.acum1 = 0
        white = (255, 255, 255)
        self.font = pygame.font.Font("fonte/jogo.ttf", 45)
        self.texto = self.font.render(str(acum), True, white)


    def desenha(self):
        self.tela.blit(self.texto, [420, 613])