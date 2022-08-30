import random

nome1 = str(input('Primeiro nome '))
nome2 = str(input('Segundo nome '))
nome3 = str(input('terceiro nome '))
nome4 = str(input('quarto nome '))

lista = [nome1, nome2, nome3, nome4]

random.shuffle(lista)

print('Sorteio na ordem :')
print(lista)