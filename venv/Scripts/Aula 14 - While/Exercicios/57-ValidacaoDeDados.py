# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado,
# peça a digitação novamente até ter um valor correto.

sexo = input('Informe seu Sexo [M]/[F]: ').upper().strip()[0]
while sexo not in 'MmFf':
    sexo = input('Sexo inválido, digite novamente: ').upper()
print('Sexo {}, registrado com sucesso!'.format(sexo))