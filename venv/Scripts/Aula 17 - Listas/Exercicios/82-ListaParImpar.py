# Exercício Python 082:
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
par = []
impar = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    continuar = ' '
    while continuar not in 'sSnN':
        continuar = input('quer continuar? ')
    if continuar in 'nN':
        break
print(f'Lista: {lista}')

for n in lista:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(f'Par: {par}')
print(f'Impar: {impar}')
