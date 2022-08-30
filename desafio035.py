r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
retas = [r1,r2,r3]
# Maior que 10 > 9 Menor que 9 < 10
if ((r1 + r2) > r3) and ((r2 + r3) > r1) and ((r1 + r3) > r2):
    print('Essas retas {},{},{} podem se tornar um trianglo.'.format(r1,r2,r3))
else:
    print('As retas {},{},{} não podem se tornar um triangulo.'.format(r1,r2,r3))    

