# Exercício Python 52: Faça um programa que leia um
# número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número: '))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end='')
        cont += 1
    else:
        print('\033[m', end='')
    print(c, end=' ')
if cont == 2:
    print('\nNúmero primo')
else:
    print('\n\033[mNão é primo, é divisivel por {} valores'.format(cont))