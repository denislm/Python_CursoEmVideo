# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o Segundo número: '))

print('Selecione uma das opções abaixo: \n'+
      '[ 1 ] somar \n'+
      '[ 2 ] multiplicar \n'+
      '[ 3 ] maior \n'+
      '[ 4 ] novos números \n'+
      '[ 5 ] sair do programa \n')
op = 0
while op != 5:
    op = int(input('Selecione uma opção: '))
    if op == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif op == 2:
        print('{} * {} = {}'.format(n1, n2, n1 * n2))
    elif op == 3:
        if n1 > n2:
            print('O primeiro número: {}, é maior do que o Segundo {}'.format(n1, n2))
        elif n2 > n1:
            print('O segundo número: {}, é maior do que o Primeiro {}'.format(n2, n1))
        else:
            print('Os dois números são iguais!')
    elif op == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o Segundo número: '))
    elif op == 5:
        print('Finalizado!')
    else:
        print('Opção inválida!')

