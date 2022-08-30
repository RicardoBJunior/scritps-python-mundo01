salario = float(input('Digite o salario: '))
if salario >= 1250:
    print('Salario com reajuste de 10 porcento fica R${salarior:.2f}'.format(salarior = salario * 1.10))
else:
     print('Salario com reajuste de 15 porcento fica R${salarioi:.2f}'.format(salarioi = salario * 1.15))