pessoas = {'nome' : 'Gustavo', 'sexo' : 'M', 'idade' : 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.values())
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')
pessoas['nome'] = 'Leandro'
pessoas['peso']=98.5
print(pessoas)

brasil = []
estado1 = {'uf' : 'Rio de Janeiro', 'sigla' : 'RJ'}
estado2 = {'uf' : 'São Paulo', 'sigla' : 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])

estado = dict()
brasil = list()
for c in range (0, 3):
    print(f'Estado {c+1}')
    estado['uf'] = str(input('Unidade federatifa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
        print()