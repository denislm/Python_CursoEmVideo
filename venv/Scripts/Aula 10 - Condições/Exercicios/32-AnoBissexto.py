# Faça um programa que leia um ano qualquer
# mostre se o ano é bissexto
# se o ano não terminar em 00
# e for divisível por 4 dizemos que ele é bissexto.
# Os anos terminados em 00 serão bissextos
# se a divisão deles por 400 for exata (==0)

valor = str(input('Digite o valor de um ano qualquer: '))
ano = int(valor)
if valor.endswith('0'):
    if ano % 400 == 0:
        print('O ano é bissexto:',ano)
    else:
        print('O ano não é Bissexto!:',ano)
elif ano % 4 == 0:
    print('Ano Bissexto, ',ano)
else:
    print('Ano não Bissexto!')

