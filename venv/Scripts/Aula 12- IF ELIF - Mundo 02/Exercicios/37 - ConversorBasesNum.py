# PRograma recebe numero Inteiro e converte para:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

num = int(input('Digite um número Inteiro: '))
print('[ 1 ] converter para BINARIO.')
print('[ 2 ] converter para OCTAL.')
print('[ 3 ] converter para HEXADECIMAL.')

op = int(input('Digite sua opção: '))

if op == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, hex(num)[2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente!')