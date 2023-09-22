print('Cedulas de R$ 1, R$ 10, R$ 20 e R$ 50')
valor = int(input('QUanto você gostaria de sacar? '))
cinquenta = vinte = dez = um = 0
erro = 0
while valor != 0:
    if valor // 50:
        valor -= 50
        cinquenta += 1
    elif valor // 20:
        valor -= 20
        vinte += 1
    elif valor // 10:
        valor -= 10
        dez += 1
    elif valor // 1:
        valor -= 1
        um += 1

    else:
        erro = 1
        break
if erro == 0:
    print(f'{um} Notas de 1'
          f'\n{dez} Notas de 10'
          f'\n{vinte} Notas de 20'
          f'\n{cinquenta} Notas de 50')
else:
    print('Erro, valor para sacar inválido!')
