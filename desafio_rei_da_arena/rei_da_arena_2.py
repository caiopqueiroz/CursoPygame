# tela de início: aperte a tecla 'p' para jogar 
# jogo inicia: inimigo vai na sua direção
# wasd move o jogador: aperte 'o' quando a arma estiver tocando o inimigo para matá-lo
# quando um inimigo é morto: outro aparece em uma posição aleatória
# quando o jogador tocar uma relíquia: outra aparece em uma posição aleatória e 1 ponto é somado 
# quando o jogador atingir 10 pontos: -
# o jogador não pode sair da tela 
# se o inimigo tocar o jogador: game over  

# ideia: júlia deve tirar foto dos papéis chatos no cartório e conseguir comer os docinhos 

# problemas: inimigo nascendo em cima do player
# falta botão de restart


import pygame
import sys
from random import randint


pygame.init()
pygame.mixer.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('25 do 4')
clock = pygame.time.Clock()
# cores
preto = (0, 0, 0)
branco = (255, 255, 255)
cinza = (138, 138, 138)
azul = (0, 0, 255)
vermelho = (255, 0, 0)
vermelho_escuro = (139, 0, 0)
amarelo = (255, 255, 0)
marrom = (101, 67, 33)
# estado 
estado = 'inicio'
# fontes
titulo = pygame.font.SysFont(None, 72)
texto = pygame.font.SysFont(None, 36)
# efeitos sonoros
som_morte = pygame.mixer.Sound('desafio_rei_da_arena/sons/morte.wav')
som_dano = pygame.mixer.Sound('desafio_rei_da_arena/sons/inimigo.wav')
som_item = pygame.mixer.Sound('desafio_rei_da_arena/sons/item.wav')
# música
pygame.mixer.music.load('desafio_rei_da_arena/sons/beyond_journey.mp3')
# tocando música
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)
# textos
nome = titulo.render('Feliz mesversário!', True, branco)
sabe_aqueles = texto.render('Sabe aqueles dias infernais no cartório em que você', True, branco)
voce_gostaria = texto.render('gostaria de ter uma arma branca pra eliminar todos', True, branco)
todos_os_papeis = texto.render('os papéis malvados enquanto come vários docinhos?', True, branco)
agora_voce = texto.render('Agora você pode ter essa experiência, amor!', True, branco)
aperte_o = texto.render('Use "WASD" para se mover e aperte "O" para derrotar', True, branco)
os_inimigos = texto.render('os inimigos que estiverem no alcance da espada', True, branco)
essa_nao = texto.render('Essa não! O trabalho te pegou!', True, branco)
mas_voce = texto.render('Mas você não pode desistir dos docinhos, tente de novo!', True, branco)
aperte_p = texto.render('Aperte "P" para jogar', True, branco)
game_over = titulo.render('Game Over', True, branco)
# player 
estado_player = 'direita'
v_player = 7
l_player = 60
h_player = 60
x_player = (800 - l_player) // 2
y_player = (600 - h_player) // 2
player_imagem = pygame.image.load('desafio_rei_da_arena/julia.png').convert_alpha()
player_imagem = pygame.transform.scale(player_imagem, (60, 60))
# espada do player
estado_espada = 'direita'
l_espada_player = 60
h_espada_player = 10 
x_espada_player = x_player + 2/3 * l_player
y_espada_player = y_player + 3/4 * h_player
espada_player_imagem = pygame.image.load('desafio_rei_da_arena/espada.png')
espada_player_imagem = pygame.transform.scale(espada_player_imagem, (60, 10))
# inimigo
v_inimigo = 2
l_inimigo = l_player
h_inimigo = h_player
x_inimigo = 700
y_inimigo = 500
inimigo_imagem = pygame.image.load('desafio_rei_da_arena/papel.png')
inimigo_imagem = pygame.transform.scale(inimigo_imagem, (60, 60))
# reliquia 
l_reliquia = 60
h_reliquia = 60
x_reliquia = randint(0, 800 - l_reliquia)
y_reliquia = randint(0, 600 - h_reliquia)
reliquia_imagem = pygame.image.load('desafio_rei_da_arena/donut.png')
reliquia_imagem = pygame.transform.scale(reliquia_imagem, (60, 60))
# pontos 
pontos = 0

