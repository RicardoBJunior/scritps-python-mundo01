velocidade = float(input('Digite a velocidade do carro: '))
multa = 7.0
multado = (velocidade - 80) * multa

if velocidade <= 80.0:
    print('Você está no limite permitido da via.')
else:
    print('Você passou acima da velocidade permetida: {:.2f}KM/H Você foi multado em: R${:.2f} '.format(velocidade,multado))

