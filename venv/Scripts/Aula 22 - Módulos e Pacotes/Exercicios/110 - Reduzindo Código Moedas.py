# Exercício Python 110:
# Adicione o módulo moeda.py criado nos desafios anteriores,
# uma função chamada resumo(), que mostre na tela algumas informações
# geradas pelas funções que já temos no módulo criado até aqui.

from utilidadesCeV import Moeda

Moeda.siglaMoeda = 'R$'

p = float(input(f"Digite o preço {Moeda.siglaMoeda} "))

Moeda.resumo(preço=p, aumenta=20, diminui=10)
