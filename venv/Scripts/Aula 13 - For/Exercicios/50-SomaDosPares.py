# Desenvolva um programa que leia seis números inteiros e
# mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for impar, desconsidere-o.
print('-=-'*10)
print('Somador de números pares: ')
print('-=-'*10)
s = 0
cont = 0
for c in range(0,6):
    n = int(input('Digite o número {}: '.format(c+1)))
    if n % 2 == 0:
        s += n
        cont += 1
print('Você informou {} números PARES e a soma foi {}'.format(cont, s))


