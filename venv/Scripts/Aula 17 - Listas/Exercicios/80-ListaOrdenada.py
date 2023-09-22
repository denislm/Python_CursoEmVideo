# Exercício Python 080:
# Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista, já na posição correta de inserção
# (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []
while True:
    if len(lista) == 5:
        break
    num = int(input('Digite um valor: '))
    if len(lista) > 0:
        menor = min(lista)
        if menor > num:
            print(lista.index(menor))
            lista.insert(0,num)
            print(lista)

    else:
        lista.append(num)


