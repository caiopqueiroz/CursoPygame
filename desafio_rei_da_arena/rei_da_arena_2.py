# tela de início: aperte 'teclasp' para jogar 
# jogo inicia: inimigo vai na sua direção
# wasd move o jogador: aperte 'o' quando a arma estiver tocando o inimigo para matá-lo
# quando um inimigo é morto: outro aparece em uma posição aleatória
# quando o jogador tocar uma relíquia: outra aparece em uma posição aleatória e 1 ponto é somado 
# quando o jogador atingir 10 pontos: - 


import pygame
import sys
from random import randint


pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Rei da Arena')
clock = pygame.time.Clock()
# cores
preto = (0, 0, 0)
branco = (255, 255, 255)
cinza = (138, 138, 138)
azul = (0, 0, 255)
vermelho = (255, 0, 0)
amarelo = (255, 255, 0)
# estado 
estado = 'inicio'
# fontes
titulo = pygame.font.SysFont(None, 72)
texto = pygame.font.SysFont(None, 36)
# textos
nome = titulo.render('Rei da Arena', True, branco)
aperte_p = texto.render('Aperte P para jogar', True, branco)
# player 
v_player = 7
l_player = 60
h_player = 60
x_player = (800 - l_player) // 2
y_player = (600 - h_player) // 2
# espada do player
estado_espada = 'direita'
l_espada_player = 60
h_espada_player = 10 
x_espada_player = x_player + l_player
y_espada_player = y_player
# inimigo
v_inimigo = 2
l_inimigo = l_player
h_inimigo = h_player
x_inimigo = randint(0, 800 - l_inimigo)
y_inimigo = randint(0, 600 - h_inimigo)
# reliquia 
l_reliquia = 30
h_reliquia = 30
x_reliquia = randint(0, 800 - l_reliquia)
y_reliquia = randint(0, 600 - h_reliquia)
# pontos 
pontos = 0

while True:
    # eventos 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_p:
                if estado == 'inicio':
                    estado = 'jogando'
            if evento.key == pygame.K_o:
                if colisao_espada_player.colliderect(colisao_inimigo): 
                    x_inimigo = randint(0, 800 - l_inimigo)
                    y_inimigo = randint(0, 600 - h_inimigo)
            # mudando a direção da espada de acordo com a direção do player
            if evento.key == pygame.K_a:
                estado_espada = 'esquerda'
            if evento.key == pygame.K_d:
                estado_espada = 'direita'

    # lógica
    if estado == 'inicio':
        pass 
    
    if estado == 'jogando':
        # definindo colisões
        colisao_player = pygame.Rect(x_player, y_player, l_player, h_player)
        colisao_espada_player = pygame.Rect(x_espada_player, y_espada_player, l_espada_player, h_espada_player)
        colisao_inimigo = pygame.Rect(x_inimigo, y_inimigo, l_inimigo, h_inimigo)
        colisao_reliquia = pygame.Rect(x_reliquia, y_reliquia, l_reliquia, h_reliquia)

        # aplicando colisões
        if colisao_player.colliderect(colisao_reliquia):
            x_reliquia = randint(0, 800 - l_reliquia)
            y_reliquia = randint(0, 600 - h_reliquia)
            pontos += 1

        # movimentação do inimigo
        if x_inimigo < x_player:
            x_inimigo += v_inimigo
        else:
            x_inimigo -= v_inimigo 
        if y_inimigo < y_player:
            y_inimigo += v_inimigo
        else:
            y_inimigo -= v_inimigo

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

        # movimentação da espada do player
        if estado_espada == 'direita':
            x_espada_player = x_player + l_player
        else:
            x_espada_player = x_player - l_player
        y_espada_player = y_player   

    # desenho
    if estado == 'inicio':
        tela.fill(preto)
        tela.blit(nome, (100, 100))
        tela.blit(aperte_p, (100, 200))

    if estado == 'jogando':
        tela.fill(cinza)
        # player
        pygame.draw.rect(tela, azul, (x_player, y_player, l_player, h_player))
        pygame.draw.rect(tela, branco, (x_espada_player, y_espada_player, l_espada_player, h_espada_player))
        # inimigo 
        pygame.draw.rect(tela, vermelho, (x_inimigo, y_inimigo, l_inimigo, h_inimigo))
        # relíquia 
        pygame.draw.rect(tela, amarelo, (x_reliquia, y_reliquia, l_reliquia, h_reliquia))
        # criando e exibindo contagem de pontos
        contagem_pontos = texto.render(f'Pontos: {pontos}', True, preto)
        tela.blit(contagem_pontos, (50, 50))

    # atualizações
    pygame.display.update()

    # travar fps
    clock.tick(60)

