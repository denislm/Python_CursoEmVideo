# Exercício Python 097:
# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex:
# escreva(‘Olá, Mundo!’) Saída:
# ~~~~~~~~~~~~~~
#   Olá, Mundo!
# ~~~~~~~~~~~~~~

def escreva(t):
    quant = len(t) + 4
    print('^' * quant)
    print(f'  {t}  ')
    print('^' * quant)
escreva('Curso em vídeo')
escreva('Aula 97')
texto = input('Digite o texto: ')
escreva(texto)