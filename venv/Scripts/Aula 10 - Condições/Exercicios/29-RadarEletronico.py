# O Programa deve ler a velocidade de um carro
# Se ele ultrapassar 80 KM/h, mostrar mensagem que ele foi multado
# A Multa vai custar R$ 7,00 por cada KM acima do limite

velocidade = float(input('Digite a velocidade atual do seu carro: '))

if velocidade > 80:
    multa = (velocidade - 80.0) * 7
    print('Você foi multado, devendo pagar o valor de: {:.2f} Reais!'.format(multa))
else:

    print('Muito bem, mantenha a velocidade abaixo de 80!')