# Exercício Python 70:
# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

preco = total = quant1000 = 0
nomeBarato = ' '
precoBarato = 0
while True:
    print('---'*15)
    print('NOVO PRODUTO')
    print('---'*15)
    produto = str(input('Produto: '))
    preco = float(input('Preço: '))
    total += preco
    print('---' * 15)
    if precoBarato == 0:
        nomeBarato = produto
        precoBarato = preco
    if preco < precoBarato:
        precoBarato = preco
        nomeBarato = produto
    if preco > 1000:
        quant1000 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Valor total: {total}')
print(f'Quantidade de produtos que custam mais de R$ 1000: {quant1000}')
print(f'Produto mais barato: {nomeBarato} ({precoBarato})')


