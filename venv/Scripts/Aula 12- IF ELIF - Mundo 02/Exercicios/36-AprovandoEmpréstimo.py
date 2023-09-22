# Escreva um programa para aprovar o empréstimo
# Bancario para a compra de uma casa, o programa, vai perguntas:
# O Valor da casa
# O Salário do comprador
# Quantos anos ele vai pagar

# Calcule o valor da prestação, sabendo, que ela não pode
# Exceder 30% do salário, ou então o empréstimo será negado!

print('-=-'*20+
      '\n\t\tSimulador de compra de Casa!\n'+
      '-=-'*20)

valorCasa = float(input('Qual é o valor da casa? '))
salario = float(input('Digite o valor do seu Salário: '))
anos =  int(input('Em quantos anos você gostaria de pagar?'))

prestacao = valorCasa / (anos * 12)
minimo = salario * 0.30

print('{:.2f}'.format(prestacao))

if (prestacao) < (minimo):
    print('Parabéns, sua casa pode ser financidada, em {} anos'.format(anos)+
          '\nSendo {} Prestações de R$ {:.2f}'.format((anos*12), prestacao))
else:
    print('Empréstimo negado!')
    print('Valor da prestação: {:.2f}'.format(prestacao))