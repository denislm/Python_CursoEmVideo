a = [5, 54, 3, 2, 1]
b = a # Lista apenas foi linkada, altera um valor, a outra fica igual
b[2] = 8
print(a)
print(b)

b = a[:]
b[2] = 7
print(f'\n{a}')
print(b)