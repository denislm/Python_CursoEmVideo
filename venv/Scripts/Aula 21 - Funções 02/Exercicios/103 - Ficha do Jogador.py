# Nome do Jogador: Romário
# número de Gols: 33


# Exercício Python 103:
# Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou.

# O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome = '<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato!')

# Programa Principal
nome = input('Nome do Jogador: ')
gols = input('número de Gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gols=gols)
else:
    ficha(nome, gols)

