import math
co = float(input('Digite o valor do cateto oposto '))
ca = float(input('Digite o valor do cateto adjacente '))
h1 = math.hypot(co,ca)

print('Cateto oposto: {} Cateto adjacente {} Hipotenusa {:.2f}'.format(co,ca,h1))