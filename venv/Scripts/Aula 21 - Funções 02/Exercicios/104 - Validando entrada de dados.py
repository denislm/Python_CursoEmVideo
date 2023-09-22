# n = leiaInt('Digite um número')
# print(f'você acabou de digitar o número {n}')
# Digite um número: 4
# Você acabou de digitar o número 4
# Digite um número: w (ERRO! Digite um número inteiro válido.)
# Exercício Python 104:

# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input()
# do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(texto):
    while True:
        num = input(texto)
        if num.isnumeric():
            return num
            break
        else:
            print('\033[31mERRO! Digite um número inteiro válido!\033[m')


#Programa Principal
n = leiaInt('Digite o número: ')
print(f'\033[32mVocê acabou de digitar o número: {n}\033[m')

