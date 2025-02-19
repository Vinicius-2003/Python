import os

# Pedir para o usuário um número entre 0 e 20
numeros_por_extenso = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", 
    "dezoito", "dezenove", "vinte"
)
os.system('cls')
while (True):
    numero = int(input("Entre um valor entre 0 e 20 : "))
    
    #Verificar se o número está dentro do range
    if numero > 20 or numero < 0:
        print("Valor fora do range! Tente novamente")
    else:
        #Procurar o número na tupla
        for num in range(len(numeros_por_extenso)):
            if num == numero:
                #Retornar o número inputado de forma extensa
                print(f"O número selecionado por escrito foi {numeros_por_extenso[num].title()}!")
        break
