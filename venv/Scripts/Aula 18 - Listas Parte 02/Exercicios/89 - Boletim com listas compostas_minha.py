#Exercício Python 089:
# Crie um programa que leia nome e duas notas de vários alunos
# e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita
# que o usuário possa mostrar as notas de cada aluno individualmente.

Aluno = list()
lista = list()
continuar = 's'

while continuar == 's':
    Aluno.append(input('Nome do Aluno: '))
    Aluno.append(float(input('Digite a Nota 01: ')))
    Aluno.append(float(input('Digite a Nota 02: ')))
    lista.append(Aluno[:])
    Aluno.clear()
    continuar = input('Deseja Continuar? (s/n): ')

i = 1

print('\nMédias de cada Aluno: ')
for nome, n1, n2 in lista:
    print(f'{i}: {nome}, média: {(n1 + n2) / 2}')
    i+=1

print('\nGostaria de ver as notas de qual aluno? (999 interrompe)')
num = int(input('Digite o número do aluno: '))
nome = lista[num-1][0]
n1 = lista[num-1][1]
n2 = lista[num-1][2]
media = n1 / n2
print(f'\nAs Notas do {nome} são: ')
print('Nota 01: {:.2f},'.format(n1))
print('Nota 02: {:.2f},'.format(n1))
print('Média: {:.2f}'.format(n1))

