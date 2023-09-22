print('Cedulas de R$ 1, R$ 10, R$ 20 e R$ 50')
valor = int(input('QUanto você gostaria de sacar? '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        elif céd == 1:
            céd = 1
        totcéd = 0
        if total == 0:
            break