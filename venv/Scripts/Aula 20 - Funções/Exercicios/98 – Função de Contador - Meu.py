# Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep

def contador(inicio,fim,passo):
    if(passo == 0):
        passo = 1
    if(inicio < fim):
        for c in range(inicio, fim+1, passo):
            print(c,end=' ')
            sleep(0.5)
    elif(inicio > fim):
        if passo == 0:
            passo = -1
        if passo > 0:
            passo = passo - (passo * 2)
        for c in range(inicio, fim-1, passo):
            print(c,end=' ')
            sleep(0.5)
    print('FIM!')

print('-=-' * 15)
print('A) de 1 até 10, de 1 em 1 ')
contador(1,10,1)
print('')
print('-=-' * 15)
print('B) de 10 até 0, de 2 em 2 ')
contador(10,0,2)
#contador(10,0,2)
print('\n','-=-' * 15)
i = int(input('Inicio: '))
f = int(input('Fim:	'))
p = int(input('Passo:	'))
contador(i,f,p)
