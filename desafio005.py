#Faça um programa que leia um numero na tela e 
# mostre na tela o seu sucessor e seu antecessor.

numero = int(input('Digite o numero '))
print('O numero digitado é {}, o seu antecessor é {}, e seu sucessor é {}'.format(numero, (numero - 1), (numero + 1)))