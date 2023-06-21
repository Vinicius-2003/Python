import math
a = int(input('digite um valor para a : '))
b = int(input('digite um valor para b : '))
c = int(input('digite um valor para c : '))
y = (math.pow(a, 2) + math.sqrt(3 * b)) / (5 * math.pow(c, 3))
print(' O resultado da equação será de {:.2f}'.format(y))
