import pygame
import sys
from random import randint

pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Aula 4')
clock = pygame.time.Clock()
# cores
preto = (0, 0, 0)
azul = (0, 0, 255)
rosa_claro = (255, 203, 217)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
# player
velocidade = 7
l_player = 30
h_player = 60
raio_player = l_player / 2
x_player = (800 - l_player) / 2
y_player = (600 - h_player) / 2
# inimigo
l_inimigo = 100
h_inimigo = 100
cor_inimigo = vermelho
x_inimigo = x_player + 200
y_inimigo = y_player
# objeto
l_objeto = 50
h_objeto = 50
x_objeto = x_player - 200
y_objeto = y_player
cor_objeto = verde

while True:
    # eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # lógica 
    # salvando posição antiga
    x_anterior_player = x_player
    y_anterior_player = y_player
    # movimento do player
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w]:
        y_player -= velocidade
    if teclas[pygame.K_a]:
        x_player -= velocidade
    if teclas[pygame.K_s]:
        y_player += velocidade
    if teclas[pygame.K_d]:
        x_player += velocidade
    # impedindo o player de sair da tela
    if x_player < 0:
        x_player = 0
    if x_player > 800 - l_player:
        x_player = 800 - l_player
    if y_player < 2 * raio_player:
        y_player = 2 * raio_player
    if y_player > 600 - h_player:
        y_player = 600 - h_player  
    # definindo colisao
    player_colisao = pygame.Rect(x_player, y_player - 2 * raio_player, l_player, h_player + 2 * raio_player)
    inimigo_colisao = pygame.Rect(x_inimigo, y_inimigo, l_inimigo, h_inimigo)
    objeto_colisao = pygame.Rect(x_objeto, y_objeto, l_objeto, h_objeto)
    # açao colisao
    cor_inimigo = vermelho
    if player_colisao.colliderect(inimigo_colisao):
        x_player = x_anterior_player
        y_player = y_anterior_player
        cor_inimigo = verde
    if player_colisao.colliderect(objeto_colisao):
        x_objeto = randint(0, 800 - l_objeto)
        y_objeto = randint(0, 600 - h_objeto)
    
    # desenho
    tela.fill(preto)
    pygame.draw.rect(tela, cor_inimigo, (x_inimigo, y_inimigo, l_inimigo, h_inimigo))
    pygame.draw.rect(tela, cor_objeto, (x_objeto, y_objeto, l_objeto, h_objeto))
    pygame.draw.rect(tela, azul, (x_player, y_player, l_player, h_player))
    pygame.draw.circle(tela, rosa_claro, (x_player + raio_player, y_player - raio_player), raio_player)

    # atualização
    pygame.display.update()

    # travar fps
    clock.tick(60)