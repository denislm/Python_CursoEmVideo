# Faça um programa que receba o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triangulo

# se o maior lado for menor do que a seoma dos outros dois lados menores = triangulo
print('-=-'*26)
print('Digite o comprimento de três retas, para verificar se formam um triângulo:')
print('-=-'*26)
r1 = float(input('Comprimento da reta 01: '))
r2 = float(input('Comprimento da reta 02: '))
r3 = float(input('Comprimento da reta 03: '))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r2 + r1):
    print('É um Triangulo')
else:
    print('Não é um Triangulo')
