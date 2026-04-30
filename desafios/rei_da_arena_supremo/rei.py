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
# a cada x pontos: velocidade do inimigo tipo 1 aumenta 
# mostrar pontos na tela durante o jogo
# exibir mensagem quando o a velocidade aumentar

# ideias para aprimorar:
# criar um gerador de inimigos que spawna mais a cada soma +x de pontos 


import pygame
import sys
from random import randint
from random import choice


pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Rei da Arena Supremo')
clock = pygame.time.Clock()
# cores
preto = (0, 0, 0)
branco = (255, 255, 255)
cinza = (138, 138, 138)
azul = (0, 0, 255)
amarelo = (255, 255, 0)
vermelho = (255, 0, 0)
# estado 
estado = 'jogando'
# fonte 
titulo = pygame.font.SysFont(None, 72)
texto = pygame.font.SysFont(None, 36)
# texto
game_over = titulo.render('GAME OVER', True, branco)
aperte_p = texto.render('Aperte P para reiniciar o jogo', True, branco)
mensagem = ''
# player
pontos = 0
pontos_acumulados = 0
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
v_vertical = 0
v_horizontal = 2
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
        if evento.type == pygame.KEYDOWN:
            if [pygame.K_p]:
                if estado == 'gameover':
                    estado = 'jogando'
                    x_player = 100
                    y_player = 100
                    x_inimigo1 = 700
                    y_inimigo1 = 500
                    x_inimigo3 = (800 - l_inimigo3) // 2
                    y_inimigo3 = (600 - h_inimigo3) // 2
                    pontos = 0

    # lógica 
    if estado == 'inicio':
        pass

    if estado == 'jogando':
        # atualizando contagem de pontos da tela
        mostrar_pontos = texto.render(f'Pontos: {pontos}', True, azul)

        # aumentando velocidade de acordo com a soma de pontos
        if pontos_acumulados == 10:
            mensagem = 'Velocidade aumentou!'
            tempo_mensagem = pygame.time.get_ticks()
            v_inimigo1 += 0.5
            print(v_inimigo1)
            pontos_acumulados = 0

        velocidade_aumentou = texto.render(mensagem, True, preto)
        # ocultado mensagem
        if mensagem:
            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - tempo_mensagem > 2000:
                mensagem = ''

        # definindo colisões
        colisao_reliquia = pygame.Rect(x_reliquia, y_reliquia, l_reliquia, h_reliquia)
        colisao_player = pygame.Rect(x_player, y_player, l_player, h_player)
        colisao_inimigo1 = pygame.Rect(x_inimigo1, y_inimigo1, l_inimigo1, h_inimigo1)
        if pontos >= 30:
            colisao_inimigo2 = pygame.Rect(x_inimigo2, y_inimigo2, l_inimigo2, h_inimigo2)
        colisao_inimigo3 = pygame.Rect(x_inimigo3, y_inimigo3, l_inimigo3, h_inimigo3)

        # aplicando colisões
        if colisao_player.colliderect(colisao_reliquia):
            # mudando a relíquia de posição 
            if x_player > 400:
                x_reliquia = randint(0, 400 - l_reliquia)
            else:
                x_reliquia = randint(400, 800 - l_reliquia)
            y_reliquia = randint(0, 600 - h_reliquia)
            pontos += 1
            pontos_acumulados += 1
            print(f'Pontos: {pontos}')
        if colisao_player.colliderect(colisao_inimigo1):
            estado = 'gameover'
        if pontos >= 30:
            if colisao_player.colliderect(colisao_inimigo2):
                estado = 'gameover'
        if colisao_player.colliderect(colisao_inimigo3):
            estado = 'gameover'

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
        x_inimigo3 += v_horizontal
        y_inimigo3 += v_vertical
        if randint(0, 100) == 0:
            if v_horizontal == 2 or v_horizontal == -2:
                v_horizontal = 0
                v_vertical = choice([-2, 2])
        if randint(0, 100) == 0:
            if v_vertical == 2 or v_vertical == -2:
                v_vertical = 0 
                v_horizontal = choice([-2, 2])

        # impedindo o inimigo 3 de sair da tela
        if x_inimigo3 < 0:
            v_horizontal *= -1
        if x_inimigo3 > 800 - l_inimigo3:
            v_horizontal *= -1
        if y_inimigo3 < 0:
            v_vertical *= -1
        if y_inimigo3 > 600 - h_inimigo3:
            v_vertical *= -1

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
        tela.blit(mostrar_pontos, (50, 50))
        tela.blit(velocidade_aumentou, (50, 450))

    if estado == 'gameover':
        tela.fill(preto)
        tela.blit(game_over, (100, 100))
        tela.blit(aperte_p, (100, 200))
        tela.blit(mostrar_pontos, (100, 300))

    # atualizações
    pygame.display.update()

    # travar fps
    clock.tick(60)