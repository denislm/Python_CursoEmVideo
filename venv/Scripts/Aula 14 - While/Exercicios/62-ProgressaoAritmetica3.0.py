print('-=-'*10)
print('Gerador de PA')
print('-=-'*10)
quantTermos = 10
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termosTotais = 10
while quantTermos != 0:
    cont = 0
    num = primeiro

    print(primeiro,end=' -> ')

    while cont < quantTermos:
        num += razão
        print(num,end=' -> ')
        cont += 1
    print('Final')
    quantTermos = int(input('Gostaria de mostrar mais quantos termos?'))
    termosTotais += quantTermos
    primeiro = num
print('A progressão foi finalizada com {} termos mostrados!'.format(termosTotais))