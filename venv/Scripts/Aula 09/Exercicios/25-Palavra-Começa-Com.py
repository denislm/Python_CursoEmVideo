# verifica se nome da cidade começa com santo
cidade = input('Digite o nome de uma cidade: ').strip().lower()
contem = cidade[0:5] == 'santo'
print(contem)

