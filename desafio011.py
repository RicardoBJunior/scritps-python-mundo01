#faca um programa que leia a largura e altura de uma parede em metros, calucle a sua
#area e a quantidade de tinta necessarioa para pintar sabendo que cada litro de tinta
#pinta uma area de 2m².

largurap = float(input('Digite a largura da parede: '))

alturap = float(input('Digite a altura da parede: '))

areap = (alturap*largurap)

tinta = int(2)

print('A area é: {}m², consegue pintar: {}'.format(areap, ((areap/tinta))))