nu = int (input('Informe um número: '))
u = nu // 1 % 10
d = nu // 10 % 10
c = nu // 100 % 10
m = nu // 1000 % 10
print ('Analizando {}'.format(nu))
print ('A unidade é {}'.format(u))
print ('A dezena é {}'.format(d))
print ('A centena é {}'.format(c))
print ('O milhar é {}'.format (m))
#Separando dígitos de um número