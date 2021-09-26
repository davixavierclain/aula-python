n = input('Qual o seu nome? ')
print('Tudo maiúsculo: {}'.format(n.upper()))
print('Tudo minúsculo: {}'.format(n.lower()))
lista = n.split()
print('O nome completo possui {} letras'.format(len(''.join(lista))))
print('O seu primeiro nome é {} e possui {} letras'.format(lista[0], len(lista[0])))
#Analisador de texto