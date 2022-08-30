#crie um programa que leia o nome de uma cidade e diga se ela começa ou nao o nome SANTO

cidade = str(input('Digite o nome da cidade: ')).strip()
cidade.upper() == 'SANTO'
cidadecortada = cidade.split()


#print('Sua cidade começa com SANTO? {}'.format('SANTO' in cidadecortada[0]))

print(cidade[:5].upper()=='SANTO')