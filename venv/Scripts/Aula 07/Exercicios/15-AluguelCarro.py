quantDias = int(input('Por quantos dias você alugou o carro?'))
quantKm = float(input('Digite a quantidade de KMs andados: '))
valor = (quantDias * 60) + (quantKm * 0.15)
print('Você pagará: R$',valor)