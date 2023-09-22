# Em que ano você nasceu? 2000
# com 18 anos o voto é obrigatório!
# Com 48 anos: VOTO OBRIGATORIO!
# Com 8 anos: Não vota!
# Coma 65 anos: Voto Opcional

# Exercício Python 101:
# Crie um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem
# voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(nasc):
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - nasc

    if idade < 16:
        return f'Com {idade} ano(s): Não vota!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} ano(s): VOTO Opcional!'
    else:
        return f'Com {idade} ano(s): VOTO Obrigatório!'

# Programa Principal
nasc = int(input("Em que ano você nasceu?"))

print(voto(nasc))
