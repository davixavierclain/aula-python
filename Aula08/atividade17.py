import math
x = float (input('Digite o primeiro cateto: '))
x2 = float (input ('Digite o segundo cateto: '))
v = math.hypot(x, x2)
print ('A hipotenusa é : {:2f}'.format(v))