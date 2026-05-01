# conceito: você é um guerreiro preso em uma arena amaldiçoada - quanto mais tempo sobrevive... mais o jogo fica insano 

# objetivos:
# sobreviver o máximo tempo possível
# coletar relíquias
# fugir de inimigos
# virar o 'Rei da Arena Supremo'

# player se move com WASD - tem um sprite - som ao andar e ao agir 
# relíquias tem spawn aleatório - dão pontos - som ao coletar
# 3 tipos de inimigos:
# tipo 1: lento - segue o player
# tipo 2: após X pontos - mais rápido
# tipo 3: movimento aleatório  
# encostar no inimigo: game over - som de morte 
# a cada x pontos: velocidade do inimigo tipo 1 aumenta 
# mostrar pontos na tela durante o jogo
# exibir mensagem quando o a velocidade aumentar
# habilidade slow motion: se o jogador pegar x relíquias em num intervalo de até 3 segundos, aparece um item coletável que deixa os inimigos mais lentos 
# slow motion - descrição detalhada:
# jogador pega 3 relíquias 
# se passarem menos de 3 segundos
# item novo aparece em uma posição aleatória na tela
# quando coletado
# a velocidade todos os inimigos diminui por 10 segundos

# ideias para aprimorar:
# criar um gerador de inimigos que spawna mais a cada soma +x de pontos 


import pygame
import sys
from random import randint
from random import choice


pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Rei da Arena Supremo')
clock = pygame.time.Clock()
# cores
preto = (0, 0, 0)
branco = (255, 255, 255)
cinza = (138, 138, 138)
azul = (0, 0, 255)
amarelo = (255, 255, 0)
vermelho = (255, 0, 0)
roxo = (160, 32, 240)
# estado 
estado = 'jogando'
# fonte 
titulo = pygame.font.SysFont(None, 72)
texto = pygame.font.SysFont(None, 36)
# texto
game_over = titulo.render('GAME OVER', True, branco)
aperte_p = texto.render('Aperte P para reiniciar o jogo', True, branco)
mensagem = ''
mensagem_slow = ''
# player
pontos = 0
pontos_acumulados = 0
pontos_sequencia = 0
v_player = 7
l_player = 60
h_player = 60
x_player = 100
y_player = 100
# reliquia
l_reliquia = 40
h_reliquia = 40
x_reliquia = randint(400, 800 - l_reliquia)
y_reliquia = randint(0, 600 - h_reliquia)
# item slow 
item_slow = False
l_item_slow = 30
h_item_slow = 30
x_item_slow = 800
y_item_slow = 600
# inimigo tipo 1
v_inimigo1 = 2
l_inimigo1 = 60
h_inimigo1 = 60
x_inimigo1 = 700
y_inimigo1 = 500
# inimigo tipo 2
v_inimigo2 = 4
l_inimigo2 = 30
h_inimigo2 = 70
x_inimigo2 = 700
y_inimigo2 = 500
# inimigo tipo 3
v_vertical = 0
v_horizontal = 2
l_inimigo3 = 30
h_inimigo3 = 30
x_inimigo3 = (800 - l_inimigo3) // 2
y_inimigo3 = (600 - h_inimigo3) // 2

contagem_tempo_slow = False

