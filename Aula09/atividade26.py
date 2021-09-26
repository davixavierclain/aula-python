f = str(input('Digite uma frase: ')).strip().upper()
print('A letra "A" aparece {} vezes nessa frase'.format(f.count('A')))
print('A mesma letra aparece pela primeira vez na posição {}'
      ' e pela última na {}'.format(f.find('A')+1,f.rfind('A')+1))
#Primeira e última ocorrência de uma string