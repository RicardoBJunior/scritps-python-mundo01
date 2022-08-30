#Crie um programa que leia o nome de uma pessa e diga se ela tem silva no nome.

nome = str(input('Digite seu nome: ')).strip()

print('O nome digitado tem SILVA? {}'.format('SILVA' in nome.upper()))