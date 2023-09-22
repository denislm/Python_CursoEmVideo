#Ex 08, ler valor em metros e converter para centimetros e milimetros

metro = float(input('Escreva um valor em metros: '))
cm = metro * 100
mm = metro * 1000
print('O valor {} em CM é de: {} cm \nO valor em mm é de {}'.format(metro,cm,mm))