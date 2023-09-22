# Crie um programa que mostre na tela todos
# os numeros pares que estão no intervalo entre 1 e 50

for c in range(1, 50):
    print('.', end='')
    if c % 2 == 0:
        print(c, end=' ')
# for c in range(1,51,2) menos saltos