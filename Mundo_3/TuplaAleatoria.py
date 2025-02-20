from random import randint
import os


os.system('cls')
tupla = (randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100))

print("Os valores sorteados foram: ", end='')
for n in tupla: 
    print(f" {n} ", end='')
    
print(f"\nO maior valor foi de: {max(tupla)}")
print(f"O menor valor foi de : {min(tupla)}")