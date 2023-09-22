print('-=-'*10)
print('\tTABUADA')
print('-=-'*10)
n = int(input('Digite um número: '))
for c in range(1,11):
    print('{} * {} = {}'.format(n, c, (n*c)))