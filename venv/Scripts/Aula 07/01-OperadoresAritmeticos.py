nome = input('Qual o seu nome?: ')
# 20 caracteres
print('Prazer em te conhcer {:20}!'.format(nome))
# Alinha a Direita
print('Prazer em te conhcer {:>20}!'.format(nome))
# Alinha no centro com 20 espaços, preenchidos com o =
print('Prazer em te conhcer {:=^20}!'.format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2

print('A Soma é {} \nO produto é {} \ne a divisão é {:.3f}'.format(s,m,d))
print('A divisão inteira é {}\nA potencia é {}'.format(di, p))