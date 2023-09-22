# Exercício Python 091:
# Crie um programa onde 4 jogadores joguem um dado e
# tenham resultados aleatórios. Guarde esses resultados
# em um dicionário em Python. No final,
# coloque esse dicionário em ordem, sabendo que o
# vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogo = {}

for j in range(1,5):
    concatena = 'jogador' + str(j)
    jogo[concatena] = randint(1,6)
# Imprime valores dos dados dos jogadores
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)

print('-=-' * 15)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse =True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
    