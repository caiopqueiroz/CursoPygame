import pygame
import sys
from rich import inspect


class desenharNuvem:
    def __init__(self, circulos=10, inicio=240, altura=100):
        # Atributos de instância 
        self.circulos = circulos
        self.inicio = inicio
        self.altura = altura
        
        if self.circulos % 2 != 0:
            self.circulos += 1
        for contador in range(1, self.circulos):
            pygame.draw.circle(tela, branco, (self.inicio + contador * 20, self.altura if contador % 2 != 0 else self.altura - 30), 30)


# Coordenadas x, y no retângulo se referem sempre ao canto superior esquerdo
# No círculo, se referem ao seu centro 
# pygame.draw.rect(tela, cor, (x, y, largura, altura))
# pygame.draw.circle(tela, cor, (x, y), raio)


pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Aula 2')
clock = pygame.time.Clock()
marrom = (137, 81, 41)
azul_claro = (135, 206, 235)
vermelho = (178, 34, 34)
vermelho_2 = (100, 34, 34)
cinza = (85, 85, 85)
amarelo = (255, 255, 0)
rosa = (255, 85, 85)
rosa_claro = (255, 182, 192)
verde = (34, 139, 34)
verde_claro = (0, 255, 0)
branco = (255, 255, 255)
x_personagem = 150
y_personagem = 330


while True:
    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Lógica

    # Desenho
    tela.fill(azul_claro)
    pygame.draw.rect(tela, verde, (0, 400, 800, 200)) # chão
    pygame.draw.rect(tela, vermelho, (300, 250, 200, 150)) # casa
    pygame.draw.rect(tela, vermelho_2, (300, 175, 200, 75)) # telhado
    pygame.draw.rect(tela, cinza, (375, 300, 50, 100)) # porta
    pygame.draw.rect(tela, azul_claro, (313, 270, 50, 60)) # janela1
    pygame.draw.rect(tela, azul_claro, (436, 270, 50, 60)) # janela2
    pygame.draw.circle(tela, amarelo, (100, 100), 55) # sol

    pygame.draw.rect(tela, rosa, (x_personagem, y_personagem, 30, 70)) # personagem
    pygame.draw.circle(tela, rosa_claro, (x_personagem + 15, y_personagem - 15), 15)

    pygame.draw.rect(tela, marrom, (620, 280, 40, 120)) # árvore
    pygame.draw.circle(tela, verde_claro, (640, 280), 50)
    pygame.draw.circle(tela, verde_claro, (640, 220), 50)
    pygame.draw.circle(tela, verde_claro, (690, 260), 50)
    pygame.draw.circle(tela, verde_claro, (590, 260), 50)
    
    desenharNuvem()
    desenharNuvem(10, 520)
    
    # Atualização
    pygame.display.update()

    # Controle de FPS
    clock.tick(60)
