import math
peso = float(input('Qual é o seu peso ? (em kg) : '))
altura = float(input('Qual a sua altura ? (em m) : '))
iMC = int((peso)/math.pow(altura , 2))
print(f'O seu IMC é de {iMC} ! ')
if iMC < 16:
    print('Voce está com Subpeso Severo!')
elif 16 <= iMC <= 19.9:
    print('Você está com Subpeso! ')
elif 20 <= iMC <= 24.9:
    print('Você está com o peso ideal, parabéns!!')
elif 25 <= iMC <= 29.9:
    print('Você está com Sobrepeso :( ')
elif 30 <= iMC <= 39.9:
    print('Você está Obeso :(( ')
elif iMC >= 40:
    print('Você é um Obeso Mórbido :((( ')