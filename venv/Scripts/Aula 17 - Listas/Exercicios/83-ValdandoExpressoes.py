# Exercício Python 083:
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = input('Digite a expressão: ')
abre = expressao.count('(')
fecha = expressao.count(')')
l1 = l2 = False
if abre == fecha:
    for l in expressao:
        if l == '(':
            l1 = True;
            l2 = False;
        if l == ')' and l1 == True:
            l2 = True
if l1 == True and l2 == True:
    print('Expressão Correta!')
else:
    print('Expressão incorreta!')
