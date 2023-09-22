dados = dict()
# Cria Dicionário com indices em String
dados = { 'nome':'Pedro','idade':25 }
print(dados['nome'])
print(dados['idade'])
# Append não funciona, para adicionar, só declarar novo Indice
dados['sexo']='M'
# Imprime o dicionário completo
print(dados)
# Remover elemento do Dicionário
del dados['idade']

# Declara Dicionário de Filmes
filme = {
    'titulo':'Star Wars',
    'ano':1977,
    'diretor':'George Lucas',
}
print( '\n Imprime todos valores guardados' )
print(filme.values())
print( '\n Imprime todas chaves Guardados' )
print(filme.keys())
print( ' \n Imprime todas chaves e valores juntos' )
print(filme.items())

print('\n Imprime chave e valores formatados! ')
for k,v in filme.items():
    print(f' O {k} é {v}')

# Cria lista com Dicionários dentro
locadora = list()
locadora.append(filme)
filme = {
    'titulo':'Avengers',
    'ano':2012,
    'diretor':'Joss Whedon'
}
locadora.append(filme)

print('\n{}'.format(locadora))
print('\nImprime ano do filme na segunda posição (01)! ')
print(locadora[1]['ano'])


