# Desenvolva uma lógica que leia o peso e altura de
# uma pessoa, calcule seu IMC e mostre seu status de acordo
# com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidde morbida

peso = float(input('Digite o seu peso: '))
altura = int(input('Digite a sua altura em CM: '))/100

imc = peso / (altura**2)

pesomin = 18.5 * altura ** 2
pesomax = 24.99 * altura ** 2

print('Seu IMC é {:.2f}, Peso Min {:.2f}, Peso Max {:.2f}'.format(imc, pesomin, pesomax))


if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal')
elif 25 <= imc < 30:
    print('Você está com sobrepeso')
elif 30 <= imc < 35:
    print('Você está com Obesidade Grau I')
elif 35 <= imc < 40:
    print('Você está com Obesidade Grau II')
else:
    print('Você está com Obesidade Grau III!')