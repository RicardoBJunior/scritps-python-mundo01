from math import floor
#crie um programa que leia um numero real qualquer pelo teclado e mostre a sua porção inteira.

nReal = float(input('Digite o valor: '))
print('O número real é {}, e sua porção inteira é: {}'.format(nReal, floor(nReal)))

