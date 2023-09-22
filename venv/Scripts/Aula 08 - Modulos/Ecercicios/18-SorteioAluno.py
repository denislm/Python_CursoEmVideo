# Um professor quer sortear um dos seus quatro alunos
# para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice

alu01 = str(input('Digite o nome do ALuno 01: '))
alu02 = str(input('Digite o nome do Aluno 02: '))
alu03 = str(input('Digite o nome do Aluno 03: '))
alu04 = str(input('Digite o nome do Aluno 04: '))

lista = [alu04,alu03,alu02,alu01]
escolhido = choice(lista)

print('O Aluno escolhido é: {}'.format(escolhido))