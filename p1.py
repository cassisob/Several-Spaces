import pygame

class Orion():

    def __init__(self, tela, walls):
        self.velocidade = 10
        self.jumps = 5
        self.tela = tela
        self.nome_imagem = 'imagens/orion3.png'
        self.imagem = pygame.image.load(self.nome_imagem)
        self.rect = self.imagem.get_rect()
        self.rect.centerx = 370
        self.rect.centery = 570
        self.move_direita = False
        self.move_esquerda = False
        self.move_cima = False
        self.move_baixo = False
        self.pula = False
        self.continuo = 10
        self.acum2 = 0
        self.direction = 'right'
        self.walls = walls

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

    def colisao(self):
        hits = pygame.sprite.spritecollide(self, self.walls, False)
        for hit in hits:
            if self.rect.y - hit.rect.top < 0:
                self.rect.y = hit.rect.top - self.rect.height
            else:
                self.rect = self.backupRect
            self.jumps = 5

    def atualiza(self, floresta):
        self.backupRect = self.rect.copy()
        if self.move_direita and self.rect.x <= 5300:
            self.rect.centerx += self.velocidade
            self.direcao('right')
            if self.rect.x >= 350 and self.rect.x <= 4500:
                floresta.retangulo.x -= 1
        if self.move_esquerda and self.rect.left > 25:
            self.rect.centerx -= self.velocidade
            self.direcao('left')
            if self.rect.x >= 350  and self.rect.x <= 4500:
                floresta.retangulo.x += 1
        if self.move_baixo:
            self.rect.centery += 5
        self.rect.y += self.continuo
        if self.pula:
            if self.jumps >= 0:
                if self.acum2 <= 5:
                    self.rect.centery -= 30
                    self.acum2 += 1
                    self.pula = True
                else:
                    self.acum2 = 0
                    self.pula = False
                self.jumps -= 1
        self.colisao()




