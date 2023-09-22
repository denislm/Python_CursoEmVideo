#ex 06, algoritmo que leia um número e mostre o dobro o triplo e raiz quadrada
num1 = int(input('DIgite um número: '))
dobro = num1*2
triplo = num1*3
raiz = num1**(1/2)

print('O dobro de {}, vale {}\nO triplo vale {}\nA raiz quadrada, vale {:.2f}'.format(num1,dobro,triplo,raiz))