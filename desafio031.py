km = float(input('Digite a km da viagem: '))
viagem = km * 0.50 #viagem até 200km
viagemL = km * 0.45 #viagens acima de 200km
if km <=200:
    print('Você pagará: R${}'.format(viagem))
else:
    print('Você pagará: R${}'.format(viagemL))