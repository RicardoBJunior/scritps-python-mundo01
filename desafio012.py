# faca um algoritimo que leia o preco de um produto novo e mostre seu novo preco com 5% de desconto.

precoP = float(input('Digite o preço do produto: '))
#d = 5*precoP
#d1 = d/100
#precofinal = precoP - d1

precofinal = precoP - (precoP * 5 / 100)

print('O produto com desconto ficou agora por: {}'.format(precofinal))