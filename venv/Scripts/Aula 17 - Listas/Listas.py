lanche = ['hamburguer', 'Suco', 'Pizza', 'Pudim']
lanche[3] = 'batata'
print(lanche)
lanche.append('Cookie')
print(lanche)
lanche.insert(0,'Cachorro Quente')
print(lanche)
del(lanche[2])  #lanche.pop(3)   #lanche.remove('Pizza')    Fazem a mesma coisa
print(lanche)
lanche.pop()
print(lanche)
if 'Pizza' in lanche:
    lanche.remove('Pizza')
print(lanche)
lanche.sort()
print(lanche)
