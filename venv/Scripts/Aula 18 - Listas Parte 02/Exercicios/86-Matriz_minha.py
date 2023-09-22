# Exercício Python 086:
# Crie um programa que declare uma matriz de dimensão 3×3 e preencha
# com valores lidos pelo teclado. No final, mostre a matriz na tela,
# com a formatação correta.

numeros = [[], [], []]
a = 0
b = 0

while True:
    if b < 3:
        valor = int(input(f'Digite um valor para: [{a}, {b}]'))
        numeros[a].append(valor)
        b = b + 1
    else:
        a = a + 1
        b = 0
    if a == 2 and b == 3:
        break

print(numeros)

