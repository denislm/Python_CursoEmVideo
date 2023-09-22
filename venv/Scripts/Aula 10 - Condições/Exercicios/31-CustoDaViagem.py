# Programa que pergunte a disntância de uma viagem em KM
# Calcule o preço da passagem cobrando:
# 0,50 por KM para viagens até 200 KM
# 0,45 para viagens mais longas

distancia = float(input('Digite a distancia percorrida na viagem: '))
valor = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O valor a ser pago é de: R$ {:.2f}'.format(valor))
