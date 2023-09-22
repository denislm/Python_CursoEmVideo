# Exercício Python 73:
# Crie uma tupla preenchida com os 20 primeiros colocados
# da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.
print('-='*15)
time = ('Corinthians','Palmeiras','antos','Grêmio','Cruzeiro',
        'Flamengo','Vasco','Chapecoense','Atlético','Botafogo',
        'Atlético-PR','Bahia','São Paulo','Fluminense','Grêmio',
        'Palmeiras','Ponte Preta','Santos', 'Sport Recife', 'Coritiba')

print(f'5 primeiros colocados: {time[0:5]}')
print('-='*15)
print(f"últimos 4 colocados: {time[-5:-1]}")
print('-='*15)
print(f'Organização Alfabética: \n{sorted(time)}')
print('-='*15)
print(f'Posição Coretiba: {time.index("Coritiba")+1}')

