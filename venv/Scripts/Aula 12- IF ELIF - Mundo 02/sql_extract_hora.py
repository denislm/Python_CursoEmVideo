import os
from development.codes.sql_extractor import sql


####### Hora
path_querys = r'\\Brws2002\n_melv\_development\sql_querys_melv\hora'
querys = []
arquivoBaixa = []

for filename in os.listdir(path_querys):
    arquivoBaixa.append(filename.replace('.txt', '.csv'))
    with open(os.path.join(path_querys, filename), 'r', encoding="utf8") as f:  # open in readonly mode
        text = f.read()
        querys.append(text)

foo = sql('BRWCL004-02\SQLPROD1', 'MELV', querys, arquivoBaixa)
foo.thread_async()
