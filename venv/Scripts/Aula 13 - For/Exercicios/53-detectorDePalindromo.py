# Exercício Python 53: Crie um programa que leia uma frase qualquer
# e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

palavra = str(input('Digite a palavre: ').strip().replace(" ",""))

cAoCont = len(palavra)-1

for c in range(len(palavra)):
    if palavra[c] == palavra[cAoCont]:
        cAoCont -= 1
        if cAoCont == 0:
            print("A palavra {}, é um Palindromo!".format(palavra))
    else:
        print('A palavra {}, não  um Palindromo!'.format(palavra))
        break











