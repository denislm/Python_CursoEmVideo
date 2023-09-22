# Exercício Python 096:
# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.

def area(l, c):
    a = l * c
    return a

print(' Controle de Terrenos ')
print('-'*20)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))


print('A área de um terreno {:.2f} x {:.2f} é de {:.2f} m².'.format(largura, comprimento, area(largura,comprimento)))
