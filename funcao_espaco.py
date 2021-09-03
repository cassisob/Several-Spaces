import sys, pygame
from bala import Bullet
from nave_alien import Alien
from random import randint
from estrela import Star


def testa_eventos(nave, balas, tela, config):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            testa_eventos_aperta_tecla(evento, nave, balas, tela, config)
        elif evento.type == pygame.KEYUP:
            testa_eventos_solta_tecla(evento, nave)

def atualiza_tela(config, tela, nave, balas, aliens, stars, final, endgame):
    tela.fill(config.cor_fundo)
    final.comeca()
    for star in stars.sprites():
        star.desenha()
    if config.acum2 == 5000:
        final.atualiza()
        final.desenha()
        nave.desenha()
        pygame.display.flip()
        return
    config.acum2 += 1
    if not endgame:
        nave.desenha()
    for alien in aliens.sprites():
        alien.desenha()
    for bala in balas.sprites():
        bala.desenha()
    pygame.display.flip()

def dispara_bala(tela, nave, balas, config):
    if config.acum1 <= 40:
        config.acum1 += 1
        nova_bala = Bullet(tela, nave)
        balas.add(nova_bala)

def testa_eventos_aperta_tecla(evento, nave, balas, tela, config):
    if evento.key == pygame.K_d:
        nave.move_direita = True
    elif evento.key == pygame.K_a:
        nave.move_esquerda = True
    elif evento.key == pygame.K_s:
        nave.move_baixo = True
    elif evento.key == pygame.K_w:
        nave.move_cima = True
    elif evento.key == pygame.K_SPACE:
        pygame.mixer.Sound("sons/shot.wav").play()
        dispara_bala(tela, nave, balas, config)

def testa_eventos_solta_tecla(evento, nave):
    if evento.key == pygame.K_d:
        nave.move_direita = False
    elif evento.key == pygame.K_a:
        nave.move_esquerda = False
    elif evento.key == pygame.K_s:
        nave.move_baixo = False
    elif evento.key == pygame.K_w:
        nave.move_cima = False

def atualiza_balas(balas):
    for bala in balas.sprites():
        if bala.retangulo.bottom <= 0:
            balas.remove(bala)
        else:
            bala.atualiza()

def obtem_numero_linhas_possiveis(alien_altura):
    espaco_valido_y = 195
    numero_linhas = int(espaco_valido_y / (2 * alien_altura))
    return numero_linhas

def cria_estrelas(config, tela, stars):
    if len(stars) <= 50:
        for i in range(30):
            star = Star(config, tela)
            stars.add(star)

def remove_estrelas(stars):
    for star in stars.sprites():
        if star.retangulo.y >= 800:
            stars.remove(star)

def cria_frota(config, tela, aliens):
    alien = Alien(tela)
    alien_altura = alien.rect.height
    numero_aliens_y = obtem_numero_linhas_possiveis(alien_altura)
    if config.acum == 20:
        for linha in range(numero_aliens_y):
            for alien_numero in range(1):
                alien = cria_alien(tela)
                hits = pygame.sprite.spritecollide(alien, aliens, False)
                if not hits:
                    aliens.add(alien)
        config.acum = 1
    config.acum += 1

def cria_alien(tela):
    alien = Alien(tela)
    alien.y = -50
    alien.rect.x = randint(50, 1180)
    alien.rect.y = alien.y
    return alien

def atualiza_aliens(aliens):
    for alien in aliens.sprites():
        alien.atualiza()

def atualiza_estrelas(stars):
    for star in stars.sprites():
        star.atualiza()

def verifica_colisoes(balas, aliens):
    for bala in balas.sprites():
        for alien in aliens.sprites():
            if bala.retangulo.colliderect(alien.rect):
                balas.remove(bala)
                aliens.remove(alien)
                break

def verifica_fim_jogo_espaco(nave, aliens):
    for alien in aliens.sprites():
        if nave.retangulo.colliderect(alien.rect):
            return True
    return False

def acaba(config, final, nave):
    if config.acum2 == 5000:
        nave.desce()
        final.desenha()
        final.atualiza()
        pygame.display.flip()
        return True
    config.acum2 += 1
    return False

def final(final, main):
    final.desenha1()
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    main()