# Exercício Python 079:
# Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro,
# ele não será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.

lista = []
continua = ' '
while True:
    num = float(input('Digite um número: '))
    if lista.count(num) == 0:
        lista.append(num)
        print(f'{num} Adicionado com sucesso!')
    else:
        print('Valor duplicado, não vou adicionar!')
    continua = ' '
    while continua not in 'SsNn':
        continua = input('Quer continuar? (S/N)')
    if continua in 'Nn':
        break;
lista.sort()
print('-='*20)
print(f'Você digitou os valores: {lista}')

