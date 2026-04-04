# parte 1

# 1 - Game loop é o loop principal do jogo, todos os seus elementos devem estar dentro dele para que funcionem corretamente.
# 2 - 'pygame.draw.rect' desenha um retângulo. 'pygame.draw.circle' desenha um círulo. Vale lembar que ao desenhar um círculo, as coordenadas atribuídas se referem ao seu centro, ao contrário do que acontece no retângulo.
# 3 - Essa é a função que atualiza a tela a cada frame, essencial para que o jogo funcione.
# 4 - É usado para travar o FPS do jogo em um valor fixo. 

# parte 2 e 3

# ex01a04
import pygame
import sys


pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Revisão')
azul = (0, 0, 120)
branco = (255, 255, 255)
laranja = (255, 131, 0)
cinza = (85, 85, 85)
clock = pygame.time.Clock()
# arena
l_arena = 600
h_arena = 400
x_arena = (800 - l_arena) / 2
y_arena = (600 - h_arena) / 2
# retangulo
l_retangulo = 50
h_retangulo = 100
x_retangulo = (400 - l_retangulo) / 2
y_retangulo = (600 - h_retangulo) / 2
# circulo
raio = 50
# player 
l_player = 30
h_player = 60
raio_player = l_player / 2
x_player = (800 - l_player) / 2
y_player = (600 - h_player) / 2
velocidade = 7

while True:
    # eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # lógica
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w]:
        y_player -= velocidade
    if teclas[pygame.K_a]:
        x_player -= velocidade
    if teclas[pygame.K_s]:
        y_player += velocidade
    if teclas[pygame.K_d]:
        x_player += velocidade

    if x_player < x_arena:
        x_player = x_arena
    if x_player > l_arena + x_arena - l_player:
        x_player = l_arena + x_arena - l_player
    if y_player < y_arena:
        y_player = y_arena
    if y_player > y_arena + h_arena - h_player:
        y_player = y_arena + h_arena - h_player


    # desenho
    tela.fill(azul)
    # pygame.draw.rect(tela, cor, (x, y, largura, altura))
    # pygame.draw.circle(tela, cor, (x, y), raio)
    pygame.draw.rect(tela, cinza, (x_arena, y_arena, l_arena, h_arena))
    pygame.draw.rect(tela, branco, (x_retangulo, y_retangulo, l_retangulo, h_retangulo))
    pygame.draw.circle(tela, branco, (600, 300), raio)
    
    pygame.draw.rect(tela, laranja, (x_player, y_player, l_player, h_player))
    pygame.draw.circle(tela, laranja, (x_player + raio_player, y_player - raio_player), raio_player)

    # atualização
    pygame.display.update()

    # travar FPS
    clock.tick(60)