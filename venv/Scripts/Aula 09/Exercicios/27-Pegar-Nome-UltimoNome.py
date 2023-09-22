#Exercício Python 27:
# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Digite seu nome completo: ').strip().title()
separa = nome.split()
firstName = separa[0]
posicaoFinal = (len(separa)-1)
lastName = separa[posicaoFinal]
print('Seu primeiro nome é:',firstName)
print('Seu ultimo nome é:',lastName)
