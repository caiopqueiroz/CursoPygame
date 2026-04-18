# estilo candy crush - formar sequências de cores 
# próximo objetivo - criar um gerador de peças: azuis e vermelhas


import pygame
import sys
from rich import inspect


pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Jogo de Combinar')
clock = pygame.time.Clock()
# cores
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
vermelho_transparente = (255, 0, 0, 128)
verde = (0, 255, 0)
verde_transparente = (0, 255, 0, 128)
azul = (0, 0, 255)
# estado
estado = 'jogando'
# peças 
estado_peca = 'padrao'
cor_peca_1 = vermelho
cor_peca_2 = azul
cor_peca_3 = azul
cor_peca_4 = azul
cor_peca_5 = vermelho
cor_peca_6 = vermelho
cor_peca_7 = azul
cor_peca_8 = azul
cor_peca_9 = azul
cor_peca_10 = vermelho
cor_peca_11 = vermelho
cor_peca_12 = azul
cor_peca_13 = azul
cor_peca_14 = azul
cor_peca_15 = vermelho
cor_peca_16 = vermelho
cor_peca_17 = azul
cor_peca_18 = azul
cor_peca_19 = azul
cor_peca_20 = vermelho
cor_peca_21 = vermelho
cor_peca_22 = azul
cor_peca_23 = azul
cor_peca_24 = azul
cor_peca_25 = vermelho
r = 30

x1 = 260
y1 = y2 = y3 = y4 = y5 = 160
x2 = x1 + 70
x3 = x1 + 140
x4 = x1 + 210
x5 = x1 + 280

x6 = 260
y6 = y7 = y8 = y9 = y10 = 230
x7 = x1 + 70
x8 = x1 + 140
x9 = x1 + 210
x10 = x1 + 280

x11 = 260
y11 = y12 = y13 = y14 = y15 = 300
x12 = x1 + 70
x13 = x1 + 140
x14 = x1 + 210
x15 = x1 + 280

x16 = 260
y16 = y17 = y18 = y19 = y20 = 370
x17 = x1 + 70
x18 = x1 + 140
x19 = x1 + 210
x20  = x1 + 280

x21 = 260
y21 = y22 = y23 = y24 = y25 = 440
x22 = x1 + 70
x23 = x1 + 140
x24 = x1 + 210
x25 = x1 + 280

# seletor
cor_seletor = vermelho_transparente
estado_seletor = False
x_seletor = x1 - r - 5
y_seletor = y1 - r - 5

