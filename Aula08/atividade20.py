import random
N1 = str (input('primeiro aluno:'))
N2 = str (input('segundo aluno:'))
N3 = str (input('terceiro aluno:'))
N4 = str (input('quarto aluno:'))
lista1 = (N1, N2, N3, N4)
random.shuffle (lista1)
print ('A ordem será')
print (lista1)