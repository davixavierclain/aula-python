from random import randint
c = randint(0, 5)
print('=' * 40)
print('Vou pensar em um número, tente adivinhar...') 
print('=' * 40)
j = int(input('Qual número eu pensei? '))
if j == c:
    print('Parabéns! Você me venceu!')
else:
    print('Ganhei! Eu pensei no número {} e não o {}, seu lixo incompetente'.format(c,j))
 