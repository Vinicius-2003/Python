import random

# Cria uma lista
lista_numeros_aleatorios = []

# Criar uma lista com os valores gerados aleatoriamente
for i in range(5):
    numeros_aleatorios = random.randint(1,5)
    lista_numeros_aleatorios.append(numeros_aleatorios)

# Cria uma tupla, e adiciona os valores da lista na tupla
tupla_numeros_aleatorios = (lista_numeros_aleatorios)
print(tupla_numeros_aleatorios)



# Maior valor
for a in range(0,4):
    for b in range (1,5):
        if a >= b:
            maior = int(a)
        elif a <= b:
            maior = int(b)
            
print(maior)