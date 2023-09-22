# Faça um programa que calcule todos os números impares
# que são multiplos de três que se encontram no
# intervalo de 1 até 500
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        #print(c, end=' + ')
        cont += 1
        s += c
print('A soma de rodos os {} vaores solicitados é {}'.format(cont, s))