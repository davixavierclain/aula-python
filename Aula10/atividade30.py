número=int(input('Dê um número qualquer:  '))
resultado = número % 2
if  resultado == 0:
    print('O número {} é par!'.format(resultado))
else:
    print('O número {} é ímpar!'.format(resultado))
