import math

angulo = float(input('Digite o angulo que deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('Sendo o angulo {:.2f}, o seno é: {:.2f}, o cosseno é {:.2f}, a tangente é {:.2f}'.format(angulo, seno, cosseno, tangente))