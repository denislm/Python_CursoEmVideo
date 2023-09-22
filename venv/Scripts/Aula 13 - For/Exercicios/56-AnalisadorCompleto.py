# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos

mediaIdade = 0
mulheres = 0
homemVelho = ''
idadehomemVelho = 0
for c in range(1,5):
    print('______ {}ª Pessoa ________'.format(c))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F]: ').upper()
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if sexo == 'M' and c == 1:
        homemVelho = nome
        idadehomemVelho = idade
    if sexo == 'M' and idade > idadehomemVelho:
        homemVelho = nome
        idadehomemVelho = idade


    mediaIdade += idade

mediaIdade = mediaIdade / 4
print('A média das idades é:',mediaIdade)
print('Existem {} mulheres, com menos de 20 anos!'.format(mulheres))
print('O Homem mais velho se chama {} e tem {} anos'.format(homemVelho,idadehomemVelho))
