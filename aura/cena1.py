# personagem acordando no quarto 


import pygame
import sys


pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Farming Aura Simulator')
clock = pygame.time.Clock()
# cores 
preto = (0, 0, 0)
branco = (255, 255, 255)
# estados
estado = 'inicio'
# fonte
titulo = pygame.font.SysFont(None, 72)
texto = pygame.font.SysFont(None, 36)
# texto 
frase = ''

while True:
    # eventos 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # lógica 
    if estado == 'inicio':
        pass

    # desenho
    if estado == 'inicio':
        # exibindo tela inicial 
        tela.fill(preto)
        frase = 'Farming Aura Simulator'
        mensagem = titulo.render(frase, True, branco)
        tela.blit(mensagem, (100, 100))
        frase = 'Aperte P para começar'
        mensagem = texto.render(frase, True, branco)
        tela.blit(mensagem, (100, 200))

    # atualizações
    pygame.display.update()

    # travar fps
    clock.tick(60)
