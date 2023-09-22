# Exercício Python 087:
# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaMatriz = 0
terceira = 0
maiorSegundaCol = 0

# l = Linha, c = Coluna
for l in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f'Digite um valor, para {[l, c]}: '))
        matriz[l][c] = valor
        if valor % 2 == 0:
            somaMatriz += valor
        if l== 2:
            terceira += valor
        if l == 1:
            if maiorSegundaCol < valor:
                maiorSegundaCol = valor
print(matriz)
print(f'O valor da soma dos números pares da Matriz é: {somaMatriz}')
print(f'O valor da soma dos números da 3ª Coluna são {terceira}')
print(f'O maior valor da 2ª Coluna é {maiorSegundaCol}')


