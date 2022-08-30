


nome = str(input('Digite o seu nome: '))

print('Nome: ',nome)

print('Nome caixa alta: ',nome.upper())

print('Nome caixa baixa: ',nome.lower())

nomeS = nome.replace(' ','')

print('Com espaço :',len(nome))

print('Sem espaço :',len(nomeS))

print(nomeS)

pNome = nome.split()

ppNome = pNome[0]

print('Seu primeiro nome é {} e tem {} letras'.format(pNome[0], len(ppNome)))

