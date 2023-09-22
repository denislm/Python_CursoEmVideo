# Exercício Python 095:
# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do
# aproveitamento de cada jogador.

from time import sleep

jogador = dict()
partidas  = list()
jogadores = list()
x = 1
continuar = 'Y'
while continuar not in 'nN':
    partidas.clear()
    jogador['nome'] = str(input(f'Nome do Jogador {x}: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range (0, tot):
        partidas.append(int(input(f'    Quantos Gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    jogadores.append(jogador.copy())
    continuar = input('Deseja Continuar? [S/N]: ').upper()[0]
    x += 1
print('-=-' * 22)
print(jogadores)

print('Selecione um dos jogadores, para mais informações: ')
for c,j in enumerate(jogadores):
    print(f'Jogador {c}: {j["nome"]}')

selecionado = int(input('digite o número do jogador: '))
if selecionado <= c:
    s = jogadores[selecionado]
    print(f'O jogador {s["nome"]} jogou {len(s["gols"])} partidas')
    for i, v in enumerate(s['gols']):
        print(f'    => Na partida {i},fez {v} gols')
        sleep(1)
    print(f'Foi um total de: {jogador["total"]} gols')

