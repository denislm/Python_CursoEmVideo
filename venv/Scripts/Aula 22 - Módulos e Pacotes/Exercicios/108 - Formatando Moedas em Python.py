# Exercício Python 108:
# Adapte o código do desafio #107,
# criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

from utilidadesCeV import Moeda

p = float(input("Digite o preço R$ "))
print(f'A metade de {Moeda.moeda(p)} é {Moeda.metade(p, True)}')
print(f'O dobro de R$ {Moeda.moeda(p)} é R$ {Moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {Moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {Moeda.diminuir(p, 13, True)}')
