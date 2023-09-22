frase = 'Curso em Video python'
print(frase[0])
print(frase[9:14])
# Pula de 2 em 2
print(frase[9:21:2])
# começa no 0 e vai até posição 05
print(frase[:5])
# começa no 15 e pega o resto
print(frase[15:])
# começa no 9 e vai até o final pulando de 3 em 3
print(frase[9::3])
# Comprimento da frase
print(len(frase))
# Conta letra especificada de 0 a 12
print(frase.count('o',0,13))
# Emcontra frase (posição inicial), se resultar -1, não encontrou
print(frase.find('deo'))
# troca palavra
print(frase.replace('python','Java'))
# maiúsculo, minusculo
print(frase.upper(), frase.lower())
# primeira letra em maiusculo ou todas letras após espaço em maiusculo
print(frase.capitalize(), frase.title())
# Remove espaços iniciais ou finais caso queira retirar iniciais ou finais lstrip ou rstrip
frase2 = '  Curso em video  Python   '
print(frase2.strip())
# Divide palavras por espaços e os junta com traços -
print('-'.join(frase.split()))
frase = frase.split()
print(frase[2])

# imprime texto grande
print("""
Lorem upsum
Lorem Upsum""")