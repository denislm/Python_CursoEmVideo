# Exercício Python 112:
# Dentro do pacote utilidadesCeV que criamos no desafio 111,
# temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro()
# que seja capaz de funcionar como a função imputa(),
# mas com uma validação de dados para aceitar apenas
# valores que seja monetários.

from utilidadesCeV import dado, Moeda


Moeda.siglaMoeda = 'R$'
p = dado.leiaDinheiro(f"Digite o preço: {Moeda.siglaMoeda} ")
Moeda.resumo(p, 35,22)




