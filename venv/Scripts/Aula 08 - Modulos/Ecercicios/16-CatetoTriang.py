from math import hypot
compCatetoOposto = float(input('Digite o comprimento do cateto oposto: '))
compCatetoAdjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = hypot(compCatetoOposto, compCatetoAdjacente)
# poderia fazer ((compCatetoOposto **2) + (** (1/2)
print('hipotenusa: {:.2f}'.format(hipotenusa))