import pygame
import sys


pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Aula 3')
clock = pygame.time.Clock()
velocidade = 7
largura_arena = 500
altura_arena = 100
x_arena = (800 - largura_arena) // 2
y_arena = (600 - altura_arena) // 2
largura_player = 25
altura_player = 50
raio_cabeca_player = largura_player // 2


# cores
cinza = (85, 85, 85)
vermelho = (255, 0, 0)
preto = (0, 0, 0)


# coordenadas de movimento
x_player = (375)
y_player = (275)

while True:
    # 1) eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2) lógica
    teclas = pygame.key.get_pressed()
    # movimentação do player
    if teclas[pygame.K_w]:
        y_player -= velocidade
    if teclas[pygame.K_a]:
        x_player -= velocidade
    if teclas[pygame.K_s]:
        y_player += velocidade
    if teclas[pygame.K_d]:
        x_player += velocidade

    # impedindo o player de sair da arena
    if x_player < x_arena:
        x_player = x_arena
    if x_player > x_arena + largura_arena - largura_player:
        x_player = x_arena + largura_arena - largura_player
    if y_player < y_arena:
        y_player = y_arena
    if y_player > y_arena + altura_arena - altura_player:
        y_player = y_arena + altura_arena - altura_player

    # 3) desenho
    tela.fill(cinza)
    # pygame.draw.rect(tela, cor, (x, y, altura, largura))
    # pygame.draw.circle(tela, cor, (x, y), raio)
    pygame.draw.rect(tela, vermelho, (x_arena, y_arena, largura_arena, altura_arena)) # arena
    pygame.draw.rect(tela, preto, (x_player, y_player, largura_player, altura_player)) # corpo do player
    pygame.draw.circle(tela, preto, (x_player + raio_cabeca_player, y_player - raio_cabeca_player), raio_cabeca_player) # cabeça do player

    # 4) atualização
    pygame.display.update()

    # 6) FPS
    clock.tick(60)
