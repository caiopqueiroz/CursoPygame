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
r = 30
x1 = 800 // 2
y1 = 600 // 2
x2 = x1
y2 = y1 - 2 * r - 10
x3 = x1
y3 = y1 + 2 * r + 10 
x4 = x1 + 2 * r + 10
y4 = y1
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
            #if cor_seletor == verde_transparente:
            #   cor_seletor = vermelho_transparente
        
        # movendo o seletor desativado
        

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
        
        # seletor 
        seletor = pygame.Surface((70, 70), pygame.SRCALPHA)
        seletor.fill(cor_seletor)
        tela.blit(seletor, (x_seletor, y_seletor))

    # atualizações
    pygame.display.update()

    # travar fps
    clock.tick(60)