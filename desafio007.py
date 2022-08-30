#desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media.
#desafio007

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) /2

print('A soma das notas é: {}.\nA media do aluno é: {}'.format((nota1+nota2),media))