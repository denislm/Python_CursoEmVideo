# Exercício Python 54: Crie um programa que leia o ano de nascimento
# de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores.
from datetime import date
ano = date.today().year
maior = 0
menor = 0

for c in range(0,7):
    nascimento = int(input('Em que ano nasceu a `{}ª pessoa: '.format(c+1)))
    if (ano - nascimento) < 18:
        menor += 1
    else:
        maior += 1
print('Ao todo tivemos {} pessoas Maiores de idade'.format(maior))
print('E {} pessoas, menores de Idade!'.format(menor))


