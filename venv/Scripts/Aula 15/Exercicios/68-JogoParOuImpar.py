from random import randint
lista = ['P','I']
acertos = 0
while True:
    computador = random.randint(0,1)
    escolhido = str(input('Par (P) ou Impar (I): ')).upper()[0]
    if escolhido is lista[computador]:
        print(f'Parabéns, você acertou!, {lista[computador]}')
        acertos += 1
    else:
        print('Você errou!')
        break
print(f'Vitórias: {acertos} Pontos')