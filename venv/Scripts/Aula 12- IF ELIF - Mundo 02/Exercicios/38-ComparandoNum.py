# programa deve ler dois números inteiros
# compararar mostrando:
# - O primeiro valor é maior
# - O Segundo valor é maior
# - Não existe valor maior, os dois são iguais

n1 = int(input('Digitwe o primeiro númerto: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O primeiro número: {}, é maior'.format(n1))
elif n2 > n1:
    print('O Segundo número: {}, é maior'.format(n2))
else:
    print('Os dois números são iguais!')