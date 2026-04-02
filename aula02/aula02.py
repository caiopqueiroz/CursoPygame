import pygame
import sys
from rich import inspect


pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Aula 2')
clock = pygame.time.Clock()
inspect(pygame.draw.circle)

while True:
    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Lógica

    # Desenho
    tela.fill((135, 206, 235))
    pygame.draw.rect(tela, (34, 139, 34), (0, 400, 800, 200)) # chão
    pygame.draw.rect(tela, (178, 34, 34), (300, 250, 200, 150)) # casa
    pygame.draw.rect(tela, (100, 34, 34), (300, 175, 200, 75)) # telhado
    pygame.draw.rect(tela, (85, 85, 85), (375, 320, 50, 80)) # porta

    # Atualização
    pygame.display.update()

    # Controle de FPS
    clock.tick(60)
