#Exercício Python 105:

# Faça um programa que tenha uma função notas()
# que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:
# – Quantidade de notas                                                                                                                                                  – A maior nota                                                                                                                                                                – A menor nota                                                                                                                                                              – A média da turma                                                                                                                                                      – A situação (opcional)
#    – A maior nota
#       – A menor nota
#           – A média da turma
#               – A situação (opcional)
# Aula Anterior

def notas(* n, sit = False):
    '''
    Função para analisar notas e situações de vários alunos:
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    '''
    quant = len(n)
    maior = max(n)
    menor = min(n)
    media = sum(n) / quant

    dicNotas = {'Quantidade de notas' : quant,
                'maior' : maior,
                'menor' : menor,
                'média' : media}
    if sit:
        if media >= 7:
            dicNotas['Situação'] = 'BOA'
        elif media >= 5:
            dicNotas['Situação'] = 'RAZOÁVEL'
        else:
            dicNotas['Situação'] = 'RUIM'

    return dicNotas



resp = notas(5.5, 9.5, 10, 6.5,sit=True)
print(resp)
resp = notas(3, 3.5, 5, 6.5, sit = True)
print(resp)
#help(notas)
