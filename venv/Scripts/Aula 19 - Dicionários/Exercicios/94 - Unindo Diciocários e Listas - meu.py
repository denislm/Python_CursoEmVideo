# Exercício Python 094:
# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários
# em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoas = list()
pessoa = dict()
mulheres = list()
maiorQueMedia = list()
c = 1
while True:
    pessoa['nome'] = str(input(f'Nome da pessoa {c}: '))
    sexo = ' '
    while(sexo not in 'MmFf'):
        sexo = str(input('Sexo (M/F): ')[0].upper())
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('Idade: '))
    continuar = input('Deseja continuar (s/n): ')
    c += 1
    pessoas.append(pessoa.copy())
    if continuar == 'n':
        break
print('-=-' * 22)
print(pessoas)
print('-=-' * 22)
# A) Quantas pessoas foram cadastradas
total = len(pessoas)
print(f'A) Ao todo temos: {total} pessoas cadastradas')

# B) A média de idade
c = 0
media = 0
for c in range(0, total):
    media = media + pessoas[c]['idade']
    if pessoas[c]['sexo'] == 'F':
        mulheres.append(pessoas[c]['nome'].copy())
media = media / total
print('B) A Média das idades é: {:.2f} anos'.format(media))
print('-=-' * 22)
# C) Uma lista com as mulheres
print('C) As mulheres cadastradas foram: ')
print(mulheres)
print('-=-' * 22)
# D) Uma lista de pessoas com idade acima da média
for c in range(0, total):
    if pessoas[c]['idade'] > media:
        maiorQueMedia.append(pessoas[c].copy())
print('Lista de pessoas com idade maior que a média: ')
print(maiorQueMedia)
