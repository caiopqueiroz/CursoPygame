import pygame
import sys
from random import randint


pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Revisão')
clock = pygame.time.Clock()
titulo = pygame.font.SysFont(None, 72)
texto = pygame.font.SysFont(None, 36)
# cores
preto = (0, 0, 0)
branco = (255, 255, 255)
azul = (0, 0, 255)
verde = (0, 255, 0)
vermelho = (255, 0, 0)
# estado 
estado = 'menu'
# player
l_player = 50
h_player = 50
v_player = 5
pontos = 0
x_player = (800 - l_player) // 2
y_player = (600 - h_player) // 2
# item
r_item = 15
x_item = 100
y_item = 100
# inimigo
l_inimigo = 50
h_inimigo = 50
v_inimigo = 2
x_inimigo = 700
y_inimigo = 500
# inimigo2
l_inimigo2 = 20
h_inimigo2 = 70
v_inimigo2 = 3
x_inimigo2 = 3000
y_inimigo2 = 3000
# textos
t1 = titulo.render('ARENA SURVIVAL', True, preto)
t2 = texto.render('Pressione P para jogar', True, preto)
t3 = titulo.render('GAME OVER', True, branco)
t5 = texto.render('Cuidado! Novo inimigo se aproximando...', True, vermelho)
t6 = texto.render('Pressione L para pausar', True, branco)

while True:
    # eventos
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if estado == 'menu' and evento.key == pygame.K_p:
                estado = 'jogando'
            if estado == 'gameover' and evento.key == pygame.K_p:
                estado = 'jogando'
                x_item = 100
                y_item = 100
                x_player = (800 - l_player) // 2
                y_player = (600 - h_player) // 2
                x_inimigo = 700
                y_inimigo = 500
                x_inimigo2 = 3000
                y_inimigo2 = 3000
                pontos = 0
            if estado == 'jogando' and evento.key == pygame.K_l:
                estado = 'menu'

    # lógica
    # contagem de pontos
    t4 = texto.render(f'Pontos: {pontos}', True, branco)

    if estado == 'jogando':
        # movimentação do player
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w]:
            y_player -= v_player
        if teclas[pygame.K_a]:
            x_player -= v_player
        if teclas[pygame.K_s]:
            y_player += v_player
        if teclas[pygame.K_d]:
            x_player += v_player

        # impedindo o player de sair da tela
        if x_player < 0:
            x_player = 0
        if y_player < 0:
            y_player = 0
        if x_player > 800 - l_player:
            x_player = 800 - l_player
        if y_player > 600 - h_player:
            y_player = 600 - h_player
        
        # movimentação do inimigo
        if x_inimigo < x_player:
            x_inimigo += v_inimigo
        else:
            x_inimigo -= v_inimigo
        if y_inimigo < y_player:
            y_inimigo += v_inimigo
        else:
            y_inimigo -= v_inimigo

        # movimentação do inimigo2
        if pontos >= 10:
            if x_inimigo2 < x_player:
                x_inimigo2 += v_inimigo2
            else:
                x_inimigo2 -= v_inimigo2
            if y_inimigo2 < y_player:
                y_inimigo2 += v_inimigo2
            else:
                y_inimigo2 -= v_inimigo2 
    
        # definindo colisões
        colisao_player = pygame.Rect(x_player, y_player, l_player, h_player)
        colisao_item = pygame.Rect(x_item - r_item, y_item - r_item, 2 * r_item, 2 * r_item)
        colisao_inimigo = pygame.Rect(x_inimigo, y_inimigo, l_inimigo, h_inimigo)
        colisao_inimigo2 = pygame.Rect(x_inimigo2, y_inimigo2, l_inimigo2, h_inimigo2)

        # aplicando colisões
        if colisao_player.colliderect(colisao_item):
            x_item = randint(r_item, 800 - r_item)
            y_item = randint(r_item, 600 - r_item)
            pontos += 1
        if colisao_player.colliderect(colisao_inimigo):
            estado = 'gameover'
        if colisao_player.colliderect(colisao_inimigo2):
            estado = 'gameover'

    # desenho 
    if estado == 'menu':
        tela.fill(branco)
        tela.blit(t1, (190, 220))
        tela.blit(t2, (265, 280))
    elif estado == 'jogando':
        tela.fill(preto)
        pygame.draw.rect(tela, azul, (x_player, y_player, l_player, h_player))
        pygame.draw.circle(tela, verde, (x_item, y_item), r_item)
        pygame.draw.rect(tela, vermelho, (x_inimigo, y_inimigo, l_inimigo, h_inimigo))
        pygame.draw.rect(tela, vermelho, (x_inimigo2, y_inimigo2, l_inimigo2, h_inimigo2))
        if pontos == 10:
            tela.blit(t5, (20, 550))
        tela.blit(t4, (20, 20))
        tela.blit(t6, (500, 20))
    elif estado == 'gameover':
        tela.fill(vermelho)
        tela.blit(t3, (250, 235))
        tela.blit(t2, (270, 290))
        tela.blit(t4, (20, 20))
    
    # atualizações
    pygame.display.update()

    # travar fps
    clock.tick(60)