# jogo simples de loop que se passa em um único cenário - a sala de aula

# a professora te faz uma pergunta: o que significa a sigla PIB? 


import pygame
import sys


pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Farming Aura Simulator')
clock = pygame.time.Clock()
# cores 
preto = (0, 0, 0)
branco = (255, 255, 255)
cinza = (211, 211, 211)
marrom = (105, 38, 14)
azul = (68, 93, 194)
verde_escuro = (9, 41, 5)
# estados
estado = 'jogando'
# fonte
titulo = pygame.font.SysFont(None, 72)
texto = pygame.font.SysFont(None, 36)

# professora
l_professora = 30
h_professora = 90
x_professora = 500
y_professora = 100

# alunos
l_alunos = 30
h_alunos = 30
x_alunos = 75
y_alunos = 300

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
        pass
    if estado == 'jogando':
        # Adicionando cor ao chão da sala de aula 
        tela.fill(cinza)
        # Quadro
        pygame.draw.rect(tela, verde_escuro, (250, 10, 300, 100))
        # Professora
        pygame.draw.rect(tela, marrom, (x_professora, y_professora, l_professora, h_professora))
        # Alunos 
        for posicao_vertical in range(0, 3):
            for posicao_horizontal in range(0, 5):
                pygame.draw.rect(tela, azul, (x_alunos + 150 * posicao_horizontal, y_alunos + 100 * posicao_vertical, l_alunos, h_alunos))
        # Exibindo pergunta da professora
        frase = 'O que significa a sigla PIB?'
        mensagem = texto.render(frase, True, preto)
        tela.blit(mensagem, (100, 150))

    # atualizações
    pygame.display.update()

    # travar fps
    clock.tick(60)
