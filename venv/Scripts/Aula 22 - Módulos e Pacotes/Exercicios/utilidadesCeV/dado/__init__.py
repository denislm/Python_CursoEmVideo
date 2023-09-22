def leiaDinheiroMeu(dinheiro):
    dinheiroSemVirgula = dinheiro.replace(',', '.')
    try:
        return float(dinheiroSemVirgula)
    except:
        print(f'\033[031m{dinheiro} é um valor iválido!\033[m')
        return False


def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg))
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[031mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            válido = True
            return float(entrada.replace(',','.'))
