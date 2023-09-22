# Método Moeda
global siglaMoeda

def aumentar(preço, taxa, format = False):
    '''
    -> Aumentar % do valor
    :param preço: Preço da moeda
    :param taxa: taxa % a ser aumentada
    :param format: Mostra a moeda (ex: R$) antes do valor
    :return: Retorna o valor com a % aumentada
    '''
    res = preço + (preço * taxa / 100)
    return res if format is False else moeda(res)


def diminuir(preço, taxa, format = False):
    '''
    -> Diminuir % do valor
    :param preço: Preço da moeda
    :param taxa: taxa % a ser diminuida
    :param format: Mostra a moeda (ex: R$) antes do valor
    :return: Retorna o valor com a % reduzida
    '''
    res = preço - (preço * taxa / 100)
    return moeda(res) if format else res


def dobro(preço, format = False):
    '''
    -> Dobra o valor
    :param preço: Preço da moeda
    :param format: Mostra a moeda (ex: R$) antes do valor:param format: Mostra a moeda (ex: R$) antes do valor
    :return: Retorna valor dobrado
    '''
    res = preço * 2
    return moeda(res) if format else res


def metade(num, v = False):
    num /= 2
    if v:
        return moeda(num)
    else:
        return num

def moeda(preço = 0):
    '''

    :param preço: Preço da moeda
    :return: Moeda formatada com Moeda do pais (Ex R$ u$)
    '''
    preço = '{} {:>5.2f}'.format(siglaMoeda, preço).replace('.', ',')
    return preço

def resumo(preço, aumenta, diminui):
    print('-' * 30)
    print('Resumo do Valor'.center(30))
    print('-' * 30)
    print(f'Preço Analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço,True)}')
    print(f'Metade do preço: \t{metade(preço,True)}')
    print(f'{aumenta}% de aumento: \t{aumentar(preço,aumenta,True)}')
    print(f'{diminui}% de redução: \t{diminuir(preço,diminui,True)}')
    print('-' * 30)