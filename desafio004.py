algo = input('Digite algo: ')
print('o tipo primitivo desse valor é', type(algo))

print('é só números? ',algo.isnumeric())
print('apenas letras ?',algo.isalpha())
print('apenas digitos digitais ?',algo.isdigit())
print('caixa alta',algo.isupper())
print('so tem espacos',algo.isspace())