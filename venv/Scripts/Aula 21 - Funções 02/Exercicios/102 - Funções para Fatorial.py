# Exercício Python 102:
# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show,
# que será um valor lógico (opcional) indicando se
# será mostrado ou não na tela o processo de cálculo do fatorial.

# Minha Função:
def fatorial(num = 0, show = False):
    '''
    -> Calcule o Fatorial de um número
    :param num: o número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do Fatorial de um número n
    '''
    if show is False:
        for i in range(num-1, 0, -1):
            num *= i
        return num
    else:
        texto = f'{num}'
        for i in range(num - 1, 0, -1):
            num *= i
            texto = texto + f' X {i}'
        texto = texto + f' = {num}'
        return texto

# Função do Curso em vídeo
def fatorial2(n = 0, show = False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' X ', end = '')
            else:
                print(' = ',end='')
        f *= c
    return f


print(fatorial2(7, True))
print(fatorial2(5, True))
help(fatorial)