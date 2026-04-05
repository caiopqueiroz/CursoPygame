import pygame
import sys
from random import randint


pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Desafio Aula 4')
clock = pygame.time.Clock()
# cores
preto = (0, 0, 0)
verde = (61, 252, 102)
verde_cinza = (96, 167, 111)
cinza = (37, 51, 40)
# player
pontos = 0
v_player = 5
l_player = 50
h_player = 50
x_player = (800 - l_player) // 2
y_player = (600 - h_player) // 2
# inimigo
v_inimigo = 2
l_inimigo = 50
h_inimigo = 50
x_inimigo = 700
y_inimigo = 500
# inimigo2
v_inimigo2 = 1
x_inimigo2 = 100
y_inimigo2 = 500
# item
x_item = 100
y_item = 100
r_item = 12

while True:
    # eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # lógica
    # salvando posição antiga do player
    x_anterior_player = x_player
    y_anterior_player = y_player
    
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

    # movimentação dos inimigos
    if x_player > x_inimigo:
        x_inimigo += v_inimigo
    elif x_player < x_inimigo: 
        x_inimigo -= v_inimigo
    if y_player > y_inimigo:
        y_inimigo += v_inimigo
    elif y_player < y_inimigo:
        y_inimigo -= v_inimigo

    if x_player > x_inimigo2:
        x_inimigo2 += v_inimigo2
    elif x_player < x_inimigo2: 
        x_inimigo2 -= v_inimigo2
    if y_player > y_inimigo2:
        y_inimigo2 += v_inimigo2
    elif y_player < y_inimigo2:
        y_inimigo2 -= v_inimigo2

    # definindo colisão
    tela_colisao_cima = pygame.Rect(0, -1, 800, 1)
    tela_colisao_esquerda = pygame.Rect(-1, 0, 1, 600)
    tela_colisao_direita = pygame.Rect(800, 0, 1, 600)
    tela_colisao_baixo = pygame.Rect(0, 600, 800, 1)
    player_colisao = pygame.Rect(x_player, y_player, l_player,  h_player)
    inimigo_colisao = pygame.Rect(x_inimigo, y_inimigo, l_player,h_player)
    inimigo2_colisao = pygame.Rect(x_inimigo2, y_inimigo2, l_inimigo, h_inimigo)
    item_colisao = pygame.Rect(x_item - r_item, y_item - r_item, 2 * r_item, 2 * r_item)

    # aplicando colisão
    if player_colisao.colliderect(tela_colisao_cima):
        x_player = x_anterior_player
        y_player = y_anterior_player
    if player_colisao.colliderect(tela_colisao_esquerda):
        x_player = x_anterior_player
        y_player = y_anterior_player
    if player_colisao.colliderect(tela_colisao_direita):
        x_player = x_anterior_player
        y_player = y_anterior_player
    if player_colisao.colliderect(tela_colisao_baixo):
        x_player = x_anterior_player
        y_player = y_anterior_player

    if player_colisao.colliderect(inimigo_colisao):
        pygame.quit()
        sys.exit()
    if player_colisao.colliderect(inimigo2_colisao):
        pygame.quit()
        sys.exit()

    if player_colisao.colliderect(item_colisao):
        x_item = randint(0, 800 - r_item)
        y_item = randint(0, 600 - r_item)
        pontos += 1
        print(f'Pontos: {pontos}')

    # desenho
    tela.fill(preto)
    pygame.draw.circle(tela, verde, (x_item, y_item), r_item)
    pygame.draw.rect(tela, verde_cinza, (x_inimigo, y_inimigo, l_inimigo, h_inimigo))
    pygame.draw.rect(tela, verde_cinza, (x_inimigo2, y_inimigo2, l_inimigo, h_inimigo))
    pygame.draw.rect(tela, verde, (x_player, y_player, l_player, h_player))

    # atualizações
    pygame.display.update()

    # travar fps
    clock.tick(60)