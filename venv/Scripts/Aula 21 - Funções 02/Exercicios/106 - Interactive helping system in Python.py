# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# SISTEMA DE AJUDA PyHELP (em cor verde
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Função ou Biblioteca > len
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Acessando o manual do comando 'len' (Azul)
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# mostra o help e volta para o menu (branco)
# fim - > Até logo -> vermelho
from time import sleep
def cabeçalho(texto, cor):
    print(f'\033[{cor}m')   # Seleciona cor do cabeçalho
    print('^' * (len(texto)+4)) # imprime ^^^^^, conforme quantidade de letras
    print(f'  {texto}  ')
    print('^' * (len(texto)+4))
    print('\033[m',end='')         # imprime ^^^^^^ colorido

#Programa principal

while True:
    cabeçalho(texto='Sistema de ajuda Pyhelp', cor='30:42')
    op = input('Função ou Biblioteca: ')
    if op == '99':
        print(cabeçalho('Até Logo!','031'))
        break
    else:
        cabeçalho(f"Acessando o manual do comando '{op}'",cor='1:30:44')
        print('\033[7:37m')
        help(op)
        print('\033[m')



