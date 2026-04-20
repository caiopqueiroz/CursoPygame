import pygame
import sys

pygame.init()
pygame.mixer.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Aula 7')
clock = pygame.time.Clock()
# cores
preto = (0, 0, 0)
verde = (0, 255, 0)
# estado
estado = 'jogando'
# sons
som_pulo = pygame.mixer.Sound('aula07/sons/madeira.mp3')
som_andar = pygame.mixer.Sound('aula07/sons/walk.mp3')
# musica
pygame.mixer.music.load('aula07/sons/musica.mp3')
# player
l_player = 35
h_player = 70
v_player = 5
x_player = (800 - l_player) // 2
y_player = (600 - h_player) // 2
player_imagem = pygame.image.load('aula07/sprites/player.png').convert_alpha()
player_imagem = pygame.transform.scale(player_imagem, (35, 70))
# tocando música
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.05)

while True:
    # eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_p:
                som_pulo.play()
            if evento.key == pygame.K_w or evento.key == pygame.K_a or evento.key == pygame.K_s or evento.key == pygame.K_d:
                som_andar.play()

    # lógica 
    if estado == 'jogando':
        # definindo colisões
        colisao_player = pygame.Rect(x_player, y_player, l_player, h_player)

        # aplicando colisões

        # movendo o player
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w]:
            y_player -= v_player
        elif teclas[pygame.K_a]:
            x_player -= v_player
        elif teclas[pygame.K_s]:
            y_player += v_player
        elif teclas[pygame.K_d]:
            x_player += v_player
        else:
            som_andar.stop()

        # impedindo o player de sair da tela
        if x_player < 0:
            x_player = 0
        if y_player < 0:
            y_player = 0
        if x_player > 800 - l_player:
            x_player = 800 - l_player
        if y_player >  600 - h_player:
            y_player = 600 - h_player 

    # desenho
    if estado == 'jogando':
        tela.fill(preto)
        tela.blit(player_imagem, (x_player, y_player))

    # atualizações
    pygame.display.update()

    # travar fps
    clock.tick(60)