# Gerar número entre 0 e 5
# usuário deve tentar acertar o número, informando se usuário venceu ou não
import random
from time import sleep
numGerado = random.randint(0,5)
#print(numGerado)
print('-=-'*20)
print('Tente adivinhar o número, escolhendo entre 0 e 5: ')
print('-=-'*20)

numEscolhido = int(input('Qual número pensei?  '))
print('Processando...')
sleep(3)
if numEscolhido == numGerado:
    print('Você acertou o número!')
elif numEscolhido > 5:
    print('O número deve ser menor que 5 e maior que 0!: ')
else:
    print('Você errou o número! o número correto era:',numGerado)

