# Exercício Python 20: O mesmo professor do desafio 19
# quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

alu01 = str(input('Digite o nome do aluno 01: '))
alu02 = str(input('Digite o nome do aluno 02: '))
alu03 = str(input('Digite o nome do aluno 03: '))
alu04 = str(input('Digite o nome do aluno 04: '))

lista = [alu01,alu02,alu03,alu04]

random.shuffle(lista)

print(lista)
