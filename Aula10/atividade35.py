r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
if r1 + r2 <= r3 or r1 + r3 <= r2 or r2 + r3 <= r1:
    print('É possível')
else:
    print('Não é possível')
    
