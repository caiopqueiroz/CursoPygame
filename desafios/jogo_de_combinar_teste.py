import pygame


pygame.init()
tela = pygame.display.set_mode((800, 600))
y1 = 600 // 2
x1 = 120
r = 30
vermelho = (255, 0, 0)
azul = (0, 0, 255)
cor = vermelho
cor_peca_0 = azul
contador = 0 

while True: 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()

    for contador in range(0, 9):
        pygame.draw.circle(tela, cor, (x1 + 70 * contador, y1), r)
    

    pygame.display.update()