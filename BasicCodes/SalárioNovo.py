nome = input(str('Qual o seu nome ? : '))
salario = int(input(' Qual o valor do seu salário atual (R$)? : '))
aumento = (salario * 15)/100
valor_final = int(salario + aumento)
print(f'{nome}, seu novo salário será de {valor_final} R$')