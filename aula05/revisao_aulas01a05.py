import pygame
import sys


pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Revisão')
clock = pygame.time.Clock()
titulo = pygame.font.SysFont(None, 72)
texto = pygame.font.SysFont(None, 36)
# cores
preto = (0, 0, 0)
branco = (255, 255, 255)
# estado 
estado = 'menu'


while True:
    # eventos
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    # lógica

    # desenho 
    if estado == 'menu':
        tela.fill(branco)
        t1 = titulo.render('ARENA SURVIVAL', True, preto)
        t2 = texto.render('Pressione P para jogar', True, preto)
        tela.blit(texto, (180, 150))
    elif estado == 'jogando':
        tela.fill(preto)
    
    # atualizações
    pygame.display.update()

    # travar fps
    clock.tick(60)