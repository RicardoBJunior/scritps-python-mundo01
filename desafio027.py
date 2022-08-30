#faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o ultimo nome,
#separadamente.

nome = str(input('Digite sue nome :')).strip()

print(nome)
cortanome = nome.split()
print(cortanome)
print('O primero nome é: ', cortanome[0])
print('O ultimo nome é: ',cortanome[-1])

