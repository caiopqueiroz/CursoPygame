import pygame 
import sys 


pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Aula 5')
clock = pygame.time.Clock()
estado = 'jogando'
# cores
preto = (0, 0, 0)
azul = (0, 0, 255)
vermelho = (255, 0, 0)
# player
l_player = 30
h_player = 60
r_player = l_player // 2
v_player = 5
x_player = 100
y_player = 100
# inimigo
l_inimigo = 25
h_inimigo = 25
v_inimigo = 2
x_inimigo = 700
y_inimigo = 500

while True:
    # eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if estado == 'game_over' and evento.key == pygame.K_r:
                x_player = 100
                y_player = 100
                x_inimigo = 700
                y_inimigo = 500
                estado = 'jogando'

    # lógica
    # definindo posição anterior do player
    x_anterior_player = x_player
    y_anterior_player = y_player 

    # definindo posição anterior do inimigo
    x_anterior_inimigo = x_inimigo
    y_anterior_inimigo = y_inimigo

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
    if y_player < 2 * r_player:
        y_player = 2 * r_player 
    if x_player > 800 - l_player:
        x_player = 800 - l_player
    if y_player > 600 - h_player:
        y_player = 600 - h_player

    # movimentação do inimigo
    if x_inimigo > x_player:
        x_inimigo -= v_inimigo
    else:
        x_inimigo += v_inimigo
    if y_inimigo >  y_player:
        y_inimigo -= v_inimigo
    else:
        y_inimigo += v_inimigo

    # definindo colisão
    colisao_player = pygame.Rect(x_player, y_player - 2 * r_player, l_player, h_player + 2 * r_player)
    colisao_inimigo = pygame.Rect(x_inimigo, y_inimigo, l_inimigo, h_inimigo)

    # aplicando colisão
    if colisao_player.colliderect(colisao_inimigo):
        estado = 'game_over'
    #if colisao_inimigo.colliderect(colisao_player):
    #    x_inimigo = x_anterior_inimigo
    #    y_inimigo = y_anterior_inimigo

    # desenho
    tela.fill(preto)
    if estado == 'jogando':
        pygame.draw.rect(tela, azul, (x_player, y_player, l_player, h_player))
        pygame.draw.circle(tela, azul, (x_player + r_player, y_player - r_player), r_player)
        pygame.draw.rect(tela, vermelho, (x_inimigo, y_inimigo, l_inimigo, h_inimigo))
    elif estado == 'game_over':
        fonte = pygame.font.SysFont(None, 36)
        #texto = fonte.render(f'Pontos: {pontos}', True, (255, 255, 255))
        #tela.blit(texto, (10, 10))
        texto_game_over = fonte.render('GAME OVER', True, (255, 0, 0))
        tela.blit(texto_game_over, (325, 275))
    
    # atualização
    pygame.display.update()

    # travar fps
    clock.tick(60)

