# Exercício Python 092:
# Crie um programa que leia nome, ano de nascimento e
# carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO,
# o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade,
# com quantos anos a pessoa vai se aposentar (35 anos de trabalho)
from datetime import datetime
anoAtual = datetime.now().year

trabalhador = {}
trabalhador['nome'] = str(input('Nome: '))
trabalhador['nascimento'] = int(input('Ano de nascimento: '))
trabalhador['ctps'] = int(input('CTPS (0 para não tem): '))
trabalhador['idade'] = anoAtual - trabalhador['nascimento']
if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de Contratação: '))
    trabalhador['salario'] = float(input('Salário: '))
    trabalhador['Aposentadoria'] = trabalhador['idade'] + (trabalhador['contratação'] + 35) - anoAtual

print('-=-' * 22)
for k, v in trabalhador.items():
    print(f'- {k} tem o valor {v}')

