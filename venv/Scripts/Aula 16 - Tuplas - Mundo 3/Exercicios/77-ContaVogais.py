palavras = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON',
            'CURSO','GRATIS','ESTUDAR','PRATICAR','TRABALHAR',
            'MERCADO','PROGRAMADOR','FUTURO')

for palavra in palavras:
    palavra = palavra.upper()
    print(f'\nNa palavra {palavra}, temos: ',end=' ')
    if palavra.count('A') > 0:
        print('A',end=' ')
    if palavra.count('E') > 0:
        print('E',end=' ')
    if palavra.count('I') > 0:
        print('I',end=' ')
    if palavra.count('O') > 0:
        print('O',end=' ')
    if palavra.count('U') > 0:
        print('U',end='')


