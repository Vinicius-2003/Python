import pygame
import random
from pygame.locals import *

# Inicializa os módulos do pygame
pygame.init()

screen_width = 800  # Largura da tela do jogo
screen_height = 600  # Altura da tela do jogo
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jogo da Nave Espacial")


class Tiro(pygame.sprite.Sprite):
    def __init__(self, position):
        super(Tiro, self).__init__()
        self.image = pygame.Surface((10, 20))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.speed = 15

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()


class naveEspacial(pygame.sprite.Sprite):
    def __init__(self, name):
        super(naveEspacial, self).__init__()
        self.name = name
        self.alive = True
        self.position = pygame.math.Vector2(
            screen_width // 2, screen_height // 2)
        self.direction = 0
        self.speed = 5
        self.max_speed = 20
        self.default_speed = 5
        self.image = pygame.image.load("nave.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_n] and self.speed <= self.max_speed:
            self.speed += 1
        if keys[K_m] and self.speed != self.default_speed:
            self.speed -= 1
        if keys[K_LEFT]:
            self.position.x -= self.speed
        if keys[K_RIGHT]:
            self.position.x += self.speed
        if keys[K_UP]:
            self.position.y -= self.speed
        if keys[K_DOWN]:
            self.position.y += self.speed

        # Impede que a nave saia da tela
        self.position.x = max(0, min(screen_width, self.position.x))
        self.position.y = max(0, min(screen_height, self.position.y))

        self.rect.center = self.position

    def shoot(self):
        tiro = Tiro(self.rect.center)
        return tiro


class Asteroide:
    def __init__(self):
        self.raio = random.randint(10, 40)
        self.position = pygame.math.Vector2(random.randint(
            0, screen_width), random.randint(0, screen_height))
        self.vel_x = random.choice([-3, -2, -1, 1, 2, 3])
        self.vel_y = random.choice([-3, -2, -1, 1, 2, 3])
        self.cor = (150, 150, 150)  # Cinza

    def mover(self):
        self.position.x += self.vel_x
        self.position.y += self.vel_y
        if self.position.x - self.raio <= 0 or self.position.x + self.raio >= screen_width:
            self.vel_x *= -1
        if self.position.y - self.raio <= 0 or self.position.y + self.raio >= screen_height:
            self.vel_y *= -1

    def desenhar(self, tela):
        pygame.draw.circle(tela, self.cor, (int(
            self.position.x), int(self.position.y)), self.raio)


def main():
    nave = naveEspacial("Falcon")
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    all_sprites.add(nave)
    clock = pygame.time.Clock()

    # Criando 8 asteroides aleatórios
    asteroides = list()
    for i in range(8):
        asteroides.append(Asteroide())

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    bullet = nave.shoot()
                    all_sprites.add(bullet)
                    bullets.add(bullet)

        screen.fill((0, 0, 0))
        for asteroide in asteroides:
            asteroide.mover()
            asteroide.desenhar(screen)

        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
