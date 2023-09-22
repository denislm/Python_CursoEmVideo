
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'pretoebranco':'\033[7;30m'}

print('\033[4;30;45mOlá Mundo!\033[m')

print('\033[7;30mOlá Mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a,b))

nome = 'Denis'
print('Olá" Muito prazer em te conhecer, {}{}{}!!!'.format(cores['vermelho'], nome, cores['limpa']))

s = 'prova de python'
x = bool(1)
print(x)

