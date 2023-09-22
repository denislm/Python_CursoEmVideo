#Ler largura e altura da parede em metros,
# calcule sua area, quantidade de tinta para pinta-la,
#cada litro de tinta pinta uma area de 2m quadrados

largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura * altura
quantTinta = area / 2
print('Sua parede tem a dimensão de {}x{} e área de: {:.2f} m²'.format(largura,altura,area) )
print('É necessário: {:.2f} litros de tinta, para pintar {:.2f} m² de parede!'.format(quantTinta, area))
