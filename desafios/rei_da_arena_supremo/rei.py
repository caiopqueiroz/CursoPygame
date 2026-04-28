# conceito: você é um guerreiro preso em uma arena amaldiçoada - quanto mais tempo sobrevive... mais o jogo fica insano 

# objetivos:
# sobreviver o máximo tempo possível
# coletar relíquias
# fugir de inimigos
# virar o 'Rei da Arena Supremo'

# player se move com WASD - tem um sprite - som ao andar e ao agir 
# relíquias tem spawn aleatório - dão pontos - som ao coletar
# 3 tipos de inimigos:
# tipo 1: lento - segue o player
# tipo 2: após X pontos - mais rápido
# tipo 3: movimento aleatório  
# encostar no inimigo: game over - som de morte 


import pygame
import sys
from random import randint


pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Rei da Arena Supremo')
clock = pygame.time.Clock()
# cores
preto = (0, 0, 0)
cinza = (138, 138, 138)
azul = (0, 0, 255)
amarelo = (255, 255, 0)
vermelho = (255, 0, 0)
# estado 
estado = 'jogando'
# player
pontos = 0
v_player = 7
l_player = 60
h_player = 60
x_player = 100
y_player = 100
# reliquia
l_reliquia = 40
h_reliquia = 40
x_reliquia = randint(400, 800 - l_reliquia)
y_reliquia = randint(0, 600 - h_reliquia)
# inimigo tipo 1
v_inimigo1 = 2
l_inimigo1 = 60
h_inimigo1 = 60
x_inimigo1 = 700
y_inimigo1 = 500
# inimigo tipo 2
v_inimigo2 = 4
l_inimigo2 = 30
h_inimigo2 = 70
x_inimigo2 = 700
y_inimigo2 = 500
# inimigo tipo 3
v_inimigo3 = 2
l_inimigo3 = 30
h_inimigo3 = 30
x_inimigo3 = (800 - l_inimigo3) // 2
y_inimigo3 = (600 - h_inimigo3) // 2

while True:
    # eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # lógica 
    if estado == 'inicio':
        pass

    if estado == 'jogando':
        # definindo colisões
        colisao_reliquia = pygame.Rect(x_reliquia, y_reliquia, l_reliquia, h_reliquia)
        colisao_player = pygame.Rect(x_player, y_player, l_player, h_player)

        # aplicando colisões
        if colisao_player.colliderect(colisao_reliquia):
            # mudando a relíquia de posição 
            if x_player > 400:
                x_reliquia = randint(0, 400 - l_reliquia)
            else:
                x_reliquia = randint(400, 800 - l_reliquia)
            y_reliquia = randint(0, 600 - h_reliquia)
            pontos += 1 
            print(f'Pontos: {pontos}')

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

        # movimentação do inimigo tipo 1 
        if x_inimigo1 > x_player:
            x_inimigo1 -= v_inimigo1
        else:
            x_inimigo1 += v_inimigo1
        if y_inimigo1 > y_player:
            y_inimigo1 -= v_inimigo1
        else:
            y_inimigo1 += v_inimigo1

        if pontos >= 30:
            # movimentação do inimigo tipo 2
            if x_inimigo2 > x_player:
                x_inimigo2 -= v_inimigo2 
            else:
                x_inimigo2 += v_inimigo2
            if y_inimigo2 > y_player:
                y_inimigo2 -= v_inimigo2
            else:
                y_inimigo2 += v_inimigo2

        # movimentação do inimigo tipo 3 
        direcao_inimigo3 = randint(0, 3)
        print(direcao_inimigo3)
        if direcao_inimigo3 == 0:
            y_inimigo3 -= v_inimigo3
        if direcao_inimigo3 == 1:
            y_inimigo3 -= v_inimigo3
        if direcao_inimigo3 == 2:
            y_inimigo3 += v_inimigo3
        if direcao_inimigo3 == 3:
            x_inimigo3 += v_inimigo3

    # desenho 
    if estado == 'inicio':
        tela.fill(preto)

    if estado == 'jogando':
        tela.fill(cinza)
        # player 
        pygame.draw.rect(tela, azul, (x_player, y_player, h_player, l_player))
        # relíquias
        pygame.draw.rect(tela, amarelo, (x_reliquia, y_reliquia, l_reliquia, h_reliquia))
        # inimigo tipo 1 
        pygame.draw.rect(tela, vermelho, (x_inimigo1, y_inimigo1, l_inimigo1, h_inimigo1))
        if pontos >= 30:
            # inimigo tipo 2 
            pygame.draw.rect(tela, vermelho, (x_inimigo2, y_inimigo2, l_inimigo2, h_inimigo2))
        # inimigo tipo 3
        pygame.draw.rect(tela, vermelho, (x_inimigo3, y_inimigo3, l_inimigo3, h_inimigo3))

    # atualizações
    pygame.display.update()

    # travar fps
    clock.tick(60)