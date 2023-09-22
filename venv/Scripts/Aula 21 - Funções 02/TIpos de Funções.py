# Cria Função de soma
def somaSimples(a, b):
    s = a + b
    print(f"{a} + {b} = {s}")
#função com empacotamento
def contador(* num):
    for valor in num:
        print(valor, end=', ')
    print('FIM!')
    print(f'Recebi o total de {len(num)} valores')
def dobra(lst):
    pos = 0
    while pos < (len(lst)):
        lst[pos] *= 2
        pos += 1
    return lst
def somaEmpacotada(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')
def titulo(msg):
    print('----------------------------------------')
    print(msg)
    print('----------------------------------------')


titulo("Curso em vídeo")
somaSimples(2,5)
contador(1,2,3,4,5,6)

valores = [7,2,5,0,4]
print(f'Valores de uma lista: {valores}')
dobra(valores)
print(f'Valores dobrados: {valores}')
somaEmpacotada(1,2,3,4,5,6,7,8,9,10)
