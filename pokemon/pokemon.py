import pygame 
import sys


pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pokemon')
clock = pygame.time.Clock()
estado = 'batalha'

# cores
preto = (0, 0, 0)
branco = (255, 255, 255)
azul = (0, 0, 255)

# fonte
fonte = pygame.font.SysFont(None, 72)

# texto das ações 
atacar = fonte.render('Atacar', True, preto)

# painel 
x_painel = 50
y_painel = 400
l_painel = 700
h_painel = 150

# seletor
x_seletor = 75
y_seletor = 425
l_seletor = 210

# pokemon
x_pokemon = 150
y_pokemon = 150

while True:
    # eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # movimentando o seletor 
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_d:
                x_seletor += l_seletor
            if evento.key == pygame.K_a:
                x_seletor -= l_seletor

    # lógica

    # desenho
    if estado == 'batalha':
        tela.fill(preto)

        # desenhando o pokemon do jogador 
        pygame.draw.rect(tela, azul, (x_pokemon, y_pokemon, 200, 400))

        # desenhando o painel de ações
        pygame.draw.rect(tela, branco, (x_painel, y_painel, l_painel, h_painel))

        # desenhando o texto da ação 'atacar'
        tela.blit(atacar, (100, 450))

        # desenhando um seletor para as ações 
        pygame.draw.rect(tela, preto, (x_seletor, y_seletor, l_seletor, 100), 5)

    # atualizações
    pygame.display.update()

    # travar fps
    clock.tick(60)