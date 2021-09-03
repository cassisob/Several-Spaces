import sys, pygame
import configuracao as c
import funcao_floresta as f1
import funcao_espaco as f2
import os
import os.path

from p1 import Orion
from fundo import Forest
from menu import Iniciar
from nave import Ship
from pygame.sprite import Group
from planeta_alien import Planeta
from camera import Camera
from mapa import MapLoader
from paredes import Parede
from morrer import Game_over
from som import Sound

map = 0
firstTime = True

def iniciaMapa():
    global map
    mapPath = os.path.join("mapa/mapa_final.tmx")
    map = MapLoader(mapPath)
    map.makeMap()

def main():
    global firstTime
    pygame.init()
    pygame.font.init()
    pygame.mouse.set_visible(False)
    config = c.Settings()
    tela = pygame.display.set_mode((config.largura, config.altura))
    pygame.display.set_caption("Several Spaces")
    clock = pygame.time.Clock()
    if firstTime:
        sounds = Sound()
        sounds.playMusic()
    menu = Iniciar(tela)
    menu1(clock, menu)
    perder = Game_over(tela)
    if firstTime:
        iniciaMapa()
        firstTime = False
    fase1(clock, config, tela, Parede, perder)

def menu1(clock, menu):
        x = True
        y = False
        while x:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        x = True
                    if event.key == pygame.K_c:
                        y = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        x = False
                    if event.key == pygame.K_c:
                        y = False
            if y == True:
                menu.controles()
            if y == False:
                menu.desenha()
            pygame.display.flip()

def fase1(clock, config, tela, Parede, perder):
    global map
    walls = pygame.sprite.Group()
    macacos = Group()
    for i in map.tmdata.objects:
        if i.name == 'parede':
            Parede(walls, i.x, i.y, i.width, i.height)
        if i.name == 'mac':
            f1.cria_macaco(tela, macacos, i.x, i.y)
    orion = Orion(tela, walls)
    floresta = Forest(tela)
    cam = Camera()
    balas = Group()
    while True:
        clock.tick(60)
        orion.atualiza(floresta)
        cam.update(orion)
        f1.atualiza_macaco(macacos)
        f1.atualiza_balas(balas)
        f1.verifica_colisoes(balas, macacos, walls)
        f1.testa_eventos(orion, balas, tela, config)
        endgame = f1.cair(orion)
        if not endgame:
            f1.atualiza_tela(config, tela, orion, floresta, map, cam, macacos, balas, endgame)
        else:
            pygame.mixer.Sound("sons/die.wav").play()
            f1.final(perder, main)
        endgame = f1.verifica_fim_jogo_floresta(orion, macacos)
        if endgame:
            pygame.mixer.Sound("sons/die.wav").play()
            f1.atualiza_tela(config, tela, orion, floresta, map, cam, macacos, balas, endgame)
            f1.final(perder, main)
        if orion.rect.x >= 5280:
            fase2(clock, config, tela)

def fase2(clock, config, tela):
    nave = Ship(tela)
    final = Planeta(tela)
    stars = Group()
    balas = Group()
    aliens = Group()
    while True:
        clock.tick(60)
        nave.atualiza()
        endgame = f2.acaba(config, final, nave)
        if not endgame:
            if config.acum2 <= 4550:
                f2.cria_frota(config, tela, aliens)
                f2.cria_estrelas(config, tela, stars)
        if final.retangulo.y == 281:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r:
                        main()
        f2.atualiza_aliens(aliens)
        f2.atualiza_estrelas(stars)
        f2.remove_estrelas(stars)
        f2.atualiza_balas(balas)
        f2.verifica_colisoes(balas, aliens)
        if final.retangulo.y <= -50:
            f2.testa_eventos(nave, balas, tela, config)
        if final.retangulo.y <= 280:
            f2.atualiza_tela(config, tela, nave, balas, aliens, stars, final, endgame)
        endgame = f2.verifica_fim_jogo_espaco(nave, aliens)
        if endgame:
            f2.atualiza_tela(config, tela, nave, balas, aliens, stars, final, endgame)
            f2.final(final, main)
            main()

main()