# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
import random
from time import sleep
itens = ('Pedra','Papel','Tesoura')
print('-=-'*15)
print('Bem vindo, ao Jokenpô!, escolha uma opção:')
print('[ 0 ] Pedra')
print('[ 1 ] Papel')
print('[ 2 ] Tesoura')
print('-=-'*15)
jogador = int(input('Digite o num da opção: '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!\n')
computador = random.randint(0,2)
print('-=-'*10)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=-'*10)
# Pedra
if computador == 0:
    if jogador == 0: # Computador pedra jogador pedra
        print('EMPATE!')
    elif jogador == 1:
        print('GANHOU!') # Computador pedra jogador papel
    elif jogador == 2:
        print('PERDEU!') # Computador pedra jogador tesoura
# Papel
elif computador == 1:
    if jogador == 0:
        print('PERDEU!') # Computador papel, jogador pedra
    elif jogador == 1:
        print('EMPATE!') # Computador papel, jogador papel
    elif jogador == 2:
        print('GANHOU!') # Computador papel, jogador Tesoura
# Tesoura
elif computador == 2:
    if jogador == 0:
        print('GANHOU!')# Computador tesoura, jogador pedra
    elif jogador == 1:
        print('GANHOU!') # Computador tesoura, jogador papel
    elif jogador == 2:
        print('Empate') # Computador tesoura, jogador tesoura
else:
    print('Número escolhido inválido!')
