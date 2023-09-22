num = 1
quant = soma = 0
while True:
    num = int(input('Digite o Número: '))
    if num == 999:
        break
    quant += 1
    soma += num
print(f'Você digitou {quant} valores {soma}')
