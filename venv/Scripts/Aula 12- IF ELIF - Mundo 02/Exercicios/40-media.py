# Crie um programa que leia duas notas de um aluno
# Calcule sua média mostrando:
# - Média baixo de 5.0: Reprovado
# - Média entre 5.0 e 5.9: Recuperação
# - Média 7.0 ou mais: Aprovado

nota1 = float(input('Digite a nota da Primeira Prova: '))
nota2 = float(input('Digite a nota da Segunda Prova: '))

media = (nota1 + nota2) / 2
print('Sua média foi de {:.2f}'.format(media))
if media < 5:
    print('Você está reprovado!')
elif 5 <= media < 7:
    print('Você está de recuperação!')
else:
    print('Você foi aprovado!')