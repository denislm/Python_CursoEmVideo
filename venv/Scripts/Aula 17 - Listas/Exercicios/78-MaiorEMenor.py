lista=[]
for i in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
print(lista)
menor = min(lista)
maior = max(lista)
print(f'O maior número é {maior}, e sua posição é a {lista.index(maior)}')
print(f'O menor valor é o: {menor} e sua posição é a {lista.index(menor)}')