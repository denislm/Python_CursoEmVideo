# Exercício Python 53: Crie um programa que leia uma frase qualquer
# e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

palavra = str(input('Digite a palavre: ').strip().replace(" ",""))
invertida = ''
# for letra in range(len(junto) -1, -1, -1):
for letra in range(len(palavra) -1, -1,-1):
    invertida += palavra[letra]

if palavra == invertida:
    print("A palavra {}, é um Palindromo!".format(palavra))
    print('pois ao contrário fica',invertida)
else:
    print('A palavra {}, não  um Palindromo!'.format(palavra))
    print('pois ao contrário fica', invertida)












