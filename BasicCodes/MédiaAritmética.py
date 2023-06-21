p1 = float(input(' Quanto você tirou na primeira prova? : '))
p2 = float(input(' Quanto foi a sua nota na 2ª prova? : '))
med = (p1 + p2)/2
print("A sua média do semestre foi : {:.1f}".format(med))
if med >= 6:
    print('='*10,'Você está acima da média! ' , '='*10)
elif med < 6:
    print('='*10, 'Você não está aprovado', '='*10)
