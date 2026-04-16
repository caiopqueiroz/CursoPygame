# estilo candy crush - formar sequências de cores 


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
estado_peca = 'inicial'
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

        # movendo o seletor se ele estiver ativo
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
        if teclas[pygame.K_d]:
            cor_peca = 'alterada'

            if estado_seletor == True:
                x_seletor += 70 
                cor_seletor = vermelho_transparente
                estado_seletor = False

    # desenho
    if estado == 'jogando':
        tela.fill(preto)
        
        if x_seletor + 5 + r == x1 and y_seletor + 5 + r == y1 and cor_peca == 'alterada':
            pygame.draw.circle(tela, azul, (x1, y1), r)
        else:
            pygame.draw.circle(tela, vermelho, (x1, y1), r)
        
        pygame.draw.circle(tela, azul, (x2, y2), r) # peça 2
        pygame.draw.circle(tela, azul, (x3, y3), r) # peça 3
        pygame.draw.circle(tela, azul, (x4, y4), r) # peça 4
        
        # seletor 
        seletor = pygame.Surface((70, 70), pygame.SRCALPHA)
        seletor.fill(cor_seletor)
        tela.blit(seletor, (x_seletor, y_seletor))

    # atualizações
    pygame.display.update()

    # travar fps
    clock.tick(60)