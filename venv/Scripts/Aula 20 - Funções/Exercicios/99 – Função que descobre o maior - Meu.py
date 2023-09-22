# Exercício Python 09:
# Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
# Verifica qual é o maior número, por meio de um For
def maior(* v):
    print('-=-' * 20)
    if len(v) == 0:
        print('Nenhum valor declarado!')
    else:
        maior = 0
        print(f'Valores (FOR): {v}')
        for k in v:
            if k >= maior:
                maior = k
        print(f'O maior valor é: {maior}')


# Ordena a lista em ordem númerica ou alfabética, pegando o ultimo item da lista (maior)
def maior2(* v):
    print('-=-' * 20)
    if len(v) == 0:
        print('Nenhum valor declarado!')
    else:
        print(f'Valores (sorted) {v}')
        newV = sorted(v)
        print(f'O maior valor é: {newV[-1]}')

#Função do MaiorCursoEmVideo
def maiorCurso(* núm):
    cont = maior = 0
    print('\Analisando os valores passados...')
    for valor in núm:
        print(f'{valor} ',end = '',flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi: {maior}')


maior(2, 9, 4, 5, 7, 1)
maior2(4, 7, 8)
maior(1, 2)
maior2(6)
maior2('A','2','99')
maiorCurso(2, 9, 4, 5, 7, 1)

