# Gerar número entre 0 e 5
# usuário deve tentar acertar o número, informando se usuário venceu ou não
import random
from time import sleep
numGerado = random.randint(0,10)
#print(numGerado)

print('-=-'*20)
print('Tente adivinhar o número, escolhendo entre 0 e 10: ')
print('-=-'*20)

numEscolhido = 0
cont = 0
while numEscolhido != numGerado:

    numEscolhido = int(input('Qual número pensei?  '))
    cont += 1


    if numEscolhido > 10:
        print('O número deve ser menor que 10 e maior que 0!: ')
    elif numEscolhido < numGerado:
        print('Mais... Tente mais uma vez.')
    elif numEscolhido > numGerado:
        print('Menos... Tente mais uma vez.')


print('Você acertou o número!')
print('Você utilizou {} tentativas, para acertar!'.format(cont))
