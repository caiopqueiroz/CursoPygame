import pygame
import sys


pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Puzzle de Gravidade')
clock = pygame.time.Clock()
# cores
preto = (0, 0, 0)
vermelho = (255, 0, 0)
azul = (0, 0, 255)
# estado
estado = 'jogando'
# player
r_player = 20
x_player = 800 // 2
y_player = 600 // 2
# gravidade
gravidade = 7

while True:
    # eventos 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # lógica
    if estado == 'jogando':
        teclas = pygame.key.get_pressed()
        if y_player < 530:
                y_player += gravidade
        if teclas[pygame.K_a]:
             x_player -= gravidade

    # desenho
    if estado == 'jogando':
        tela.fill(preto)
        # paredes
        pygame.draw.rect(tela, vermelho, (0, 550, 800, 50))
        pygame.draw.rect(tela, vermelho, (0, 0, 50, 550))
        pygame.draw.rect(tela, vermelho, (50, 0, 750, 50))
        pygame.draw.rect(tela, vermelho, (750, 50, 50, 200))
        pygame.draw.rect(tela, vermelho, (750, 350, 50, 200))
        # player
        pygame.draw.circle(tela, azul, (x_player, y_player), r_player)
    
    # atualizações
    pygame.display.update()

    # travar fps
    clock.tick(60)
