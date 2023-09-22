# Exercício Python 44: Elabore um programa que calcule o valor a ser pago
# por um produto, considerando o seu preço normal e condição de pagamento:
#  à vista dinheiro/cheque: 10% de desconto
#  à vista no cartão: 5% de desconto
#  em até 2x no cartão: preço formal
#  3x ou mais no cartão: 20% de juros

preço = float(input('Digite o preço das Compras: '))

print('[ 1 ] à vista dinheiro/cheque: 10% de desconto')
print('[ 2 ] à vista no cartão: 5% de desconto')
print('[ 3 ] até 2x no cartão: preço formal')
print('[ 4 ] 3x ou mais no cartão: 20% de juros')
op = int(input('\nDigite uma opção: '))
valor = 0

if op == 1:
    preço = preço - (preço * 0.10)
    print('Preço com desconto de 10%: {:.2f}'.format(preço))
elif op == 2:
    preço = preço - (preço * 0.05)
    print('Preço com desconto de 5%> {:.2f}'.format(preço))
elif op == 3:
    print('Preço: {:.2f}'.format(preço))
elif op == 4:
    preço = preço + (preço * 0.20)
    print('Preço com juros: {:.2f}'.format(preço))
else:
    print('Opção inválida!')