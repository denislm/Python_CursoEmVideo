números = list()
while True:
        n = int(input('Digite um valor:'))
        if n not in números:
            números.append(n)
            print('Valor adicionado com sucesso....!')
        else:
            print('Valor duplicado! não vou adicionar!')
        r = str(input('Quer Continuar? (S/N'))
        if r in 'Nn':
            break
print(números)