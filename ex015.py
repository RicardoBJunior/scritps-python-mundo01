#Exercício Python 15: Escreva um programa que pergunte a quantidade de 
# Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.


print('Bem vindo!')

kmh = int(input('Quantos Km você percorreu com o carro alugado? '))
dia = float(input('Quantos dias você ficou com o carro alugado? '))

precoP = (kmh * 0.15) + (dia * 60) 


print('Voce vai ter que pagar R${:.2f} pelo aluguel do carro.'.format(precoP))