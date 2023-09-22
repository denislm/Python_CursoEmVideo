n = 1
par = 0
impar = 0
print('DIgite os valores e 0 para parar!')
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Números Pares:',par)
print('Números Impares:',impar)
