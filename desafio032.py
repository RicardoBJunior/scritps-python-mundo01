from datetime import date
ano = int(input('Digite o ano: '))

#print('Esse ano é bissexto'if(ano % 4 == 0) else 'Nao é bissexto')
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Esse ano é bissexto!')
else:
    print('Não é bissexto!')