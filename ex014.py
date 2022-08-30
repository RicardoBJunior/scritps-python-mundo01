# conversor de temperatura graus celsius para graus fahrenheit.

grauC = float(input('Digite a temperatura em Graus Celsius: '))


print('A temperatura que você digitou é {}C'.format(grauC))
tF = (grauC * 1.8) + 32
float(tF)
print('A temperatura convertida para Fahrenheit é: {:.1f}F'.format(tF))