while True:
    # eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # lógica
    if estado == 'jogando':
        teclas = pygame.key.get_pressed()

        # ativando seletor
        if teclas[pygame.K_x]:
            if cor_seletor == vermelho_transparente:
                cor_seletor = verde_transparente
                estado_seletor = True
        
        # movendo o seletor desativado
        pass

        # definindo o estado da peça como 'trocar' caso a tecla seja pressionada
        if teclas[pygame.K_w] and estado_seletor == True:
            estado_peca = 'trocar'
        if teclas[pygame.K_a] and estado_seletor == True:
            estado_peca = 'trocar'
        if teclas[pygame.K_s] and estado_seletor == True:
            estado_peca = 'trocar'
        if teclas[pygame.K_d] and estado_seletor == True:
            estado_peca = 'trocar'
            
        # trocando a cor da primeira peça
        if x_seletor + 5 + r == x1 and y_seletor + 5 + r == y1 and estado_peca == 'trocar':
            cor_anterior = cor_peca_1
            if cor_peca_1 == vermelho:
                cor_peca_1 = azul
            else:
                cor_peca_1 = vermelho
        if x_seletor + 5 + r == x2 and y_seletor + 5 + r == y2 and estado_peca == 'trocar':
            cor_anterior = cor_peca_2
            if cor_peca_2 == vermelho:
                cor_peca_2 = azul
            else:
                cor_peca_2 = vermelho
        if x_seletor + 5 + r == x3 and y_seletor + 5 + r == y3 and estado_peca == 'trocar':
            cor_anterior = cor_peca_3
            if cor_peca_3 == vermelho:
                cor_peca_3 = azul
            else:
                cor_peca_3 = vermelho
        if x_seletor + 5 + r == x4 and y_seletor + 5 + r == y4 and estado_peca == 'trocar':
            cor_anterior = cor_peca_4
            if cor_peca_4 == vermelho:
                cor_peca_4 = azul
            else:
                cor_peca_4 = vermelho

        # movendo o seletor 
        if estado_seletor == True and teclas[pygame.K_w]:
            y_seletor -= 70
            cor_seletor = vermelho_transparente
            estado_seletor = False
        if estado_seletor == True and teclas[pygame.K_a]:
            x_seletor -= 70
            cor_seletor = vermelho_transparente
            estado_seletor = False
        if estado_seletor == True and teclas[pygame.K_s]:
            y_seletor += 70
            cor_seletor = vermelho_transparente
            estado_seletor = False
        if estado_seletor == True and teclas[pygame.K_d]:    
            x_seletor += 70 
            cor_seletor = vermelho_transparente
            estado_seletor = False
        
        # fazendo a outra peça ganhar a cor anterior da peça trocada
        if x_seletor + 5 + r == x1 and y_seletor + 5 + r == y1 and estado_peca == 'trocar':
            cor_peca_1 = cor_anterior
            estado_peca = 'padrao'
        if x_seletor + 5 + r == x2 and y_seletor + 5 + r == y2 and estado_peca == 'trocar':
            cor_peca_2 = cor_anterior
            estado_peca = 'padrao'
        if x_seletor + 5 + r == x3 and y_seletor + 5 + r == y3 and estado_peca == 'trocar':
            cor_peca_3 = cor_anterior
            estado_peca = 'padrao'
        if x_seletor + 5 + r == x4 and y_seletor + 5 + r == y4 and estado_peca == 'trocar':
            cor_peca_4 = cor_anterior
            estado_peca = 'padrao'

    # desenho
    if estado == 'jogando':
        tela.fill(preto)
        
        pygame.draw.circle(tela, cor_peca_1, (x1, y1), r) # peça 1 
        pygame.draw.circle(tela, cor_peca_2, (x2, y2), r) # peça 2
        pygame.draw.circle(tela, cor_peca_3, (x3, y3), r) # peça 3
        pygame.draw.circle(tela, cor_peca_4, (x4, y4), r) # peça 4
        pygame.draw.circle(tela, cor_peca_5, (x5, y5), r) # peça 5
        pygame.draw.circle(tela, cor_peca_6, (x6, y6), r) # peça 1 
        pygame.draw.circle(tela, cor_peca_7, (x7, y7), r) # peça 2
        pygame.draw.circle(tela, cor_peca_8, (x8, y8), r) # peça 3
        pygame.draw.circle(tela, cor_peca_9, (x9, y9), r) # peça 4
        pygame.draw.circle(tela, cor_peca_10, (x10, y10), r) # peça 5
        pygame.draw.circle(tela, cor_peca_11, (x11, y11), r) # peça 1 
        pygame.draw.circle(tela, cor_peca_12, (x12, y12), r) # peça 2
        pygame.draw.circle(tela, cor_peca_13, (x13, y13), r) # peça 3
        pygame.draw.circle(tela, cor_peca_14, (x14, y14), r) # peça 4
        pygame.draw.circle(tela, cor_peca_15, (x15, y15), r) # peça 5
        pygame.draw.circle(tela, cor_peca_16, (x16, y16), r) # peça 1 
        pygame.draw.circle(tela, cor_peca_17, (x17, y17), r) # peça 2
        pygame.draw.circle(tela, cor_peca_18, (x18, y18), r) # peça 3
        pygame.draw.circle(tela, cor_peca_19, (x19, y19), r) # peça 4
        pygame.draw.circle(tela, cor_peca_20, (x20, y20), r) # peça 5
        pygame.draw.circle(tela, cor_peca_21, (x21, y21), r) # peça 1 
        pygame.draw.circle(tela, cor_peca_22, (x22, y22), r) # peça 2
        pygame.draw.circle(tela, cor_peca_23, (x23, y23), r) # peça 3
        pygame.draw.circle(tela, cor_peca_24, (x24, y24), r) # peça 4
        pygame.draw.circle(tela, cor_peca_25, (x25, y25), r) # peça 5
        
        # seletor 
        seletor = pygame.Surface((70, 70), pygame.SRCALPHA)
        seletor.fill(cor_seletor)
        tela.blit(seletor, (x_seletor, y_seletor))

    # atualizações
    pygame.display.update()

    # travar fps
    clock.tick(60)