import pygame 
import sys


pygame.init() # Iniciando a biblioteca 
largura, altura = 800, 600 # Definindo largura e altura da janela do jogo
tela = pygame.display.set_mode((largura, altura)) # Definindo a variável tela, para controlar o que aparece nela
clock = pygame.time.Clock()
pygame.display.set_caption('Meu Primeiro Jogo') # Definindo nome da janela
while True: # Loop principal, tudo aqui se repete constantemente até que a janela seja fechada 
    for evento in pygame.event.get(): # Controla os eventos criados, o loop sempre passa por cada um deles repetidas vezes, assim, quando as condições são satisfeitas, eles são executados
        if evento.type == pygame.QUIT: # Se o evento for 'fechar a janela do jogo'
            pygame.quit() # Pygame é encerrado
            sys.exit()
    tela.fill((0, 0, 0)) # Enquanto estivermos no loop principal, a tela será 'limpada' a cada frame
    clock.tick(60)
    pygame.draw.rect(tela, (255, 255, 255), (100, 100, 100, 50)) # Desenha um retângulo
    pygame.display.update() # Mecanismo que atualiza sem parar, essencial para que as informações apareçam na tela 


