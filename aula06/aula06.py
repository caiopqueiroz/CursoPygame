import pygame
import sys 


pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Aula 6')
clock = pygame.time.Clock()
# cores
preto = (0, 0, 0)
azul = (0, 0, 255)
vermelho = (255, 0, 0)
amarelo = (255, 255, 0)
# estado 
estado = 'jogando'
# player
x_player = ((800 // 4) - 50) // 2
y_player = (600 - 50) // 2
player_imagem = pygame.image.load('aula06/player.png').convert_alpha()
player_imagem = pygame.transform.scale(player_imagem, (50, 50))
# coroa
coroa_imagem = pygame.image.load('aula06/coroa.png').convert_alpha()
coroa_imagem = pygame.transform.scale(coroa_imagem, (50, 50))
r_coroa = 20
# canos
inicio_canos = 800 // 4
espaco_canos = 390 // 3
l_canos = 160 // 3
h_canos = 400
canos_imagem = pygame.image.load('aula06/cano.png').convert_alpha()
canos_imagem = pygame.transform.scale(canos_imagem, (l_canos, h_canos))
# gravidade
gravidade = 0.5
velocidade_vertical = 0

while True:
    # eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_p:
                velocidade_vertical = -10

    # lógica 
    if estado == 'jogando':
        # definindo x e y anterior do player
        x_anterior_player = x_player
        y_anterior_player = y_player

        # impedindo o player de sair da tela 
        if x_player < 0:
            x_player = 0
        if x_player > 800 - 50:
            x_player = 800 - 50
        if y_player < 0:
            y_player = 0
        if y_player > 600 - 50:
            y_player = 600 - 50

        # aplicando gravidade
        velocidade_vertical += gravidade
        y_player += velocidade_vertical

        # movendo o player para a direita automaticamente
        x_player += 1

        # definindo colisões
        #colisao_cano = pygame.Rect(x_cano, y_cano, l_cano, h_cano)
        colisao_canos = list()
        for contador in range(0, 4):
            colisao_canos.append(pygame.Rect(inicio_canos + contador * (l_canos + espaco_canos), 0 if contador % 2 == 0 else 200, l_canos, h_canos))
        colisao_player = pygame.Rect(x_player, y_player, 45, 45)
        colisao_coroa = pygame.Rect(inicio_canos + 3 * (l_canos + espaco_canos), 150, 50, 50)

        # aplicando colisões
        for contador in range(0, 4):
            if colisao_player.colliderect(colisao_canos[contador]):
                pygame.quit()
                sys.exit()
        if colisao_player.colliderect(colisao_coroa):
            print('venceu!')

    # desenho
    if estado == 'jogando':
        tela.fill(preto)
        # player
        tela.blit(player_imagem, (x_player, y_player))
        # coroa
        tela.blit(coroa_imagem, (inicio_canos + 3 * (l_canos + espaco_canos), 150))  
        # canos
        for contador in range(0, 4):
            tela.blit(canos_imagem, (inicio_canos + contador * (l_canos + espaco_canos), 0 if contador % 2 == 0 else 200))

    # atualizações
    pygame.display.update()

    # travar fps
    clock.tick(60)