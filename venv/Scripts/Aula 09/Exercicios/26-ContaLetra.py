# Mostrar quantas vezes a letra A aparece
# Em qual posição ela aparece pela primeira vez
# Em qual posição ela aparece a ultima vez

palavra = input('Digite uma palavra: ').lower().strip()
print('A letra A, aparece {} vezes'.format(palavra.count('a')))
print('A letra A, foi encontrada na posição: {}, pela primeira vez'.format(palavra.find('a')+1))
print('Ultima posição, onde se encontrou a letra A: {}'.format(palavra.rfind('a')+1))
