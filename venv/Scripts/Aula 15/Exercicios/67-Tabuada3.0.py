num = 1
while True:
    print(30 * '------')
    num = int(input('Quer ver a tabuada de qual valor? '))
    print(30 * '------')
    if num < 0:
        break
    for c in range(1,11):
        print(f'{num} X {c} = {num * c}')
print('Programa de Tabuada Encerrado!')

