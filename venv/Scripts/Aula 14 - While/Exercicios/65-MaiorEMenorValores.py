# Exercício Python 65:
# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual
# foi o maior e o menor valores lidos. O programa deve perguntar
# ao usuário se ele quer ou não continuar a digitar valores.

soma = média = 0
quant = 0
continuar = 'S'
maior = menor = 0
while continuar in 'Ss':
        num = int(input('Digite um número: '))
        quant += 1
        soma += num
        if quant == 1:
                maior = menor = num
        if num < menor:
                menor = num
        if num > maior:
                maior = num

        continuar = str(input('Quer continuar? (s/n)')).upper().strip()[0]

print('media = {} / {}'.format(soma, quant))
média = soma / quant
print('Você digitou {} números, sendo a média de todos {}'. format(quant, média))
print('O maior número é o {} e o menor é o {}'.format(maior,menor))