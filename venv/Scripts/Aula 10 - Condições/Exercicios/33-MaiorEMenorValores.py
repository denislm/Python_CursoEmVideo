print('Digite 3 números')
a = float(input('Numéro 01: '))
b = float(input('Numero 02: '))
c = float(input('Numero 03: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c <b :
    menor = c
if a < b and a < c:
    menor = a
print('O menor valor é o',menor)

maior =a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
if a > b and a > c:
    maior = a
print('O maior valor é o',maior)


