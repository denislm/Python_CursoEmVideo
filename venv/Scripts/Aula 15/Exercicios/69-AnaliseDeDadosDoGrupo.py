
cont = 1
homens = mulheres = 0
maiorDeIdade = 0
fMenosde20 = 0
continuar = 'S'

while continuar == 'S':
    print(20*'---')
    print('Cadastrar uma Pessoa')
    print(30*'---')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ').upper()[0])
    continuar = str(input('Continuar? (s/n): ').upper()[0])
    if sexo == 'M':
        homens += 1
        if idade > 18:
            maiorDeIdade += 1
    elif sexo == 'F':
        mulheres += 1
        if idade > 18:
            maiorDeIdade += 1
        elif idade < 20:
            fMenosde20 += 1
    else:
        print('Sexo inválido!')

print(f'Existem {homens} homens, {mulheres} mulheres, sendo'
      f'\nTotal: {homens + mulheres}'
      f'\n{maiorDeIdade} maiores de idade'
      f'\n{fMenosde20} mulheres, com menos de 20 anos')