while True:
    # eventos 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_p:
                if estado == 'inicio':
                    estado = 'jogando'
                if estado == 'gameover':
                    x_inimigo = 700
                    y_inimigo = 500
                    x_player = (800 - l_player) // 2
                    y_player = (600 - h_player) // 2
                    pontos = 0 
                    estado = 'jogando'
            if evento.key == pygame.K_o:
                if colisao_espada_player.colliderect(colisao_inimigo):
                    som_dano.play() 
                    if x_player > 400:
                        x_inimigo = randint(0, 400 - l_inimigo)
                    else:
                        x_inimigo = randint(400, 800 - l_inimigo)
                    y_inimigo = randint(0, 600 - h_inimigo)
            # mudando a direção da espada de acordo com a direção do player
            if evento.key == pygame.K_a:
                if estado_espada == 'direita':
                    espada_player_imagem = pygame.transform.flip(espada_player_imagem, True, False) 
                    estado_espada = 'esquerda'
                if estado_player == 'direita':
                    player_imagem = pygame.transform.flip(player_imagem, True, False)
                    estado_player = 'esquerda'
            if evento.key == pygame.K_d:
                if estado_espada == 'esquerda':
                    espada_player_imagem = pygame.transform.flip(espada_player_imagem, True, False)
                    estado_espada = 'direita'
                if estado_player == 'esquerda':
                    player_imagem = pygame.transform.flip(player_imagem, True, False)
                    estado_player = 'direita'

    # lógica
    if estado == 'inicio':
        pass 
    
    if estado == 'jogando':
        # aumentando velocidade do inimigo 
        if pontos < 10:
            v_inimigo = 2
        if pontos >= 10:
            v_inimigo = 3
        if pontos >= 30:
            v_inimigo = 4

        # definindo colisões
        colisao_player = pygame.Rect(x_player, y_player, l_player, h_player)
        colisao_espada_player = pygame.Rect(x_espada_player, y_espada_player, l_espada_player, h_espada_player)
        colisao_inimigo = pygame.Rect(x_inimigo, y_inimigo, l_inimigo, h_inimigo)
        colisao_reliquia = pygame.Rect(x_reliquia, y_reliquia, l_reliquia, h_reliquia)

        # aplicando colisões
        if colisao_player.colliderect(colisao_reliquia):
            som_item.play()
            if x_player > 400:
                x_reliquia = randint(0, 400 - l_reliquia)
            else: 
                x_reliquia = randint(400, 800 - l_reliquia)
            y_reliquia = randint(0, 600 - h_reliquia)
            pontos += 1
        if colisao_inimigo.colliderect(colisao_player):
            som_morte.play()
            estado = 'gameover'

        # movimentação do inimigo
        if x_inimigo < x_player:
            x_inimigo += v_inimigo
        else:
            x_inimigo -= v_inimigo 
        if y_inimigo < y_player:
            y_inimigo += v_inimigo
        else:
            y_inimigo -= v_inimigo

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

        # movimentação da espada do player
        if estado_espada == 'direita':
            x_espada_player = x_player + 2/3 * l_player
        else:
            x_espada_player = x_player - 2/3 * l_player
        y_espada_player = y_player + 3/4 * h_player

        # impedindo o player de sair da tela 
        if x_player < 0:
            x_player = 0
        if y_player < 0:
            y_player = 0
        if x_player > 800 - l_player:
            x_player = 800 - l_player
        if y_player > 600 - h_player:
            y_player = 600 - h_player 

    # desenho
    if estado == 'inicio':
        tela.fill(vermelho_escuro)
        tela.blit(nome, (50, 50))
        tela.blit(sabe_aqueles, (50, 150))
        tela.blit(voce_gostaria, (50, 200))
        tela.blit(todos_os_papeis, (50, 250))
        tela.blit(agora_voce, (50, 300))
        tela.blit(aperte_o, (50, 400))
        tela.blit(os_inimigos, (50, 450))
        tela.blit(aperte_p, (50, 500))

    if estado == 'jogando':
        tela.fill(marrom)
        # relíquia 
        tela.blit(reliquia_imagem, (x_reliquia, y_reliquia))
        # player
        tela.blit(player_imagem, (x_player, y_player))
        tela.blit(espada_player_imagem, (x_espada_player, y_espada_player))
        # inimigo 
        tela.blit(inimigo_imagem, (x_inimigo, y_inimigo))
        # criando e exibindo contagem de pontos
        contagem_pontos = texto.render(f'Pontos: {pontos}', True, preto)
        tela.blit(contagem_pontos, (50, 50))

    if estado == 'gameover':
        tela.fill(vermelho_escuro)
        tela.blit(game_over, (50, 100))
        # criando e exibindo contagem de pontos na cor branca
        contagem_pontos = texto.render(f'Pontos: {pontos}', True, branco)
        tela.blit(contagem_pontos, (50, 200))
        tela.blit(essa_nao, (50, 300))
        tela.blit(mas_voce, (50, 350))
        tela.blit(aperte_p, (50, 450))

    # atualizações
    pygame.display.update()

    # travar fps
    clock.tick(60)

