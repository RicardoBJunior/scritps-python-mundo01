#vCrie um programa que leia quanto dinheiro uma pessoa tem na carteira e 
# mostre quantos dolares ela pode comprar
dConta = float(input('Digite o valor que você tem na conta: '))
dolar = float(5.11)
print('Com R${} Reais você consgue comprar {:.2f} Dolares.'.format(dConta,(dConta/dolar)))