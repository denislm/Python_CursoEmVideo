# Exercício Python 060:
# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input('Digite um número, para calcular o fatorial: '))
texto = str(num)
cont = (num - 1)
fatorial = num
while cont != 0:
    fatorial *= cont
    texto = texto + ' * '+str(cont)
    cont -= 1
print('Calculando {}! = {} = {}'.format(num, texto, fatorial))




