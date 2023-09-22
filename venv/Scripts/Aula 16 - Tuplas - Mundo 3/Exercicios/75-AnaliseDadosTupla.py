# Exercício Python 075:
# Desenvolva um programa que leia quatro valores pelo teclado
# e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.


# for c in range(0,4):
numeros = (int(input('digite um Valor: ')),
           int(input('digite um Valor: ')),
           int(input('digite um Valor: ')),
           int(input('digite um Valor: ')))


print(f'O valor 9 apareceu: {numeros.count(9)} vezes')
print(f'O valor 3 apareceu na : {numeros.index(3)+1}ª posição')
print('números pares: ',end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
