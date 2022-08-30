import random 

num = random.randint(0,5)

numero = int(input('Digite um número de 0 a 5: '))

if num == numero:
    print('Você adivinhou o número que o computador digitou.')
else:
    print('Você errou!!')
    
