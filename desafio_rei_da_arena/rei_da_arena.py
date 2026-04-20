import pygame
import sys
from random import randint


pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Rei da Arena')
clock = pygame.time.Clock()
# cores 
preto =  (0, 0, 0)
azul = (0, 0, 255)
vermelho = (255, 0, 0)
amarelo = (255, 255, 0)
branco = (255, 255, 255)
# estado 
estado = 'jogando'
# player
v_player = 5
l_player = 60
h_player = 60
l_espada_player = 30
h_espada_player = 10
x_player = (800 - l_player) // 2
y_player = (600 - h_player) // 2 
# inimigo a
inimigo_a = False
v_inimigo_a = 2
l_inimigo_a = l_player
h_inimigo_a = h_player
# inimigo b
inimigo_b = True
estado_inimigo_b = 'descendo'
v_inimigo_b = 5
l_inimigo_b = l_player
h_inimigo_b = h_player
x_inimigo_b = 100
y_inimigo_b = 100
# reliquias
l_reliquia = 25
h_reliquia = 25
x_reliquia = x_player + 200
y_reliquia = y_player
 
while True:
    # eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_p:
                x_inimigo_a1 = randint(0, 800 - l_inimigo_a)
                y_inimigo_a1 = randint(0, 600 - h_inimigo_a)
                inimigo_a = True
            if evento.key == pygame.K_k and estado_player == 'atacar':
                inimigo_b = False
    
    # lógica
    if estado == 'jogando':
        # defininindo estado do player
        estado_player = 'fugindo'

        # definindo a posição da espada do player
        x_espada_player = x_player + l_player
        y_espada_player = y_player

        # definindo colisões
        colisao_player = pygame.Rect(x_player, y_player, l_player, h_player)
        
        if inimigo_a == True: 
            colisao_inimigo_a1 = pygame.Rect(x_inimigo_a1, y_inimigo_a1, l_inimigo_a, h_inimigo_a)
        
        if inimigo_b == True:
            colisao_inimigo_b = list()
            for contador in range(0, 2):
                colisao_inimigo_b.append(pygame.Rect(x_inimigo_b + (contador * 550), y_inimigo_b, l_inimigo_b, h_inimigo_b))
        
        colisao_reliquias = pygame.Rect(x_reliquia, y_reliquia, l_reliquia, h_reliquia)

        colisao_espada_player = pygame.Rect(x_espada_player, y_espada_player, l_espada_player, h_espada_player)

        # aplicando colisões
        if inimigo_a == True:
            if colisao_player.colliderect(colisao_inimigo_a1):
                print('game over')
        if inimigo_b == True:
            for contador in range(0, 2):
                if colisao_player.colliderect(colisao_inimigo_b[contador]):
                    print('game over')
                if colisao_espada_player.colliderect(colisao_inimigo_b[contador]):
                    estado_player = 'atacar'
        if colisao_player.colliderect(colisao_reliquias):
            x_reliquia = randint(0, 800 - l_reliquia)
            y_reliquia = randint(0, 600 - h_reliquia)
        
        # movendo o player
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

        # movendo o inimigo do tipo a
        if inimigo_a == True:
            if x_inimigo_a1 < x_player:
                x_inimigo_a1 += v_inimigo_a
            else:
                x_inimigo_a1 -= v_inimigo_a
            if y_inimigo_a1 < y_player:
                y_inimigo_a1 += v_inimigo_a
            else:
                y_inimigo_a1 -= v_inimigo_a

        # movendo o inimigo do tipo b
        if inimigo_b == True:
            if estado_inimigo_b == 'descendo':
                y_inimigo_b += v_inimigo_b
                if y_inimigo_b + h_inimigo_b == 500:
                    estado_inimigo_b = 'subindo'
            if estado_inimigo_b == 'subindo':
                y_inimigo_b -= v_inimigo_b
                if y_inimigo_b == 100:
                    estado_inimigo_b = 'descendo'

    # desenho
    if estado == 'jogando':
        tela.fill(preto)
        # desenhando player
        pygame.draw.rect(tela, azul, (x_player, y_player, l_player, h_player))

        # desenhando espada do player
        pygame.draw.rect(tela, branco, (x_espada_player, y_espada_player, l_espada_player, h_espada_player))
        
        # spawn de inimigo do tipo a
        if inimigo_a == True:
            pygame.draw.rect(tela, vermelho, (x_inimigo_a1, y_inimigo_a1, l_inimigo_a, h_inimigo_a))

        # desenhando inimigo do tipo b
        if inimigo_b == True:
            for contador in range(0, 2):
                pygame.draw.rect(tela, vermelho, (x_inimigo_b + (contador * 550), y_inimigo_b, l_inimigo_b, h_inimigo_b))

        # desenhando relíquias
        pygame.draw.rect(tela, amarelo, (x_reliquia, y_reliquia, l_reliquia, h_reliquia))

    # atualizações
    pygame.display.update()

    # travar fps
    clock.tick(60)