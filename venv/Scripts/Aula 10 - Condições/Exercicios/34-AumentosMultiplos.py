# Programa deve perguntar o salário de um funcionário
# calcular o valor do seu aumento:
# Se o salario for maior que 1.250,00: 10% de aumento
# Se o salario for menor que 1.250,00: 15% de aumento

salario = float(input('Digite o valor do seu salário: '))

if salario > 1250:
    salario = salario + (salario * 0.10)
else:
    salario = salario + (salario * 0.15)

print('Seu novo salário será de: R$ {:.2f}'.format(salario))

