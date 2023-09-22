# Exercício Python 100:
# Faça um programa que tenha uma lista chamada números e duas funções
# chamadas sorteia() e somaPar().
#
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
#
# e a segunda função vai mostrar a soma entre todos os valores
# pares sorteados pela função anterior.
import random
from time import sleep
def sorteia(números):
    print('-=-' * 15)
    print('Números Sorteados: ', end = '')
    for i in range(0, 5):
        num = random.randint(1,99)
        números.append(num)
        print(num, end=' ')
        sleep(0.3)
    print('\n',end='')
    print('-=-' * 15)


def somaPar(números):
    print('Valores pares: ',end='')
    for valor in números:
        if valor % 2 == 0:
            print(valor,end=' ')
            sleep(0.3)
    print('\n', end='')
    print('-=-' * 15)

#Programa
números = list()
sorteia(números)
somaPar(números)
print('26'[-1])
