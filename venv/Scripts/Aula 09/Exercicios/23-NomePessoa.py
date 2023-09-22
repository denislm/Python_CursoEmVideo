# Crie um programa que leia o nome completo de uma pessoa
# mostre o nome com letras maiusculas
# com letras minusculas
# quantas letras sxistem(sem considerar espaços)
#quantas letras tem o primeiro nome

nome = str(input('Digite o seu nome completo: ').strip())
print('Nome em maiúculo\n{}'.format(nome.upper()))
print('Nome em minusculo\n{}'.format(nome.lower()))
#nome = nome.split()
#len(''.join(nome) conta letras sem espaços
# print('O seu primeiro nome possui {} letras'.format(len(nome[0])))
print('O seu nome possui {} letras'.format(len(nome)-nome.count(" ")))
print('O seu primeiro nome possui {} letras'.format(nome.find(" ")))