print('-=-'*10)
print('Gerador de PA')
print('-=-'*10)

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
cont = 0
num = primeiro

print(primeiro,end=' -> ')

while cont < 10:
    num += razão
    print(num,end=' -> ')
    cont += 1
print('Final')
