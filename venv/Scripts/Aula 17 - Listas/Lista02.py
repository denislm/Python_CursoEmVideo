num = list(range(4,11))
print(num)
num.sort(reverse=True)
print(num)
num.append(11)
print(num)
num[7] = 3
num.insert(2,2)
print(num)

if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')
print(num)
print(f'Essa lista tem {len(num)} elementos')
