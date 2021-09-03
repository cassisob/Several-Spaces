import sys, pygame
from inimigo import Macaco
from bala_floresta import Bullet1


def testa_eventos(orion, balas, tela, config):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            testa_eventos_aperta_tecla(evento, orion, balas, tela, config)
        elif evento.type == pygame.KEYUP:
            testa_eventos_solta_tecla(evento, orion)

def atualiza_tela(config, tela, orion, floresta, map, cam, macacos, balas, endgame):
    tela.fill(config.cor_fundo)
    cam.apply(orion)
    floresta.desenha()
    for layer in map.layers:
        tela.blit(layer, cam.apply_rect(layer.get_rect()))
    floresta.desenha1(cam)
    for macaco in macacos.sprites():
        macaco.desenha(cam)
    for bala in balas.sprites():
        bala.desenha(cam)
    if not endgame:
        orion.desenha(cam)
    pygame.display.flip()

def dispara_bala(tela, orion, balas, config):
    if config.acum4 <= 40:
        config.acum4 += 1
        nova_bala = Bullet1(tela, orion)
        balas.add(nova_bala)

def testa_eventos_aperta_tecla(evento, orion, balas, tela, config):
    if evento.key == pygame.K_d:
        orion.move_direita = True
    elif evento.key == pygame.K_a:
        orion.move_esquerda = True
    elif evento.key == pygame.K_s:
        orion.move_baixo = True
    elif evento.key == pygame.K_w:
        pygame.mixer.Sound("sons/jump_01.wav").play()
        orion.pula = True
    elif evento.key == pygame.K_SPACE:
        pygame.mixer.Sound("sons/shot.wav").play()
        dispara_bala(tela, orion, balas, config)

def testa_eventos_solta_tecla(evento, orion):
    if evento.key == pygame.K_d:
        orion.move_direita = False
    elif evento.key == pygame.K_a:
        orion.move_esquerda = False
    elif evento.key == pygame.K_s:
        orion.move_baixo = False

def atualiza_balas(balas):
    for bala in balas.sprites():
        if bala.rect.bottom <= 0:
            balas.remove(bala)
        else:
            bala.atualiza(balas)

def atualiza_macaco(macacos):
    for macaco in macacos.sprites():
        macaco.atualiza()

def cria_macaco(tela, macacos, x, y):
    macaco = Macaco(tela, x, y)
    macacos.add(macaco)

def verifica_colisoes(balas, macacos, walls):
    for bala in balas.sprites():
        for macaco in macacos.sprites():
            if bala.rect.colliderect(macaco.rect):
                balas.remove(bala)
                macacos.remove(macaco)
                break
        hits = pygame.sprite.spritecollide(bala, walls, False)
        if hits:
            balas.remove(bala)

def verifica_fim_jogo_floresta(orion, macacos):
    for macaco in macacos.sprites():
        if orion.rect.colliderect(macaco.rect):
            return True
    return False

def cair(orion):
    if orion.rect.y >= 720:
        return True
    return False

def final(perder, main):
    perder.desenha()
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    main()