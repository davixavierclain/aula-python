d = float(input('qual a distância da sua viangem? '))
s1 = d * 0.50
s2 = d * 0.45
print('Você está prestes a começar uma viagem de {}km'.format(d))
if d >= 200:
    print('E o preço da sua passagem será de R${}'.format(s2))
else:
    print('E o preço da sua passagem será de R${}'.format(s1))