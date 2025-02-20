
import os


tupla = (
    int(input("Insira um valor : ")),
    int(input("Insira um valor : ")),
    int(input("Insira um valor : ")),
    int(input("Insira um valor : "))
    )

os.system('cls')

print(f"Você digitou os valores : {tupla}", end='')

print(f"\nO número 9 apareceu {tupla.count(9)} vez(es)! ")

if 3 in tupla:
    print(f"A primeira vez que o número 3 foi digitado, foi na {tupla.index(3)+1}ª posição ")

print("Os valores pares foram : ", end='')
for num in tupla:
    if num%2 == 0:
        print(num, end=" ")
