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
branco = (255, 255, 255)
# estado
estado = 'jogando'
# player
r_player = 20
x_player = 800 // 2
y_player = 600 // 2
# gravidade
gravidade = 10
sentido_gravidade = 'baixo'

while True:
    # eventos 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # lógica
    if estado == 'jogando':
        # definindo x e y anteriores do player
        x_anterior_player = x_player
        y_anterior_player = y_player
        
        # mudando a direção da gravidade de acordo com a tecla pressionada 
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w] and acao_player == 'parado':
            sentido_gravidade = 'cima'
        if teclas[pygame.K_a] and acao_player == 'parado':
            sentido_gravidade = 'esquerda'
        if teclas[pygame.K_s] and acao_player == 'parado':
            sentido_gravidade = 'baixo'
        if teclas[pygame.K_d] and acao_player == 'parado':
            sentido_gravidade = 'direita'
        
        # direcionando o player de acordo com a gravidade
        if sentido_gravidade == 'cima':
            y_player -= gravidade
            acao_player = 'movendo'
        if sentido_gravidade == 'esquerda':
            x_player -= gravidade
            acao_player = 'movendo'
        if sentido_gravidade == 'baixo':
            y_player += gravidade
            acao_player = 'movendo'
        if sentido_gravidade == 'direita':
            x_player += gravidade
            acao_player = 'movendo'

        # impedindo o player de atravessar as paredes
        if y_player > 530:
            y_player = 530
            acao_player = 'parado'
        if x_player < 70:
            x_player = 70
            acao_player = 'parado'
        if y_player < 70:
            y_player = 70
            acao_player = 'parado'

        # definindo colisões
        bloco1 = pygame.Rect(700, 500, 50, 50)
        bloco2 = pygame.Rect(650, 50, 50, 50)
        bloco3 = pygame.Rect(200, 100, 50, 50)
        bloco4 = pygame.Rect(50, 150, 50, 50)
        bloco5 = pygame.Rect(150, 300, 50, 50)
        parede_direita_cima = pygame.Rect(750, 50, 50, 200)
        parede_direita_baixo = pygame.Rect(750, 350, 50, 200)
        player = pygame.Rect(x_player - r_player, y_player - r_player, 2 * r_player, 2 * r_player)

        # aplicando colisões
        if bloco1.colliderect(player):
            x_player = x_anterior_player
            y_player = y_anterior_player
            acao_player = 'parado'
        if bloco2.colliderect(player):
            x_player = x_anterior_player
            y_player = y_anterior_player
            acao_player = 'parado'
        if bloco3.colliderect(player):
            x_player = x_anterior_player
            y_player = y_anterior_player
            acao_player = 'parado'
        if bloco4.colliderect(player):
            x_player = x_anterior_player
            y_player = y_anterior_player
            acao_player = 'parado'
        if bloco5.colliderect(player):
            x_player = x_anterior_player
            y_player = y_anterior_player
            acao_player = 'parado'
        if parede_direita_cima.colliderect(player):
            x_player = x_anterior_player
            y_player = y_anterior_player
            acao_player = 'parado'
        if parede_direita_baixo.colliderect(player):
            x_player = x_anterior_player
            y_player = y_anterior_player
            acao_player = 'parado'

        if x_player > 820:
            estado = 'vitoria'
        
    # desenho
    if estado == 'jogando':
        tela.fill(preto)
        # paredes
        pygame.draw.rect(tela, vermelho, (0, 550, 800, 50))
        pygame.draw.rect(tela, vermelho, (0, 0, 50, 550))
        pygame.draw.rect(tela, vermelho, (50, 0, 750, 50))
        pygame.draw.rect(tela, vermelho, (750, 50, 50, 200))
        pygame.draw.rect(tela, vermelho, (750, 350, 50, 200))
        # blocos 
        pygame.draw.rect(tela, vermelho, (700, 500, 50, 50))
        pygame.draw.rect(tela, vermelho, (650, 50, 50, 50))
        pygame.draw.rect(tela, vermelho, (200, 100, 50, 50))
        pygame.draw.rect(tela, vermelho, (50, 150, 50, 50))
        pygame.draw.rect(tela, vermelho, (150, 300, 50, 50))
        # player
        pygame.draw.circle(tela, azul, (x_player, y_player), r_player)
    if estado == 'vitoria':
        tela.fill(preto)
        titulo = pygame.font.SysFont(None, 56)
        t1 = titulo.render('Parabéns! Você completou o desafio!', True, branco)
        tela.blit(t1, (55, 250))
    
    # atualizações
    pygame.display.update()

    # travar fps
    clock.tick(60)
