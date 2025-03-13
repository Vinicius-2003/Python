import pygame
import random

# Configurações da tela
largura = 800
altura  = 600

# Configurações dos círculos
tamanhos = [10, 20, 30]
num_circulos = 3 
cores = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 255, 255)]

class Circulo:
    def __init__(self):
        self.raio = random.choice(tamanhos)
        self.cor = random.choice(cores)
        self.position = pygame.math.Vector2(largura // 2, altura // 2)
        self.vel_x = random.choice([-2, -1, 1, 2])
        self.vel_y = random.choice([-2, -1, 1, 2])
    
    def mover(self):
        self.position.x += self.vel_x
        self.position.y += self.vel_y

        # Colisão com as bordas
        if self.position.x - self.raio <= 0 or self.position.x + self.raio >= largura:
            self.vel_x *= -1
        if self.position.y - self.raio <= 0 or self.position.y + self.raio >= altura:
            self.vel_y *= -1
    
    def desenhar(self, tela):
        pygame.draw.circle(tela, self.cor, (self.position.x, self.position.y), self.raio)

# Inicialização do pygame
pygame.init()
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Círculos Aleatórios")
clock = pygame.time.Clock()

# Criando os círculos
circulos = list()
for i in range(3):
    circulos.append(Circulo())

# Loop principal
rodando = True
while rodando:
    tela.fill((0, 0, 0))  # Preencher fundo preto
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    # Atualizar e desenhar círculos
    for circulo in circulos:
        circulo.mover()
        circulo.desenhar(tela)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
