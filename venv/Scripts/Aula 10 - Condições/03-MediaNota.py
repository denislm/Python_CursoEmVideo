n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2) /2
if m == 6.0:
    print('Você está dentro da média, nota:',m)
if m < 6:
    print('Você foi mal!, média:',m)
else:
    print('Você foi bem! parabéns!, média:',m)