while True:
    # eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_p:
                if estado == 'gameover':
                    estado = 'jogando'
                    x_player = 100
                    y_player = 100
                    x_inimigo1 = 700
                    y_inimigo1 = 500
                    v_inimigo1 = 2
                    x_inimigo3 = (800 - l_inimigo3) // 2
                    y_inimigo3 = (600 - h_inimigo3) // 2
                    pontos = 0
                    pontos_acumulados = 0
                    pontos_sequencia = 0
                    item_slow = False

    # lógica 
    if estado == 'inicio':
        pass

    if estado == 'jogando':
        # atualizando contagem de pontos da tela
        mostrar_pontos = texto.render(f'Pontos: {pontos}', True, azul)

        # aumentando velocidade de acordo com a soma de pontos
        if pontos_acumulados == 15:
            mensagem = 'Velocidade aumentou!'
            # o tempo_mensagem vai se tornar o tempo passado, em milissegundos desde o início do jogo, ou seja, vai receber um único valor que não vai se alterar, exemplo: 4000
            tempo_mensagem = pygame.time.get_ticks()
            v_inimigo1 += 0.5
            pontos_acumulados = 0

        velocidade_aumentou = texto.render(mensagem, True, preto)
        # ocultado mensagem
        if mensagem:
            # quando a mensagem for exibida, o tempo_atual vai receber um valor, exemplo: 4001, mas, esse valor vai aumentar a cada novo frame porque ele estará sendo executado a cada novo frame (4002, 4003, ...)
            tempo_atual = pygame.time.get_ticks()
            # quando a direfença entre o tempo_atual e o tempo_mensagem (que é fixo) for maior que 2000 (2 segundos), a mensagem voltará a ser nula
            if tempo_atual - tempo_mensagem > 2000:
                mensagem = ''

        velocidade_diminuiu = texto.render(mensagem_slow, True, preto)
        if mensagem_slow:
            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - tempo_mensagem_slow > 2000:
                mensagem_slow = ''

        # definindo colisões
        colisao_reliquia = pygame.Rect(x_reliquia, y_reliquia, l_reliquia, h_reliquia)
        colisao_player = pygame.Rect(x_player, y_player, l_player, h_player)
        colisao_inimigo1 = pygame.Rect(x_inimigo1, y_inimigo1, l_inimigo1, h_inimigo1)
        colisao_inimigo3 = pygame.Rect(x_inimigo3, y_inimigo3, l_inimigo3, h_inimigo3)

        # aplicando colisões
        if colisao_player.colliderect(colisao_reliquia):
            # mudando a relíquia de posição 
            if x_player > 400:
                x_reliquia = randint(0, 400 - l_reliquia)
            else:
                x_reliquia = randint(400, 800 - l_reliquia)
            y_reliquia = randint(0, 600 - h_reliquia)
            # somando pontos e pontos acumulados
            pontos += 1
            pontos_acumulados += 1
            pontos_sequencia += 1
            # contando tempo gasto pra pegar a relíquia 1  
            if pontos_sequencia == 1:
                tempo_reliquia1 = pygame.time.get_ticks()
            # contando tempo gasto pra pegar relíquia 3
            if pontos_sequencia == 3:
                tempo_reliquia3 = pygame.time.get_ticks()
                # checando o tempo gasto e exibindo o item de recompensa
                if tempo_reliquia3 - tempo_reliquia1 <= 3000:
                    print('isso, item novo!')
                    item_slow = True 
                    if x_player < 400:
                        x_item_slow = randint(400, 800 - l_item_slow)
                    else:
                        x_item_slow = randint(0, 400 - l_item_slow)
                    y_item_slow = randint(0, 600 - h_item_slow)
                # resetando a sequência
                pontos_sequencia = 0
        
        # checando se já passaram os 10 segundos e retornando à velocidade original
        if contagem_tempo_slow:
            tempo_slow = pygame.time.get_ticks()
            if tempo_slow - tempo_inicio_slow > 10000:
                v_inimigo1 = v_anterior_inimigo1
                if pontos >= 30:
                    v_inimigo2 = 4
                print('inimigos velocidade normal')
                contagem_tempo_slow = False
        if item_slow:
            colisao_item_slow = pygame.Rect(x_item_slow, y_item_slow, l_item_slow, h_item_slow)
            if colisao_player.colliderect(colisao_item_slow):
                mensagem_slow = 'Inimigos mais lentos por 10 segundos!'
                tempo_mensagem_slow = pygame.time.get_ticks()
                v_anterior_inimigo1 = v_inimigo1
                v_inimigo1 = 1
                if pontos >= 30:
                    v_inimigo2 = 1
                # contando os 10 segundos de slow 
                contagem_tempo_slow = True
                tempo_inicio_slow = pygame.time.get_ticks()
                print('inimigos mais lentos')
                item_slow = False

        if colisao_player.colliderect(colisao_inimigo1):
            estado = 'gameover'
        
        if pontos >= 30:
            colisao_inimigo2 = pygame.Rect(x_inimigo2, y_inimigo2, l_inimigo2, h_inimigo2)
            if colisao_player.colliderect(colisao_inimigo2):
                estado = 'gameover'
        
        if colisao_player.colliderect(colisao_inimigo3):
            estado = 'gameover'

        # movimentação do player
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w]:
            y_player -= v_player
        if teclas[pygame.K_a]:
            x_player -= v_player
        if teclas[pygame.K_s]:
            y_player += v_player
        if teclas[pygame.K_d]:
            x_player += v_player

        # movimentação do inimigo tipo 1 
        if x_inimigo1 > x_player:
            x_inimigo1 -= v_inimigo1
        else:
            x_inimigo1 += v_inimigo1
        if y_inimigo1 > y_player:
            y_inimigo1 -= v_inimigo1
        else:
            y_inimigo1 += v_inimigo1

        if pontos >= 30:
            # movimentação do inimigo tipo 2
            if x_inimigo2 > x_player:
                x_inimigo2 -= v_inimigo2 
            else:
                x_inimigo2 += v_inimigo2
            if y_inimigo2 > y_player:
                y_inimigo2 -= v_inimigo2
            else:
                y_inimigo2 += v_inimigo2

        # movimentação do inimigo tipo 3 
        x_inimigo3 += v_horizontal
        y_inimigo3 += v_vertical
        if randint(0, 100) == 0:
            if v_horizontal == 2 or v_horizontal == -2:
                v_horizontal = 0
                v_vertical = choice([-2, 2])
        if randint(0, 100) == 0:
            if v_vertical == 2 or v_vertical == -2:
                v_vertical = 0 
                v_horizontal = choice([-2, 2])

        # impedindo o inimigo 3 de sair da tela
        if x_inimigo3 < 0:
            v_horizontal *= -1
        if x_inimigo3 > 800 - l_inimigo3:
            v_horizontal *= -1
        if y_inimigo3 < 0:
            v_vertical *= -1
        if y_inimigo3 > 600 - h_inimigo3:
            v_vertical *= -1

    # desenho 
    if estado == 'inicio':
        tela.fill(preto)

    if estado == 'jogando':
        tela.fill(cinza)
        # player 
        pygame.draw.rect(tela, azul, (x_player, y_player, h_player, l_player))
        # relíquias
        pygame.draw.rect(tela, amarelo, (x_reliquia, y_reliquia, l_reliquia, h_reliquia))
        # item_slow
        if item_slow: 
            pygame.draw.rect(tela, roxo, (x_item_slow, y_item_slow, l_item_slow, h_item_slow))
        # inimigo tipo 1 
        pygame.draw.rect(tela, vermelho, (x_inimigo1, y_inimigo1, l_inimigo1, h_inimigo1))
        if pontos >= 30:
            # inimigo tipo 2 
            pygame.draw.rect(tela, vermelho, (x_inimigo2, y_inimigo2, l_inimigo2, h_inimigo2))
        # inimigo tipo 3
        pygame.draw.rect(tela, vermelho, (x_inimigo3, y_inimigo3, l_inimigo3, h_inimigo3))
        tela.blit(mostrar_pontos, (50, 50))
        tela.blit(velocidade_aumentou, (480, 50))
        tela.blit(velocidade_diminuiu, (180, 250))

    if estado == 'gameover':
        tela.fill(preto)
        tela.blit(game_over, (100, 100))
        tela.blit(aperte_p, (100, 200))
        tela.blit(mostrar_pontos, (100, 300))

    # atualizações
    pygame.display.update()

    # travar fps
    clock.tick(60)