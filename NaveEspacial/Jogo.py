import os
import random

class NaveEspacial:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.position = (0, 0)  # Posição inicial
        self.direction = 0  # Direção inicial (0 graus)
        self.speed = 0  # Velocidade inicial
        self.shield = 100  # Nível de escudo inicial
        self.energy = 100  # Energia inicial


    def move(self):
        # Implementação para mover a nave
        print(f"{self.name} está se movendo para a frente.")

    def turn(self, direction):
        # Implementação para girar a nave
        if direction.lower() == 'esquerda':
            self.direction -= 90  # Exemplo de rotação
        elif direction.lower() == 'direita':
            self.direction += 90
        print(f"{self.name} virou para a {direction}.")

    def shoot(self):
        # Implementação para lançar um projétil
        if self.energy >= 10:
            self.energy -= 10  # Custo de energia para atirar
            print(f"{self.name} lançou um projétil.")
        else:
            print(f"{self.name} não tem energia suficiente para atirar.")

    def hit(self, damage):
        # Implementação para quando a nave é atingida
        self.shield -= damage
        if self.shield <= 0:
            self.alive = False
            print(f"{self.name} foi destruída.")
        else:
            print(f"{self.name} foi atingida! Escudo restante: {self.shield}")

    def recharge(self,name):
        # Implementação para recarregar energia
        self.energy = 100
        print(f"{self.name} recarregou sua energia.")

                

    def randomRecharge(self):
        energy = random.randint(1,101)
        print(f"{self.name} recebeu {energy} de energia ")
        self.energy = energy
            

    
            
        
# Exemplo de uso

nave1 = NaveEspacial("Falcon")
nave2 = NaveEspacial("Águia")

nave1.move()
nave2.turn("esquerda")

nave1.shoot()
nave2.hit(20)

randomPlayer = random.randint(1,2)

if randomPlayer == 1:
    nave1.randomRecharge()
elif randomPlayer == 2:
    nave2.randomRecharge()

nave2.shoot()
nave1.hit(10)

nave1.shoot()
nave2.hit(3)
