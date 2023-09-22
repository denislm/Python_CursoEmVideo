n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valors: '))
print(type(n1))
s= n1 +n2

# Python 2
# print('A soma entre',n1,'e',n2,'é',s)

# Minha tentativa
# print('A soma entre {}'.format(n1) + ' e {}'.format(n2)+' é',s)

# Melhor método de print
print('A soma entre {} e {} vale {}'.format(n1, n2, s))
