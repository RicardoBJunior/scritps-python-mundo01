n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

s = n1 + n2
sb = n1 - n2
m = n1 * n2
p = n1 ** n2 
d = n1 / n2 

print('A soma é {}, a subtração é {}, a multiplicação é {}'.format(s,sb,m), end='')

print (' A potencia é {}, a divisão é {:.2f}.'.format(p,d))