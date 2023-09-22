# Desenvolva um programa que leia o primeiro termo
# e a razão de uma PA. No final, mostre os 10 primeiros
# termos dessa progressão.

print('-=-' * 10)
print('10 termos de uma PA')
print('-=-' * 10)
n = 0
primeiroTermo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
n = primeiroTermo
for c in range(primeiroTermo, 10):
    print(n,end=' -> ')
    n += razao
print('ACABOU')