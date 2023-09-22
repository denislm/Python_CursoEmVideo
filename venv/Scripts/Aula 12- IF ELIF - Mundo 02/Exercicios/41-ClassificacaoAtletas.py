# A confederação nacional de natação precisa de um programa que leia:
# o ano de nascimento de um atleta e mostre sua categoria, de acordo com sua idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: Junior
# Até 20 anos: SENIOR
# Acima: MASTER
from datetime import date

anoAtual = date.today().year
anoAtleta = int(input('Digite o ano de Nacimento do atleta: '))
idade = anoAtual - anoAtleta
print('O nível do atleta com {} anos, é'.format(idade))
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade == 20:
    print('SENIOR')
else:
    print('MASTER')