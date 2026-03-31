import pygame
import sys


pygame.init()
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Aula 1')
clock = pygame.time.Clock()
ultimo_tempo = 0
cor_branco = (255, 255, 255)
cor_preto = (0, 0, 0)
cor = (0, 0, 0)


# Loop principal
while True: 
    # 1) Eventos (captura tudo que o jogador faz, pressionar uma tecla, por exemplo)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2) Lógica 
    # Trocando a cor da tela a cada 1 segundo
    tempo_atual = pygame.time.get_ticks() # Essa função mede o tempo decorrido desde que o pygame foi iniciado
    if tempo_atual - ultimo_tempo > 1000: # Se já tiverem passados 1000 milissegundos
        if cor == cor_preto: # Se a cor da tela for preta
            cor = cor_branco # Ela passará a ser branca
        else: # Caso for branca
            cor = cor_preto # Passará a ser preta
        ultimo_tempo = tempo_atual # O último tempo passa a ser o tempo atual, permitindo assim que esse loop não pare 

    # 3) Desenho
    tela.fill(cor) # Importante ser o primeiro desenho, pois vai sempre limpar a tela antes de desenhar de novo
    pygame.draw.rect(tela, (85, 85, 85), (350, 250, 200, 200)) # Parâmetros (em ordem): onde será desenhado, cor, posição-tamanho 

    # 4) Atualização
    pygame.display.update()

    # 5) Controle de FPS
    clock.tick(60) 