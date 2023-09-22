# Faça um programa que leia o ano de nascimento
# de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alista ao serviço militar;
# Se é a hora de se alistar
# Se já passou o tempo do alistamento
from datetime import date

anoAtual = date.today().year
nascimento = int(input('Digite o seu ano de nascimento: '))
idade = anoAtual - nascimento
print('Legal, você completa este amo: {} anos!'.format(idade))
if idade == 18:
    print('Sendo assim, este ano você deve se alistar ao serviço militar! (Jan a Jun)')
elif idade < 18:
    print('Você não precisa se alistar ainda, apenas daqui {} anos '.format(18-idade))
else:
    resposta = str(input('Você já se alistou? (S/N): '))
    if resposta == 's':
        print('Muito bem! você deve ter se alistado há {} anos, atrás!\n'.format(idade - 18))

    elif resposta == 'n':
        print('Sinto muito, você já passou da idade de se alistar, em {} anos\n'.format(idade - 18)
              + 'Terá que ir atrás disso, se apresentando a uma junta militar!')
    else:
        print('Opção inválida!')