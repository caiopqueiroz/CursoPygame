import pygame 
import sys


pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pokemon')
clock = pygame.time.Clock()
estado = 'batalha'

# estado do seletor
estado_seletor = 'principal'

# cores
preto = (0, 0, 0)
branco = (255, 255, 255)
azul = (0, 0, 255)
vermelho = (255, 0, 0)

# fonte
fonte = pygame.font.SysFont(None, 72)

# formatação dos textos 
largura_maxima = 154
altura_fixa = 49

# texto das ações 
atacar = fonte.render('Atacar', True, preto)
fugir = fonte.render('Fugir', True, preto)
arranhao = fonte.render('Arranhão', True, preto)
# adaptando o texto 'arranhão' para a largura máxima do seletor
arranhao = pygame.transform.scale(arranhao, (largura_maxima, altura_fixa))

# painel 
x_painel = 50
y_painel = 400
l_painel = 700
h_painel = 150

# seletor
x_seletor = x_original_seletor = 75
y_seletor = y_original_seletor = 425
l_seletor = 210

# pokemon
x_pokemon = 150
y_pokemon = 150

# inimigo
x_inimigo = 550
y_inimigo = 50

while True:
    # eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # movimentando o seletor 
        if evento.type == pygame.KEYDOWN:
            # movendo o seletor para a direita
            if evento.key == pygame.K_d:
                x_seletor += l_seletor
            
            # movendo o seletor para a esquerda 
            if evento.key == pygame.K_a:
                x_seletor -= l_seletor
            
            # trocando o estado do seletor
            if evento.key == pygame.K_p:
                if x_seletor == x_original_seletor:
                    estado_seletor = 'atacar'
                
                if x_seletor == x_original_seletor:
                    if estado_seletor == 'atacar':
                        pass
            
            # trocando o estado do seletor
            if evento.key == pygame.K_o:
                if estado_seletor == 'atacar':
                    estado_seletor = 'principal'

    # lógica

    # desenho
    if estado == 'batalha':
        tela.fill(preto)

        # desenhando o pokemon do jogador 
        pygame.draw.rect(tela, azul, (x_pokemon, y_pokemon, 200, 400))

        # desenhando o pokemon inimigo 
        pygame.draw.rect(tela, vermelho, (x_inimigo, y_inimigo, 100, 200))

        # desenhando o painel de ações
        pygame.draw.rect(tela, branco, (x_painel, y_painel, l_painel, h_painel))

        # forma do seletor no estado principal 
        if estado_seletor == 'principal':
            # desenhando o texto da ação 'atacar'
            tela.blit(atacar, (100, 450))

            # desenhando o texto da ação 'fugir'
            tela.blit(fugir, (325, 450))

        # forma do seletor no estado atacar
        if estado_seletor == 'atacar':
            # desenhando o texto do ataque 'arranhão'
            tela.blit(arranhao, (100, 450))

        # desenhando um seletor para as ações 
        pygame.draw.rect(tela, preto, (x_seletor, y_seletor, l_seletor, 100), 5)

    # atualizações
    pygame.display.update()

    # travar fps
    clock.tick(60)