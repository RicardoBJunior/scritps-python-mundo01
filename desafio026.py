#faça um programa que leia uma frase pelo teclado e mostre:
#quantas vezes aparece a letra A
#em que posição ela aparece a primeira vez
#em que posição ela parece a última vez


frase = str(input('Digite a frase: ')).strip()
frase = frase.lower()
print('A letra A na frase:  {}, apareceu: {} vezes.'.format(frase,frase.count('a')))

print('A letra A apareceu a primeira vez na posição {}.'.format(frase.find('a')+1))

print('A letra A apareceu a ultima vez na posição {}.'.format(frase.rfind('a')+1))